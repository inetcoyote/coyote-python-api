import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Базовый URL твоего API (примеры):
#   - Локально: http://127.0.0.1:5000
#   - На Render: https://flask-user-api.onrender.com

BASE_URL = "https://coyote-python-api.onrender.com/"  # ← Замени на свой URL при необходимости
ENDPOINT = "/users"

# Полный URL
url = BASE_URL + ENDPOINT

try:
    # Выполняем GET-запрос
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    response = requests.get(url, timeout=1000, verify=False)

    # Проверяем статус ответа
    if response.status_code == 200:
        users = response.json()  # Преобразуем ответ в Python-объект (список словарей)

        print("✅ Список пользователей:")
        print("-" * 40)
        for user in users:
            user_id = user.get("id")
            name = user.get("name")
            email = user.get("email", "не указан")
            print(f"ID: {user_id} | Имя: {name} | Email: {email}")
    elif response.status_code == 404:
        print("❌ Ошибка: Эндпоинт /users не найден (404). Проверь URL или запущен ли сервер.")
    else:
        print(f"❌ Ошибка сервера: статус {response.status_code}")
        print("Текст ответа:", response.text)

except requests.exceptions.ConnectionError:
    print("🔗 Не удалось подключиться. Убедись, что сервер запущен и доступен.")
    print(Str(requests.exceptions.ConnectionError))
except requests.exceptions.Timeout:
    print("⏰ Время ожидания ответа истекло.")
except requests.exceptions.RequestException as e:
    print(f"🚨 Ошибка запроса: {e}")