#!/bin/bash
# Start script for Render deployment

# Install dependencies
pip install -r requirements.txt

# Start Gunicorn
gunicorn wsgi:app -c gunicorn.conf.py 