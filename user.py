from flask_login import UserMixin

# Dummy user store for demo
USERS = {
    'admin': {'id': '1', 'name': 'Admin', 'username': 'admin', 'password': 'admin'}
}

class User(UserMixin):
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    @staticmethod
    def get_by_username(username):
        user = USERS.get(username)
        if user:
            return User(user['id'], user['name'], user['username'], user['password'])
        return None

    def check_password(self, password):
        return self.password == password

def load_user(user_id):
    for user in USERS.values():
        if user['id'] == user_id:
            return User(user['id'], user['name'], user['username'], user['password'])
    return None
