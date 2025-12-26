# inventory-platform
Inventory platform with LLM-powered querying


Cистема инвентаризации, разрабатывается как **API-first SaaS**, с возможностью самостоятельного
развёртывания и интеграции через веб-интерфейс, Telegram-ботов и другие клиенты.


## Описание текущей стадии разработки
- используетс бд SQLite
- эндпоинты
- - добавление, удаление, редактирование, получение 1 строки url = "http://127.0.0.1:8000/api/items/"
- - получение списка url = "http://127.0.0.1:8000/api/items/list/


Инструкция
- скачать репозиторий
- создать виртуальное окружение
- усстановить зависимости pip install requirements.txt или pip install -r requirements.txt (для windows)
- создать бд  python manage.py makemigrations
              python manage.py migrate
