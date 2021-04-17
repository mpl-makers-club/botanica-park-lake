# Retrieve Melbourne Bureau of Meteorology (BOM) rain 7-day forecast data.
# Conversion of XML file to JSON so data extraction is easier
# Extraction of min and max rain data over 7-day forecast
# 11 April 2021
# Edmond Lascaris

import wget
import os
import json
import xmltodict

# Tank size in litres
TANK_SIZE = 6000
# Roof Area in square metres connected to tank
ROOF_AREA = 80

if os.path.exists('/home/pi/botanica-park-lake/BOM.xml'):
    os.remove('/home/pi/botanica-park-lake/BOM.xml')
    print("Existing BOM.xml file removed")

# http://www.bom.gov.au/catalogue/anon-ftp.shtml
# Click on link for - All forecast, warning and observation products
link = 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDV10450.xml'
#link = 'ftp://ftp.bom.gov.au/anon/gen/fwo/IDV10450.txt'
wget.download(link, '/home/pi/botanica-park-lake/BOM.xml')
print("Downloaded new BOM.xml file")

# https://www.geeksforgeeks.org/python-xml-to-json/
with open("/home/pi/botanica-park-lake/BOM.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    json_data = json.dumps(data_dict)

    with open("/home/pi/botanica-park-lake/BOM.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()

# Working with JSON data in Python
# https://realpython.com/python-json/
with open("BOM.json", "r") as json_file:
    data = json.load(json_file)

    rain_forecast_list = [0,0,0,0,0,0,0]
    tank_required_list = [0,0,0,0,0,0,0]
    for i in range(0,8):
        try:
            print("Day ", i)
            type_data = data['product']['forecast']['area'][2]['forecast-period'][i]['element'][1]['@type']
            text_data = data['product']['forecast']['area'][2]['forecast-period'][i]['element'][1]['#text']
            if type_data == 'precipitation_range':
                print("Day ", i)
                print(text_data)
                list_data = text_data.split(' ')
                print(list_data)
                if len(list_data) == 4:
                    # e.g. 0.2 to 4 mm
                    max_rain = float(list_data[2])
                    rain_forecast_list[i-1] = max_rain
                    tank_required = max_rain * ROOF_AREA
                    tank_required_list[i-1] = tank_required
                    print("The min rain is " + list_data[0])
                    print("The max rain is " + list_data[2])
                    #print("Tank volume required is " + str(max_rain * ROOF_AREA) + "L")
                    
                if len(list_data) == 2:
                    # e.g. 3 mm - not sure if this is required
                    print("The forecast rain is " + list_data[0])
        except:
            print("*** Check BOM.JSON - data format has changed ***")
            

print(rain_forecast_list)
print(tank_required_list)

        



