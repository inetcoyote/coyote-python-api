import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Базовый URL твоего API
BASE_URL = "https://coyote-python-api.onrender.com/"  # ← Замени на свой (например, https://flask-api.onrender.com)
url = f"{BASE_URL}/users"

# Данные нового пользователя
new_user = [{
    "name": "Coyote",
    "email": "coyote@example.com"
}, {
    "name": "Дмитрий",
    "email": "dima@example.com"
}, {
    "name": "Кирилл",
    "email": "baby@example.com"
}]

# Заголовки
headers = {
    "Content-Type": "application/json"
}

try:
    # Выполняем POST-запрос
    response = requests.post(url, json=new_user, headers=headers, timeout=10, verify=False)

    # Проверяем статус ответа
    if response.status_code == 201:
        created_user = response.json()
        print("✅ Пользователь успешно создан!")
        print(f"ID: {created_user['id']}")
        print(f"Имя: {created_user['name']}")
        print(f"Email: {created_user['email']}")
    elif response.status_code == 400:
        error = response.json()
        print(f"❌ Ошибка ввода: {error.get('message', 'Некорректные данные')}")
    else:
        print(f"❌ Ошибка сервера: статус {response.status_code}")
        print("Текст ошибки:", response.text)

except requests.exceptions.ConnectionError:
    print("🔗 Не удалось подключиться. Убедись, что сервер запущен.")
except requests.exceptions.Timeout:
    print("⏰ Время ожидания истекло.")
except requests.exceptions.RequestException as e:
    print(f"🚨 Ошибка запроса: {e}")