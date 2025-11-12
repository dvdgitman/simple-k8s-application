#!/usr/bin/env python
"""
Entrypoint script for running the Flask application with gunicorn.
"""
import os
from app.app import app

if __name__ == '__main__':
    # This is for local development/testing
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
