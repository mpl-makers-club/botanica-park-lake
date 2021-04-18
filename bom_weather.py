import requests
import json
import datetime

r = requests.get('http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json')
#print(r.json())
print("extrcting data")
print(r)

