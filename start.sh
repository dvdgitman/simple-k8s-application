#!/bin/bash
# Entrypoint script to run the Flask application with gunicorn

exec gunicorn --config gunicorn_config.py app.app:app
