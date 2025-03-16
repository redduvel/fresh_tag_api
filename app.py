import os
from datetime import datetime
from flask import Flask, jsonify, request, redirect, url_for
from dotenv import load_dotenv
from api.supabase_client import get_supabase_client
from api.server.server import server_bp
from api.auth.auth import auth_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(server_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True) 