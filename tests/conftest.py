import pytest
from flask import current_app as app

@pytest.fixture()
def app():

    # other setup can go here
    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()