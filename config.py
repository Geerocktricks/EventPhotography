import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    
    SECRET_KEY = os.environ.get('SECRET_KEY')

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