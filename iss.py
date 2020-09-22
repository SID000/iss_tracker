#!/bin/python3

import json
import urllib.request
import webbrowser
import datetime
import sys
import time

url = 'http://api.open-notify.org/astros.json'
answer = urllib.request.urlopen(url)
extracted_data = json.loads(answer.read())
now = datetime.datetime.now()

print('People on the ISS:', extracted_data['number'])

dudes = extracted_data['people']

for p in dudes:
  print(p['name'])


url = 'http://api.open-notify.org/iss-now.json'
Antwort = urllib.request.urlopen (url)
ergebnis = json.loads(Antwort.read())

location = ergebnis['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('latitude: ', lat)
print('longitude: ', lon)

webbrowser.open('https://www.latlong.net/c/?lat='+str(lat)+'&long='+str(lon)+'')

print ('Current date and time: '+(now.strftime('%d-%m-%Y %H:%M:%S')))

sys.stdout = open('test.txt', 'w')

print ('Current date and time: '+(now.strftime('%d-%m-%Y %H:%M:%S')))
print('latitude: ' + str(lat))
print('longitude: ' + str(lon))
print('People on the ISS:', extracted_data['number'])

dudes = extracted_data['people']

for p in dudes:
  print(p['name'])

sys.stdout.close()