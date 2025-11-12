"""Gunicorn configuration file."""
import multiprocessing
import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
backlog = 2048

# Worker processes
workers = int(os.environ.get('GUNICORN_WORKERS', 2))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
# '-' sends access logs to stdout and error logs to stderr
# This is ideal for containerized applications and log aggregation
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = os.environ.get('LOG_LEVEL', 'info')
