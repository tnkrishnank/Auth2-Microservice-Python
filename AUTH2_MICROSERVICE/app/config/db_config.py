class MySQLConfig():
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = 'localhost'
    DB_NAME = 'auth2'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False