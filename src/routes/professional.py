from flask import Blueprint, request, jsonify
import sys
import os

professional_bp = Blueprint('professional', __name__)

@professional_bp.route('/register', methods=['POST'])
def register_professional():
      try:
                data = request.get_json()

        # Validate required fields
                required_fields = ['name', 'email', 'phone', 'category', 'company', 'license_number']
                for field in required_fields:
                              if not data.get(field):
                                                return jsonify({'error': f'{field} is required'}), 400

                          # Basic response for professional registration
                          response_data = {
                    'success': True,
                    'message': 'Professional registration submitted successfully',
                    'professional_id': 'temp_id_12345',
                    'status': 'pending_verification'
                }

        return jsonify(response_data)

except Exception as e:
        return jsonify({'error': f'Registration error: {str(e)}'}), 500

@professional_bp.route('/login', methods=['POST'])
def login_professional():
      try:
                data = request.get_json()
                email = data.get('email')
                password = data.get('password')

        if not email or not password:
                      return jsonify({'error': 'Email and password are required'}), 400

        # Basic login response
        response_data = {
                      'success': True,
                      'message': 'Login successful',
                      'token': 'temp_token_12345',
                      'professional': {
                                        'id': 'temp_id_12345',
                                        'name': 'Professional User',
                                        'email': email,
                                        'category': 'agent'
                      }
        }

        return jsonify(response_data)

except Exception as e:
        return jsonify({'error': f'Login error: {str(e)}'}), 500
