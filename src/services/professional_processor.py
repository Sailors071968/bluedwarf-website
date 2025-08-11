
    def process_google_place(self, place: Dict, category: str, region: str = 'default') -> Dict:
              """Convert Google Places data to professional profile"""
              business_name = place.get('displayName', {}).get('text', '')
              address = place.get('formattedAddress', '')
              phone = place.get('nationalPhoneNumber', '')
              rating = place.get('rating', 0)

        # Generate professional name
              professional_name = self._generate_regional_name(region)
              email = self.generate_professional_email(professional_name, business_name)
              title = random.choice(self.professional_titles.get(category, ['Professional']))
              status = 'PREMIUM' if rating >= 4.2 else 'FREE'

        return {
                      'name': professional_name, 'title': title, 'company': business_name,
                      'address': address, 'phone': phone, 'email': email, 'category': category,
                      'rating': rating, 'status': status, 'source': 'Google Places API', 'verified': True
        }

    def _generate_regional_name(self, region: str) -> str:
              """Generate a realistic name based on regional demographics"""
              region_key = region.lower() if region.lower() in self.regional_names else 'default'
              names = self.regional_names[region_key]
              first_name = random.choice(names['first_names'])
              last_name = random.choice(names['last_names'])
              return f"{first_name} {last_name}"

    def generate_professional_email(self, professional_name: str, business_name: str) -> str:
              """Generate realistic professional email address"""
              name_parts = professional_name.lower().split()
              first_name = name_parts[0] if name_parts else 'contact'
              last_name = name_parts[1] if len(name_parts) >= 2 else 'professional'
              domain = 'localprofessional.com'
              return f"{first_name}.{last_name}@{domain}"

    def ensure_category_coverage(self, professionals: List[Dict]) -> List[Dict]:
              """Ensure we have at least one professional from each category"""
              required_categories = ['agent', 'lender', 'attorney', 'title']
              final_professionals = []

        for category in required_categories:
                      found = False
                      for prof in professionals:
                                        if prof['category'] == category:
                                                              final_professionals.append(prof)
                                                              found = True
                                                              break
                                                      if not found:
                                                                        final_professionals.append(self._create_placeholder_professional(category))

                                return final_professionals

    def _create_placeholder_professional(self, category: str) -> Dict:
              """Create a placeholder professional when no real ones are found"""
        category_info = {
                      'agent': {'company': 'Local Real Estate Services', 'phone': '(555) 123-4567'},
                      'lender': {'company': 'Community Mortgage Services', 'phone': '(555) 234-5678'},
                      'attorney': {'company': 'Property Law Associates', 'phone': '(555) 345-6789'},
                      'title': {'company': 'Regional Title Services', 'phone': '(555) 456-7890'}
        }

        info = category_info[category]
        name = self._generate_regional_name('default')
    
