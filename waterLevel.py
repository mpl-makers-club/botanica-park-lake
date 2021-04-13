import requests
import html
r = requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-WTR06")

print("Water level")
print(r)
print(r.json())

print("ATM")
r= requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-ATC01")
print(r)
print(r.json())
