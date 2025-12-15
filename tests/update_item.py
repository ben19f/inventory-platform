import requests
import json

# URL эндпоинта
url = "http://127.0.0.1:8000/api/items/6/"


# Данные для отправки (в формате словаря Python)
data = {
    "title": "Скелет волка (обновлено)",
    "comment": "Новая выставка"
}

# Заголовки запроса
headers = {
    "Content-Type": "application/json"
}

# Отправка PATCH‑запроса
response = requests.patch(
    url,
    headers=headers,
    data=json.dumps(data)  # Преобразуем словарь в JSON‑строку
)

# Вывод результата
print("Статус‑код:", response.status_code)
print("Текст ответа:", response.text)


# Если ответ в формате JSON, можно получить словарь
if response.headers.get('content-type') == 'application/json':
    print("JSON‑ответ:", response.json())
