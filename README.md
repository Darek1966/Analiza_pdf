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

<div style="display: flex; align-items: center; gap: 15px;">
  <img src="logo.png" alt="Icon" width="70">
  <div style="display: flex; align-items: center; gap: 10px;">
    <span>netdark_1966</span>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
    </svg>
    <a href="mailto:netdark_1966@op.pl">netdark_1966</a>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    <a href="https://github.com/Darek1966">GitHub — Darek1966</a>
  </div>
</div>

---
