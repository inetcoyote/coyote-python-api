from flask import Flask, request, jsonify

# Создаём приложение Flask
app = Flask(__name__)

# Временная "база данных" (в реальном проекте используй БД: SQLite, PostgreSQL и т.д.)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# === Обработка HTTP-запросов ===

# GET / — проверка, что сервер работает
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running!"}), 200

# GET /users — получить всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET /users/<id> — получить пользователя по ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST /users — создать нового пользователя
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Field 'name' is required"}), 400

    new_id = max(u["id"] for u in users) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT /users/<id> — обновить пользователя
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    if 'name' in data:
        user['name'] = data['name']
    return jsonify(user), 200

# DELETE /users/<id> — удалить пользователя
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users_before = len(users)
    users = [u for u in users if u["id"] != user_id]
    if len(users) == users_before:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200


# === Запуск приложения ===
if __name__ == '__main__':
    import os
    # Render, Railway и др. передают PORT через переменную окружения
    port = int(os.environ.get('PORT', 5000))
    # Запуск сервера
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False — обязательно для продакшена!