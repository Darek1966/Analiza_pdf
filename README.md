# Analiza PDF 📄

## Opis

Analiza PDF to zaawansowane narzędzie webowe stworzone w Streamlit, które umożliwia kompleksową analizę dokumentów PDF. Aplikacja pozwala na ekstrakcję i analizę tekstu, obrazów, linków oraz metadanych z plików PDF, oferując przyjazny interfejs użytkownika i możliwość pobierania wyodrębnionych elementów.

## Funkcje

- **Ekstrakcja tekstu** - wyodrębnianie całej zawartości tekstowej z dokumentu PDF
- **Podgląd stron** - wizualizacja wszystkich stron dokumentu jako obrazów
- **Ekstrakcja obrazów** - wyodrębnianie wszystkich obrazów osadzonych w dokumencie PDF
- **Wykrywanie linków** - automatyczne wykrywanie i wyświetlanie linków URL zawartych w dokumencie
- **Analiza metadanych** - wyświetlanie metadanych dokumentu (autor, data utworzenia, itp.)
- **Pobieranie wyników** - możliwość pobrania wyodrębnionych elementów (tekst, obrazy, linki, metadane)

## Instalacja

### Wymagania wstępne

- Python 3.7 lub nowszy
- Git (opcjonalnie)

### Kroki instalacji

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/twojaNazwaUzytkownika/Analiza_pdf.git
   cd Analiza_pdf
   ```
2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie, ale zalecane):

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/macOS
   source venv/bin/activate
   ```
3. Zainstaluj wymagane zależności:

   ```bash
   pip install -r requirements.txt
   ```
4. Uruchom aplikację:

   ```bash
   streamlit run app.py
   ```
5. Alternatywnie, możesz użyć skryptu konfiguracyjnego (tylko Windows):

   ```bash
   setup_env.bat
   ```

## Użycie

1. Uruchom aplikację za pomocą komendy `streamlit run app.py`
2. Otwórz przeglądarkę internetową pod adresem wyświetlonym w terminalu (domyślnie http://localhost:8501)
3. Wgraj jeden lub więcej plików PDF za pomocą przycisku "Wgraj jeden lub więcej plików PDF"
4. Przełączaj się między zakładkami, aby przeglądać różne aspekty dokumentu:
   * **Tekst** - pełna zawartość tekstowa dokumentu
   * **Obrazy (strony)** - podgląd wszystkich stron dokumentu
   * **Obrazy (osadzone)** - wszystkie obrazy osadzone w dokumencie
   * **Linki** - wykryte linki URL
   * **Metadane** - informacje o dokumencie

## Wykorzystane technologie

* [Streamlit](https://streamlit.io/) - framework do tworzenia aplikacji webowych w Pythonie
* [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) - biblioteka do przetwarzania dokumentów PDF
* [PyPDF2](https://pypdf2.readthedocs.io/) - biblioteka do manipulacji plikami PDF
* [Pillow](https://pillow.readthedocs.io/) - biblioteka do przetwarzania obrazów
* Python 3.7+ - język programowania

## Współpraca nad projektem

Zachęcamy do współpracy nad projektem! Oto jak możesz się zaangażować:

1. Utwórz fork repozytorium
2. Stwórz nową gałąź dla swojej funkcji (`git checkout -b nowa-funkcja`)
3. Zatwierdź swoje zmiany (`git commit -m 'Dodano nową funkcję'`)
4. Wypchnij gałąź do swojego forka (`git push origin nowa-funkcja`)
5. Otwórz Pull Request

### Wytyczne dotyczące współpracy

* Utrzymuj spójny styl kodu
* Dodawaj komentarze do nowych funkcji
* Aktualizuj dokumentację, gdy wprowadzasz zmiany
* Testuj swój kod przed wysłaniem Pull Request

## Licencja

Ten projekt jest udostępniany na licencji MIT. Szczegółowe informacje znajdują się w pliku [LICENSE](vscode-webview://1qd8v1tula0u43gou3ukfl0snpfh7dthaabr622qdvjsb150mmrk/LICENSE).

## Kontakt
[![Email](https://img.shields.io/badge/Email-Napisz%20do%20mnie-blue?style=for-the-badge&logo=gmail&logoColor=white)](mailto:netdark_1966@op.pl)

[![GitHub](https://img.shields.io/badge/GitHub-Darek1966-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Darek1966)

---
