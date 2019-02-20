from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(confi_name):

    app = Flask(__name__)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     
     #creating the app configurations
     app.config.from_object(config_options[config_name])


     #initializing flask extensions
     bootstrap.init_app(app)

     return app