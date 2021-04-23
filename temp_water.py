import requests
import json
import datetime

now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")
battery = ""
temperature = ""

# Botanica Battery
print("battery data")
try:
    r = requests.get('https://api.particle.io/v1/devices/330045000b47373336373936/string_bat?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
    #print(r.json())
    #print(r.content)
    r_dict = r.json()
    print("JSON")
    print(r_dict)
    print(r_dict['result'])
    battery = r_dict['result']
except:
    print("exception - no battery data - unit may be offline")

# Botanica Temperature
print("temperature lake water data")
try:
    r = requests.get('https://api.particle.io/v1/devices/330045000b47373336373936/string_temp?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
    #print(r.json())
    #print(r.content)
    r_dict = r.json()
    print("JSON")
    print(r_dict)
    print(r_dict['result'])
    temperature = r_dict['result']
except:
    print("exception - no temperature data - unit may be offline")

f = open('/home/pi/botanica-park-lake/temp_water_data.txt','a')
f.write(date_stamp + "," + temperature + "," + battery + "\n")
f.close()
print("Particle electron water temperature data collected and saved")



