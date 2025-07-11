from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password, name):
        self.id = username
        self.password = password
        self.name = name

    def check_password(self, password):
        return self.password == password

# Demo users dictionary: username -> User
users = {
    'pravesh': User('pravesh', 'demo123', 'Pravesh Kumar'),
    'hitendra': User('hitendra', 'demo123', 'Hitendra Pal'),
}
