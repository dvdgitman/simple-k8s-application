from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint returning basic info."""
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'running',
        'hostname': socket.gethostname(),
        'version': '1.0.0'
    })
