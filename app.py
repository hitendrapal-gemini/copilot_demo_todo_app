from flask import Flask
from flask_login import LoginManager
from tasks import tasks 
from config import Config # Import the tasks Blueprint
from user import User, load_user  # User model and loader
from auth import auth  # Auth blueprint for login/logout

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

login_manager.user_loader(load_user)

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(tasks, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')