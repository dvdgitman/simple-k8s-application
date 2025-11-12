# Simple Flask Application

A simple Flask REST API application

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python >= 3.8** (check with `python --version` or `python3 --version`)
- **pip** (Python package manager, usually comes with Python)

### Installing Python

If you don't have Python installed:

**macOS:**
```bash
brew install python@3.14
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.14 python3.14-venv python3-pip
```

## First-Time Setup

Follow these steps to set up the project for the first time:

### 1. Clone the Repository (if needed)

```bash
git clone https://github.com/outbrain-inc/simple-k8s-application.git
cd simple-k8s-application
```

### 2. Create and Activate Virtual Environment

The virtual environment isolates project dependencies from your system Python.

**Create the virtual environment:**
```bash
python3 -m venv .venv
```

**Activate the virtual environment:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

This installs:
- Flask 3.1.0 (web framework)
- Gunicorn 23.0.0 (production WSGI server)


## Running the Application

There are two ways to run the application:

### Development Mode (Recommended for Local Development)

Uses Flask's built-in development server with auto-reload and debug mode:

```bash
python run.py
```

**Features:**
- Auto-reloads when code changes
- Detailed error messages
- Debug mode enabled
- Runs on `http://localhost:5001`

### Production Mode (Gunicorn)

Uses Gunicorn, a production-ready WSGI server:

```bash
./start.sh
```

Or directly:
```bash
gunicorn --config gunicorn_config.py app.app:app
```

**Features:**
- Multiple worker processes
- Better performance
- Production-ready configuration
- Runs on `http://localhost:5000`


## Running Tests

The project includes a comprehensive test suite using pytest.

### Install Test Dependencies

First, install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

This installs:
- pytest 8.3.4 (testing framework)
- pytest-cov 6.0.0 (coverage plugin)
- pytest-flask 1.3.0 (Flask testing utilities)

### Run All Tests

Run the complete test suite:

```bash
pytest
```

### Key Files Explained

- **app/app.py** - Contains the Flask application and all route definitions
- **run.py** - Wrapper script for running Flask development server
- **start.sh** - Bash script to start Gunicorn with proper config
- **gunicorn_config.py** - Production server configuration (workers, logging, etc.)
- **requirements.txt** - Lists all Python packages needed

