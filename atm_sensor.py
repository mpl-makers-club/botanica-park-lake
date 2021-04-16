# file atm_sensor_get.py
import requests
#import html
#r = requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-WTR06")

#print("Water level")
#print(r)
#print(r.json())

print("ATM")
r= requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-ATC01")
#print(r)
#print(r.json())
temperature = str(r.json()[0]["val_calibrated"])
atm_pressure = str(r.json()[1]["val_calibrated"])
battery_voltage = str(r.json()[2]["val_calibrated"])
signal_strenth = (r.json()[3]["val_calibrated"])
