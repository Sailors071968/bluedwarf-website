
            logger.info(f"Loaded {len(self.zip_data)} zip codes into memory")

except Exception as e:
            logger.error(f"Error loading zip code database: {str(e)}")
            # Fallback to empty dict if loading fails
            self.zip_data = {}

    def get_location_info(self, address_or_zip: str) -> Optional[Dict]:
              """Get location information for an address or zip code"""
              import re

        # Extract zip code from address using regex
              zip_pattern = r'\b(\d{5})\b'
              zip_match = re.search(zip_pattern, address_or_zip)

        if zip_match:
                      zip_code = zip_match.group(1)
else:
              # If no zip found, treat the whole string as a zip code
              zip_code = address_or_zip.strip()[:5]

        # Look up the zip code in our database
          location_data = self.zip_data.get(zip_code)

        if location_data:
                      # Return location data with coordinates
                      return {
                                        'city': location_data['city'],
                                        'state': location_data['state'],
                                        'state_name': location_data['state_name'],
                                        'county': location_data['county'],
                                        'zip_code': zip_code,
                                        'coordinates': {
                                                              'latitude': location_data['latitude'],
                                                              'longitude': location_data['longitude']
                                        }
                      }

        return None

    def is_valid_zip(self, zip_code: str) -> bool:
              """Check if a zip code exists in our database"""
              clean_zip = zip_code.strip()[:5]
              return clean_zip in self.zip_data

    def get_zip_count(self) -> int:
              """Get the total number of zip codes loaded"""
              return len(self.zip_data)
