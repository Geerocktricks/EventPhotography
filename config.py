import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://geerocktricks:Geerock_1@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass
config_options = {
'development':DevConfig,
'production':ProdConfig
}