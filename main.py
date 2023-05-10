import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode 
import folium

# Replace 'number' with the phone number you want to locate
print("Enter your phone number on this format e.g +23498348356374, +442345242662 etc")
number = input(">> ")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

Key = 'f8f31182eef5418b81b6aa85471d26f8'
geocoder = OpenCageGeocode(Key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# myMap.save("mylocation.html")
