from flask import Flask
from flask_restx import Api, Resource, fields
from flask import jsonify, request

app = Flask(__name__)

# === Настройка API и Swagger ===
api = Api(
    app,
    version='1.0',
    title='User API',
    description='API для управления пользователями с Swagger UI',
    doc='/swagger/'  # Swagger будет доступен по /swagger/
)

# Неймспейс (группировка путей)
ns = api.namespace('users', description='Операции с пользователями')

# Модель данных для Swagger (для документации тела запроса)
user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description='ID пользователя'),
    'name': fields.String(required=True, description='Имя пользователя'),
    'email': fields.String(description='Email пользователя')
})

# Временная "база данных"
users = [
    {"id": 1, "name": "Coyote", "email": "coyote@example.com"},
    {"id": 2, "name": "Dima", "email": "dima@test.com"},
    {"id": 3, "name": "Baby", "email": None}
]


# === Ресурс для работы с пользователями ===
@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """Получить список всех пользователей"""
        return users

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """Создать нового пользователя"""
        data = request.get_json()
        if not data or 'name' not in data:
            return {'error': 'Поле "name" обязательно для создания'}, 400

        new_id = max(u["id"] for u in users) + 1 if users else 1
        new_user = {
            "id": new_id,
            "name": data["name"],
            "email": data.get("email")
        }
        users.append(new_user)
        return new_user, 201


@ns.route('/<int:user_id>')
@ns.param('user_id', 'ID пользователя')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, user_id):
        """Получить пользователя по ID"""
        user = next((u for u in users if u["id"] == user_id), None)
        if user:
            return user
        ns.abort(404, "Запись не найдена")

    @ns.doc('update_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        """Полное обновление пользователя"""
        user = next((u for u in users if u["id"] == user_id), None)
        if not user:
            ns.abort(404, "Запись не найдена")

        data = request.get_json()
        if 'name' not in data:
            return {'error': 'Поле "name" обязательно для обновления'}, 400

        user['name'] = data['name']
        user['email'] = data.get('email')
        return user

    @ns.doc('patch_user')
    @ns.expect(api.model('UserPatch', {
        'name': fields.String(description='Новое имя'),
        'email': fields.String(description='Новый email')
    }))
    @ns.marshal_with(user_model)
    def patch(self, user_id):
        """Частичное обновление пользователя"""
        user = next((u for u in users if u["id"] == user_id), None)
        if not user:
            ns.abort(404, "Запись не найдена")

        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'email' in data:
            user['email'] = data['email']

        return user

    @ns.doc('delete_user')
    def delete(self, user_id):
        """Удалить пользователя"""
        global users
        users_before = len(users)
        users = [u for u in users if u["id"] != user_id]
        if len(users) == users_before:
            ns.abort(404, "Запись не найдена")
        return {'message': 'Запись удалена успешно'}, 200


# === Запуск приложения ===
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)