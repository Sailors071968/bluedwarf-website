from flask import Blueprint, request, jsonify

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
      try:
                data = request.get_json()
                zip_code = data.get('zip_code')

        if not zip_code:
                      return jsonify({'error': 'Zip code is required'}), 400

        # $49 per zip code per month subscription
        response_data = {
                      'success': True,
                      'checkout_url': f'https://checkout.stripe.com/pay/cs_test_subscription_{zip_code}',
                      'session_id': f'cs_test_{zip_code}_monthly',
                      'pricing': {
                                        'amount': 4900,  # $49.00 in cents
                                        'currency': 'usd',
                                        'interval': 'month',
                                        'description': f'Monthly access to professional data for zip code {zip_code}'
                      }
        }

        return jsonify(response_data)

except Exception as e:
        return jsonify({'error': f'Checkout session error: {str(e)}'}), 500
