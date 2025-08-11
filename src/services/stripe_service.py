"""
Stripe Payment Service for BlueDwarf Platform
"""
import stripe
import os

class StripeService:
      def __init__(self):
                stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_test_...')

    def create_checkout_session(self, plan_type: str, success_url: str, cancel_url: str):
              """Create Stripe checkout session."""
              try:
                            session = stripe.checkout.Session.create(
                                              payment_method_types=['card'],
                                              line_items=[{'price': 'price_test_basic', 'quantity': 1}],
                                              mode='subscription',
                                              success_url=success_url,
                                              cancel_url=cancel_url,
                            )
                            return {'checkout_url': session.url, 'session_id': session.id}
except Exception as e:
            return None

    def get_subscription_plans(self):
              """Get subscription plans."""
              return {
                  'basic': {'name': 'Basic Plan', 'price': 29.99},
                  'premium': {'name': 'Premium Plan', 'price': 59.99}
              }
