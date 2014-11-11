#!/opt/local/bin/python
from geopy.geocoders import Nominatim
import unittest

geolocator = Nominatim()
location = geolocator.geocode("5010 Hawxhurt Ct Antioch CA", timeout=None)

print(location.address)
