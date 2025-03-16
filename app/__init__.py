from flask import Flask
from app.server.server import server_bp
from app.auth.auth import auth_bp

def create_app():
    
    app = Flask(__name__)
    
    app.register_blueprint(server_bp)
    app.register_blueprint(auth_bp)

    return app 