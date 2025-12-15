import requests
from testconfig import itemlisturl

url = itemlisturl


# Параметры запроса (будут добавлены к URL как ?tenant_id=1)
params = {
    "tenant_id": 1
}

# Отправка GET‑запроса
response = requests.get(url, params=params)

# Вывод результата
print("Статус-код:", response.status_code)
print("Текст ответа:", response.text)


# Если ответ в формате JSON, можно декодировать:
if response.status_code == 200:
    print("JSON‑ответ:", response.json())
