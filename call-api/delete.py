import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Базовый URL твоего API
BASE_URL = "https://coyote-python-api.onrender.com/"  # ← Замени на свой (например, https://flask-api.onrender.com)
user_id = 4  # ID пользователя, которого нужно удалить
url = f"{BASE_URL}/users/{user_id}"

try:
    # Выполняем DELETE-запрос
    response = requests.delete(url, timeout=10, verify=False)

    # Проверяем статус ответа
    if response.status_code == 200:
        result = response.json()
        print("✅ Успешно удалено:")
        print(result.get("message", "Пользователь удалён"))
    elif response.status_code == 204:
        # 204 — No Content (сервер ничего не возвращает)
        print("✅ Пользователь удалён (статус 204)")
    elif response.status_code == 404:
        error = response.json()
        print(f"❌ Не найдено: {error.get('message', 'Пользователь не существует')}")
    else:
        print(f"❌ Ошибка сервера: статус {response.status_code}")
        print("Текст ошибки:", response.text)

except requests.exceptions.ConnectionError:
    print("🔗 Не удалось подключиться. Убедись, что сервер запущен.")
except requests.exceptions.Timeout:
    print("⏰ Время ожидания истекло.")
except requests.exceptions.RequestException as e:
    print(f"🚨 Ошибка запроса: {e}")