import pytest
from src.system_design.rest.flask.flask_sqlalchemy.app.config import TestConfig
from src.system_design.rest.flask.flask_sqlalchemy.app.extensions import db as _db
from src.system_design.rest.flask.flask_sqlalchemy.app import create_app


@pytest.fixture
def flask_sql_alchemy_app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def db(flask_sql_alchemy_app):
    _db.init_app(flask_sql_alchemy_app)
    
    with flask_sql_alchemy_app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture
def flask_sql_alchemy_test_client(flask_sql_alchemy_app):
    return flask_sql_alchemy_app.test_client()