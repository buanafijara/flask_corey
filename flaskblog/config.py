import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  # To prevent form/ cookies modification (security purposes)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('DUMMY_EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('DUMMY_EMAIL_PASSWORD')