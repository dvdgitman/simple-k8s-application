FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY gunicorn_config.py .
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8080

CMD ["gunicorn", "--config", "gunicorn_config.py", "app.app:app"]

