# Analiza_pdf

Aplikacja Streamlit do analizy plików PDF:

- Wyodrębnianie tekstu
- Podgląd stron jako obrazy (PNG)
- Wyodrębnianie i pobieranie osadzonych obrazów
- Lista linków z dokumentu
- Metadane PDF
- Pobieranie wyników
- Obsługa wielu plików PDF

## Instalacja

1. Uruchom terminal w folderze projektu.
2. Wpisz:
   ```
   .\setup_env.bat
   ```
3. Aktywuj środowisko:
   ```
   venv\Scripts\activate
   ```
4. Uruchom aplikację:
   ```
   streamlit run app.py
   ```

## Wymagania

- Python 3.8+
- Streamlit
- PyMuPDF
- PyPDF2
- Pillow

## Funkcje

- Zakładki: Tekst, Obrazy (strony), Obrazy (osadzone), Linki, Metadane
- Pobieranie wyników do plików
- Obsługa wielu plików PDF jednocześnie

## Licencja

MIT
