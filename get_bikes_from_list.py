#!/usr/bin/env python3
import requests
import json

# https://api.tfl.gov.uk/BikePoint
# commonName

urllink = "https://api.tfl.gov.uk/BikePoint"
address = ""
# address = "Bank of England Museum, Bank"
resp = requests.get(urllink)
location = (json.loads(resp.text))
for item in location:
    if address in str(item):
        locationId = str((item['commonName']))
        print(locationId)

pickAddress = input('Please enter the bike point location name from list above: ')
specificLocation = (json.loads(resp.text))
for item in specificLocation:
    if pickAddress in str(item):
        locationId = str((item['id']))
        print('The location ID for ' + pickAddress + ' is ' + locationId)
try:
    urllink2 = "https://api.tfl.gov.uk/BikePoint/" + locationId
    resp2 = requests.get(urllink2)
    python_data = (json.loads(resp2.text))['additionalProperties']
    for item in python_data:
        if "NbBikes" in str(item):
            print('Number of bikes available at '+ pickAddress + ' is ' + item['value']) 
except KeyError:
    print(f'Cannot find {pickAddress}. Did you pick one of the locations from the list?')



