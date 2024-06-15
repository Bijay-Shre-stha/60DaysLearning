import phonenumbers
from phone import get_number
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os
import folium

load_dotenv()

API_KEY = os.getenv("API_KEY")

number = get_number()

try:
    parsed_number = phonenumbers.parse(number)

    if not phonenumbers.is_valid_number(parsed_number):
        raise ValueError("The phone number is not valid.")

    phone_location = geocoder.description_for_number(parsed_number, "en")
    print("Phone Location:", phone_location)

    service_provider = carrier.name_for_number(parsed_number, "en")
    print("Service Provider:", service_provider)

    time_zones = timezone.time_zones_for_number(parsed_number)
    print("Time Zone(s):", time_zones)

    region = geocoder.region_code_for_number(parsed_number)
    print("Region:", region)

    geocoder = OpenCageGeocode(API_KEY)
    query = str(phone_location)
    result = geocoder.geocode(query)

    if result and len(result) > 0:
        phone_latitude = result[0]['geometry']['lat']
        phone_longitude = result[0]['geometry']['lng']
        print("Latitude:", phone_latitude)
        print("Longitude:", phone_longitude)

        map = folium.Map(location=[phone_latitude, phone_longitude], zoom_start=9)
        folium.Marker([phone_latitude, phone_longitude], popup=phone_location).add_to(map)

        path = "./phoneLocation.html"
        map.save(path)
        print("Map saved as Phone_Location.html")
    else:
        print("Geocoding failed. Please check the API key and try again.")
except phonenumbers.NumberParseException as e:
    print(f"Error parsing phone number: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
