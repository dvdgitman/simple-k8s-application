"""Pytest configuration and fixtures for testing."""
import pytest
from app.app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a test application instance."""
    flask_app.config.update({
        'TESTING': True,
    })
    yield flask_app


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a test CLI runner for the Flask application."""
    return app.test_cli_runner()
