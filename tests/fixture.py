import pytest
from ms import app as app_


@pytest.fixture
def app():
    with app_.app_context():
        app_.config.update(TESTING=True)

    yield app_


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
