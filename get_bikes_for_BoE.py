#!/usr/bin/env python3
import requests
import json
#The Bike point location for Bank of England is BikePoints_340"
urllink = "https://api.tfl.gov.uk/BikePoint/BikePoints_340"
resp = requests.get(urllink)
python_data = (json.loads(resp.text))['additionalProperties']
for item in python_data:
    if "NbBikes" in str(item):
        print('Number of bikes avilable is: ' + item['value'])