from flask_login import UserMixin

# Dummy user store for demo purposes
USERS = {
    "admin": {"id": "admin", "name": "Admin User", "password": "password123"},
}

class User(UserMixin):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get(user_id):
        user = USERS.get(user_id)
        if user:
            return User(user["id"], user["name"])
        return None

    @staticmethod
    def validate(username, password):
        user = USERS.get(username)
        if user and user["password"] == password:
            return User(user["id"], user["name"])
        return None
