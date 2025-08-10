@echo off
setlocal
cd /d "%~dp0"
py -3.12 -m venv .venv || py -m venv .venv || python -m venv .venv
".\.venv\Scripts\python.exe" -m pip install --upgrade pip
".\.venv\Scripts\pip.exe" install aiogram==3.12.0 python-dotenv==1.0.1 pydantic==2.7.4
".\.venv\Scripts\python.exe" start.py
pause
