
    def get_city_size_category(self, city: str, state: str) -> str:
              """Determine city size category for property value calculation"""
              # Simple heuristic based on common city name patterns
              city_lower = city.lower()

        # Large cities (common large city names)
              large_city_indicators = ['city', 'heights', 'beach', 'springs', 'valley', 'hills']
              if any(indicator in city_lower for indicator in large_city_indicators):
                            return 'large_city'

              # Small cities/rural (common small place indicators)
              small_indicators = ['ville', 'town', 'burg', 'field', 'wood', 'dale', 'view']
              if any(indicator in city_lower for indicator in small_indicators):
                            return 'small_city'

              # Default to medium city
              return 'medium_city'

    def estimate_property_value(self, city: str, state: str, county: str = None) -> int:
              """Estimate property value for a location"""
              # Get state multiplier
              state_multiplier = self.state_multipliers.get(state.upper(), 1.0)

        # Get city size multiplier
              city_size = self.get_city_size_category(city, state.upper())
              city_multiplier = self.city_size_multipliers[city_size]

        # Calculate base value
              estimated_value = self.base_value * state_multiplier * city_multiplier

        # Add some randomness (+/- 15%)
              variance = random.uniform(0.85, 1.15)
              estimated_value *= variance

        # Round to nearest $1000
              estimated_value = round(estimated_value / 1000) * 1000

        # Ensure minimum value
              estimated_value = max(estimated_value, 50000)

        return int(estimated_value)

    def get_market_description(self, value: int) -> str:
              """Get a market description based on property value"""
              if value >= 800000:
                            return "Luxury Market"
elif value >= 500000:
            return "Premium Market"
elif value >= 300000:
            return "Strong Market"
elif value >= 200000:
            return "Stable Market"
else:
            return "Affordable Market"

    def get_monthly_rent_estimate(self, property_value: int) -> int:
              """Estimate monthly rent based on property value (1% rule approximation)"""
              monthly_rent = property_value * 0.008  # 0.8% of property value per month
        return round(monthly_rent / 50) * 50  # Round to nearest $50
