# MercedesScanMinskBot — минимальный старт для Railway (aiogram v3)

## Что внутри
- `app/main.py` — запуск бота, проверка токена, поллинг
- `app/handlers/basic.py` — `/start` + эхо и простая клавиатура
- `app/handlers/__init__.py` — сборка роутеров
- `requirements.txt` — зависимости

## Быстрый деплой на Railway
1. Создай новый проект в Railway и подключи репозиторий **или** загрузи ZIP.
2. В **Settings → Variables** добавь переменную: `BOT_TOKEN` = `<твой токен из @BotFather>`
3. Убедись, что команда запуска: `python -m app.main` (если нужно — задай в Deploy settings).
4. Перезапусти деплой. В логах увидишь:
   - `✅ Bot OK: @...`
   - `▶️ Старт поллинга…`
5. Напиши боту `/start` — ответит и покажет клавиатуру.

## Дальше
Добавляй свои обработчики в `app/handlers/` и включай их в `__init__.py` через
`router.include_router(...)`.