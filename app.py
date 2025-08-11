import streamlit as st
import fitz  # PyMuPDF
import io
from PIL import Image
from PyPDF2 import PdfReader
import re

def extract_images_from_pdf(doc):
    images = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            images.append({
                "data": image_bytes,
                "ext": ext,
                "page": page_num + 1,
                "index": img_index + 1
            })
    return images

st.set_page_config(page_title="Analiza PDF", page_icon=":page_facing_up:", layout="wide")
st.title("Analiza PDF :page_facing_up:")

uploaded_files = st.file_uploader("Wgraj jeden lub więcej plików PDF", type=["pdf"], accept_multiple_files=True)

if uploaded_files:

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tekst", "Obrazy (strony)", "Obrazy (osadzone)", "Linki", "Metadane"])
    for file in uploaded_files:
        st.subheader(f"Plik: {file.name}")
        progress_bar = st.progress(0, text="Wczytywanie dokumentu...")
        pdf_bytes = file.read()
        progress_bar.progress(10, text="Wczytano plik PDF")
        pdf_stream = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_stream)
        progress_bar.progress(30, text="Wczytano metadane i strony")
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        progress_bar.progress(50, text="Analiza dokumentu...")

        # --- Tekst ---
        with tab1:
            st.markdown(f"### {file.name}")
            text = ""
            for i, page in enumerate(reader.pages):
                text += page.extract_text() or ""
                progress_bar.progress(50 + int(30 * (i+1)/len(reader.pages)), text=f"Przetwarzanie tekstu ({i+1}/{len(reader.pages)})")
            st.markdown('<div style="width:70%; max-width:900px; margin:auto;">', unsafe_allow_html=True)
            st.text_area("Tekst z dokumentu:", text, height=200, key=f"txt_{file.name}")
            st.download_button("Pobierz tekst", text, file_name=f"{file.name}_tekst.txt")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Obrazy (podgląd stron) ---
        with tab2:
            st.markdown(f"### {file.name}")
            st.markdown('<div style="width:70%; max-width:900px; margin:auto;">', unsafe_allow_html=True)
            st.markdown('<div style="overflow-y:auto; max-height:400px;">', unsafe_allow_html=True)
            cols = st.columns(3)
            for page_num in range(len(doc)):
                pix = doc[page_num].get_pixmap(matrix=fitz.Matrix(0.5, 0.5))
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                with cols[page_num % 3]:
                    st.image(img, caption=f"Strona {page_num+1}", use_container_width=True)
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    st.download_button(f"Pobierz stronę {page_num+1}", buf.getvalue(), file_name=f"{file.name}_strona_{page_num+1}.png")
                progress_bar.progress(80 + int(15 * (page_num+1)/len(doc)), text=f"Przetwarzanie obrazów stron ({page_num+1}/{len(doc)})")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Obrazy (osadzone w PDF) ---
        with tab3:
            st.markdown(f"### {file.name}")
            images = extract_images_from_pdf(doc)
            st.markdown('<div style="width:70%; max-width:900px; margin:auto;">', unsafe_allow_html=True)
            st.markdown('<div style="overflow-y:auto; max-height:400px;">', unsafe_allow_html=True)
            if images:
                cols = st.columns(3)
                for idx, img in enumerate(images):
                    with cols[idx % 3]:
                        st.image(img["data"], caption=f"Obraz {img['index']} (strona {img['page']})", use_container_width=True)
                        st.download_button(
                            f"Pobierz obraz {img['index']} (strona {img['page']})",
                            img["data"],
                            file_name=f"{file.name}_obraz_{img['page']}_{img['index']}.{img['ext']}"
                        )
            else:
                st.info("Brak osadzonych obrazów w dokumencie.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            progress_bar.progress(95, text="Przetwarzanie osadzonych obrazów")

        # --- Linki ---
        with tab4:
            st.markdown(f"### {file.name}")
            links = set()
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                found = re.findall(r"https?://\S+", text)
                links.update(found)
                progress_bar.progress(97, text=f"Przetwarzanie linków ({i+1}/{len(reader.pages)})")
            st.markdown('<div style="width:70%; max-width:900px; margin:auto;">', unsafe_allow_html=True)
            st.markdown('<div style="overflow-y:auto; max-height:300px;">', unsafe_allow_html=True)
            if links:
                for idx, link in enumerate(links, 1):
                    st.markdown(f"<div style='word-break:break-all;'><b>{idx}.</b> <a href='{link}' target='_blank'>{link}</a></div>", unsafe_allow_html=True)
                st.download_button("Pobierz listę linków", "\n".join(links), file_name=f"{file.name}_linki.txt")
            else:
                st.info("Brak linków w dokumencie.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Metadane ---
        with tab5:
            st.markdown(f"### {file.name}")
            meta = reader.metadata
            meta_str = "\n".join([f"{k}: {v}" for k, v in meta.items()])
            st.markdown('<div style="width:70%; max-width:900px; margin:auto;">', unsafe_allow_html=True)
            st.markdown('<div style="overflow-y:auto; max-height:200px;">', unsafe_allow_html=True)
            st.code(meta_str)
            st.download_button("Pobierz metadane", meta_str, file_name=f"{file.name}_metadane.txt")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            progress_bar.progress(100, text="Gotowe!")
