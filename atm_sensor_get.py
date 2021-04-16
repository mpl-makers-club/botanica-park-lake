# file atm_sensor_get.py
import requests
import datetime


now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")

r= requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-ATC01")
#print(r)
#print(r.json())
temp = str(r.json()[0]["val_calibrated"])
pres = str(r.json()[1]["val_calibrated"])
bat = str(r.json()[2]["val_calibrated"])
signal = str(r.json()[3]["val_calibrated"])


f = open('/home/pi/botanica-park-lake/atm_data.txt','a')
f.write(date_stamp + "," + temp + "," + pres + "," + bat + "," + signal + "\n")
f.close()
print("WHI-ATM01 data collected and saved")
