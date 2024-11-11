import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Flask
DEBUG = True  # Set to False in production
UPLOAD_FOLDER = 'uploads'  # Directory for uploaded CSV files
ALLOWED_EXTENSIONS = {'csv'}  # Allowed file extensions for CSV uploads

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'birthday.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Email Configuration
MAIL_SERVER = 'smtp.gmail.com'  # SMTP server address
MAIL_PORT = 587  # SMTP server port (587 for TLS)
MAIL_USE_TLS = True  # Use TLS for secure connection
MAIL_USE_SSL = False  # Use SSL (set to False when using TLS)
MAIL_USERNAME = 'Shilpa'  # SMTP server username
MAIL_PASSWORD = '****'  # SMTP server password
MAIL_DEFAULT_SENDER = 'kulkarnishilpa735@gmail.com'  # Default sender email address

# Admins (for access control)
ADMINS = ['kulkarnishilpa735@gmail.comm']  # List of admin email addresses






