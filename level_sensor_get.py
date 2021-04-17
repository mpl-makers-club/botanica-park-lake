# file level_sensor_get.py
import requests
import datetime


now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")

r= requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-WTR06")
#print(r)
#print(r.json())
depth = str(r.json()[0]["val_calibrated"])
bat = str(r.json()[1]["val_calibrated"])
signal = str(r.json()[2]["val_calibrated"])



f = open('/home/pi/botanica-park-lake/level_data.txt','a')
f.write(date_stamp + "," + depth + "," + bat + "," + signal + "\n")
f.close()
print("WHI-WTR06 data collected and saved")
