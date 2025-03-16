from flask import Blueprint, request, jsonify
from app.db.supabase_client import get_supabase_client

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/invite', methods=['POST'])
def invite():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    supabase = get_supabase_client()
    user = supabase.auth.admin.invite_user_by_email(email, options={'redirect_to': 'freshtag://auth'})
    if user is None:
        return jsonify({'error': 'Failed to invite user'}), 500
    
    return jsonify({'message': 'User invited successfully'}), 200
        