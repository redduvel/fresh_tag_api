from flask import Blueprint, jsonify
from datetime import datetime
import os
from api.db.supabase_client import get_supabase_client

server_bp = Blueprint('server', __name__, url_prefix='/api/server')

@server_bp.route('/status', methods=['GET'])
def server_status():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
                    
    supabase_connected = False
    if supabase_url and supabase_key:
        try:
            supabase = get_supabase_client()
            supabase_connected = True
        except Exception as e:
            server_bp.logger.error(f"Supabase connection error: {e}")
    
    return jsonify({
        'status': 'online',
        'timestamp': datetime.now().isoformat(),
        'supabase_connected': supabase_connected
    })
