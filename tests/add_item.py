import requests
import json
from testconfig import itemurl

url = itemurl

# Данные для отправки
data = {
    "tenant_id": 1,
    "category_id": 10,
    "title": "череп собаки",
    "comment": "Выставка 2025",
    "inventory_number": "EX-002",
    "attributes": {
        "animal_type": "млекопитающее",
        "predator": True,
        "weight_kg": 8
    }
}

# Отправка POST‑запроса
response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)  # Преобразуем dict в JSON‑строку
)

# Вывод результата
print("Статус-код:", response.status_code)
print("Ответ:", response.json())  # если ответ в JSON



# Ответ:
#
# {
#   "id": 1,
#   "tenant_id": 1,
#   "category_id": 10,
#   "title": "Скелет волка",
#   "comment": "Выставка 2025",
#   "inventory_number": "EX-001",
#   "attributes": {
#     "animal_type": "млекопитающее",
#     "predator": true,
#     "weight_kg": 18
#   },
#   "created_at": "2025-12-15T16:00:00Z"
# }