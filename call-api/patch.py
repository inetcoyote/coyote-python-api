import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Базовый URL твоего API
BASE_URL = "https://coyote-python-api.onrender.com/"  # ← Замени на свой (например, на Render)
user_id = 2  # ID пользователя, которого нужно обновить
url = f"{BASE_URL}/users/{user_id}"

# Данные для частичного обновления (можно передавать только то, что меняется)
updated_data = {
    "email": "test@example.com"
    # Поле "name" не передаём — оно не изменится
}

# Заголовки
headers = {
    "Content-Type": "application/json"
}

try:
    # Выполняем PATCH-запрос
    response = requests.patch(url, json=updated_data, headers=headers, timeout=10, verify=False)

    # Проверяем статус ответа
    if response.status_code == 200:
        updated_user = response.json()
        print("✅ Пользователь успешно обновлён (частично):")
        print(f"ID: {updated_user['id']}")
        print(f"Имя: {updated_user['name']}")
        print(f"Email: {updated_user['email']}")
    elif response.status_code == 404:
        print("❌ Пользователь не найден (404)")
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