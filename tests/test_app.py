"""Unit tests for the Flask application endpoints."""
import json
import socket
import pytest


class TestHomeEndpoint:
    """Tests for the home endpoint (/)."""

    @pytest.mark.unit
    def test_home_endpoint_returns_200(self, client):
        """Test that home endpoint returns 200 OK."""
        response = client.get('/')
        assert response.status_code == 200

    @pytest.mark.unit
    def test_home_endpoint_returns_json(self, client):
        """Test that home endpoint returns JSON content type."""
        response = client.get('/')
        assert response.content_type == 'application/json'

    @pytest.mark.unit
    def test_home_endpoint_response_structure(self, client):
        """Test that home endpoint returns expected JSON structure."""
        response = client.get('/')
        data = json.loads(response.data)

        assert 'message' in data
        assert 'status' in data
        assert 'hostname' in data
        assert 'version' in data

    @pytest.mark.unit
    def test_home_endpoint_message_content(self, client):
        """Test that home endpoint returns correct message."""
        response = client.get('/')
        data = json.loads(response.data)

        assert data['message'] == 'Hello from Flask!'
        assert data['status'] == 'running'
        assert data['version'] == '1.0.0'

    @pytest.mark.unit
    def test_home_endpoint_hostname(self, client):
        """Test that home endpoint returns valid hostname."""
        response = client.get('/')
        data = json.loads(response.data)

        # Hostname should match the system hostname
        assert data['hostname'] == socket.gethostname()
        assert isinstance(data['hostname'], str)
        assert len(data['hostname']) > 0


class TestErrorHandling:
    """Tests for error handling."""

    @pytest.mark.unit
    def test_404_on_invalid_endpoint(self, client):
        """Test that invalid endpoints return 404."""
        response = client.get('/invalid-endpoint')
        assert response.status_code == 404

    @pytest.mark.unit
    def test_405_on_invalid_method(self, client):
        """Test that invalid HTTP methods return 405."""
        response = client.post('/')
        assert response.status_code == 405


class TestApplicationConfiguration:
    """Tests for application configuration."""

    @pytest.mark.unit
    def test_app_is_in_testing_mode(self, app):
        """Test that the test app is in testing mode."""
        assert app.config['TESTING'] is True

    @pytest.mark.unit
    def test_app_name(self, app):
        """Test that the app has the correct name."""
        assert app.name == 'app.app'
