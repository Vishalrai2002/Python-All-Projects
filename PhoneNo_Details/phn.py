
# Below code is only tell the your first company name when you purchased the sim not giving the information 
# about the new sim company like whethrer you port your sim or not, it doesn't care it only tell about the old company

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your Moblie No: with +.. ")
phone=phonenumbers.parse(number)

time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en");

print("Phone No: ",phone)
print("TimeZone: ",time)
print("Carrier Name: ",car)
print("Country: ",reg)
