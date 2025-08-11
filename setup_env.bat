@echo off
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
@echo ---
@echo Środowisko venv zostało utworzone i zależności zainstalowane.
@echo Aby aktywować środowisko wpisz: venv\Scripts\activate
@echo Aby uruchomić aplikację wpisz: streamlit run app.py
