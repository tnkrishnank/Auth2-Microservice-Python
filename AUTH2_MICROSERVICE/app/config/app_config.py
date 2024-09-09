class DevelopmentConfig:
    DEBUG = True
    SERVER_NAME = "127.0.0.1:8000"

class ProductionConfig:
    DEBUG = False
    SERVER_NAME = "127.0.0.1:80"