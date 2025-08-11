
# MercedesScan Bot — деплой на Render (финальная сборка)

## Содержимое
- start.py — точка входа (aiogram v3, polling)
- requirements.txt — зависимости
- Procfile — для Render (Background Worker)
- runtime.txt — версия Python
- .env.example — пример локального запуска
- README_DEPLOY.md — эта инструкция

## Как запустить локально
1) `pip install -r requirements.txt`
2) Создай `.env` на основе `.env.example` и поставь реальный `BOT_TOKEN`.
3) `python start.py`

## Как задеплоить на Render (Background Worker)
1) Залей эти файлы в корень репозитория на GitHub.
2) На https://render.com → New → Background Worker → выбери репозиторий/ветку.
3) Build Command: `pip install -r requirements.txt`
4) Start Command: `python start.py`
5) Environment → Add Variable: `BOT_TOKEN=ВАШ_ТОКЕН`
6) Create Worker → дождись статуса **Running**.
7) Проверь `/start` и `/ping` в Telegram.
