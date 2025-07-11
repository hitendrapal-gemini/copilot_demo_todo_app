from flask import Flask
from tasks import tasks 
from config import Config # Import the tasks Blueprint
from flask_login import LoginManager
from user import User, users  # Import User model

app = Flask(__name__)

app.config['SECRET_KEY'] = Config.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'tasks.login'

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Register the tasks Blueprint
app.register_blueprint(tasks, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')