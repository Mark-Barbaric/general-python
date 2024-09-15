import os


class Config:
    API_VERSION = 'v1'
    HOST = '0.0.0.0'
    PORT = os.environ.get("FLASK_PORT", 5000)


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory SQLite database for testing
    TESTING = True
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in testing for simplicity
