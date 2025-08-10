@echo off
title MercedesScanMinskBot - Автозапуск
cd /d "E:\боты\MercedesScanMinskBot_v3\MercedesScanMinskBot"

:loop
echo Запуск бота...
call .venv\Scripts\activate
python start.py
echo Бот завершил работу. Перезапуск через 5 секунд...
timeout /t 5 /nobreak >nul
goto loop