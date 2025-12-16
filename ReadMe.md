### Описание проекта:
Это простой REST API для управления пользователями, реализованный на Flask. API поддерживает CRUD-операции (создание, чтение, обновление, удаление) для пользователей. API также интегрировано с
Swagger UI для удобного тестирования и документации.

### Основные возможности:
- Получение списка всех пользователей
- Получение пользователя по ID
- Создание нового пользователя
- Обновление пользователя (полное обновление)
- Частичное обновление пользователя
- Удаление пользователя
- Документация API с использованием Swagger UI
- Поддержка развертывания на платформе Render

### Endpoint для доступа к API:
https://coyote-python-api.onrender.com/

### Swagger UI:
https://coyote-python-api.onrender.com/swagger/

### Технологии:
- Python 3.11.5
- Flask 2.3.3
- Flask-RESTx
- Swagger UI
- Render (для развертывания)

### Развертывание на Render:
- Создайте новый веб-сервис на Render.
- Укажите репозиторий с вашим кодом.
- Установите зависимости:
    - pip install -r requirements.txt
- Запустите приложение:
    - python app.py

### Примеры запросов:
- **Получить список всех пользователей:**
```
curl -X GET http://coyote-python-api.onrender.com/users/
```
- **Получить пользователя по ID:**
```
curl -X GET http://coyote-python-api.onrender.com/users/1
```
- **Создать нового пользователя:**
```
curl -X POST http://coyote-python-api.onrender.com/users/ -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}
```
- **Обновить пользователя (полное обновление):**
```
curl -X PUT http://coyote-python-api.onrender.com/users/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane@example
```
- **Частичное обновление пользователя:**
```
curl -X PATCH http://coyote-python-api.onrender.com/users/1 -H "Content-Type: application/json" -d '{"email": "jane.doe@example.com"}'
```
- **Удалить пользователя:**
```
curl -X DELETE http://coyote-python-api.onrender.com/users/1
```

### Структура проекта:
- app.py: Основной файл приложения
- requirements.txt: Список зависимостей
- runtime.txt: Версия Python
- README.md: Документация проекта

### Лицензия:
- Этот проект лицензирован под лицензией MIT.
