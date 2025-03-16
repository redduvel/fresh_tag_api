import os

# Gunicorn config variables
workers = os.getenv("GUNICORN_WORKERS", "2")
worker_class = "sync"
bind = "0.0.0.0:9890"
timeout = 120
accesslog = "-"
errorlog = "-"
loglevel = "info" 