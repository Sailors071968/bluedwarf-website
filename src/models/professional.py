"""
Professional Model for BlueDwarf Platform
Ensures only authentic professional data is stored and displayed
"""

class Professional:
      def __init__(self):
                self.name = None
                self.title = None
                self.company = None
                self.phone = None
                self.email = None
                self.address = None
                self.zip_code = None
                self.linkedin_photo = None
                self.category = None  # agent, lender, attorney, title
        self.verified = False
        self.source = None  # google_places, linkedin, official_directory

    def validate_authenticity(self):
              """Ensure all data is from verified sources only"""
              required_fields = [self.name, self.company, self.phone, self.category]
              if not all(required_fields):
                            return False

              # Must have verified source
              if self.source not in ['google_places', 'linkedin', 'official_directory']:
                            return False

        return True

    def to_dict(self):
              """Convert to dictionary for API responses"""
              if not self.validate_authenticity():
                            return None

        return {
                      'name': self.name,
                      'title': self.title,
                      'company': self.company,
                      'phone': self.phone,
                      'email': self.email,
                      'address': self.address,
                      'zip_code': self.zip_code,
                      'linkedin_photo': self.linkedin_photo,
                      'category': self.category,
                      'verified': self.verified,
                      'source': self.source
        }
