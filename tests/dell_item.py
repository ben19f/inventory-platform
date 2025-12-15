import requests

# URL эндпоинта (удаляем элемент с ID=1)
url = "http://127.0.0.1:8000/api/items/6/"

# Отправка DELETE‑запроса
response = requests.delete(url)

# Вывод результата
print("Статус-код:", response.status_code)
print("Текст ответа:", response.text)

# Если ответ в формате JSON, можно декодировать
if response.headers.get('content-type') == 'application/json':
    print("JSON‑ответ:", response.json())
