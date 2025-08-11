import requests
import os

class LinkedInAPIService:
      def __init__(self):
                self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')

    def search_professional_photos(self, professional_data, zip_code):
              try:
                            photo_url = self._search_by_location(professional_data, zip_code)
                            professional_data['linkedin_photo'] = photo_url
                            return professional_data
                        except:
            professional_data['linkedin_photo'] = None
            return professional_data

    def _search_by_location(self, professional_data, zip_code):
              try:
                            headers = {'Authorization': f'Bearer {self.access_token}'}
                            response = requests.get(f"https://api.linkedin.com/v2/people-search", headers=headers)
                            return None
                        except:
            return None
