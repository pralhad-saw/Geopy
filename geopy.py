from geopy.geocoders import Nominatim

# Initialize the geolocator with a unique app name
geolocator = Nominatim(user_agent="my_geo_app")

# Input your latitude and longitude as a single string
coordinates = "19.0760, 72.8777"  # Example: Mumbai coordinates

# Perform reverse geocoding
location = geolocator.reverse(coordinates)

# Print the full address or location details
print(location.address)
print(location.raw)  # Detailed dictionary with city, country, postal code, etc.
