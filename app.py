from flask import Flask
from tasks import tasks 
from config import Config # Import the tasks Blueprint
from flask_login import LoginManager
from user import User

app = Flask(__name__)

app.config['SECRET_KEY'] = Config.SECRET_KEY

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Register the tasks Blueprint
app.register_blueprint(tasks, url_prefix='/')

# Register auth blueprint
from auth import auth
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')