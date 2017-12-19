import requests

r = requests.get("https://data.toulouse-metropole.fr/api/records/1.0/search/?dataset=velo-toulouse&lang=fr&geofilter.distance=43.600470%2C+1.445672%2C+750")
print(r.content)