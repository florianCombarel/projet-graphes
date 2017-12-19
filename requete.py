import requests
import json

r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=Toulouse&apiKey=397a31b163129affc10acc002c5db644c338ad54")
print(r.content)
data = r.json()
#print(json.dumps(data, indent=4))
#print(data[0]["number"])
data_filtrer = []
print("data = "+str(len(data)))
for x in data:
    pourcentage = x["available_bikes"] * 100 / x["bike_stands"]
    if pourcentage < 10:
        data_filtrer.append(x)
print("data_filtrer = "+str(len(data_filtrer)))
print(json.dumps(data_filtrer, indent=4))

