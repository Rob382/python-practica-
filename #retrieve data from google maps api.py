#retrieve data from google maps api
from pickle import NONE
import urllib.request, urllib.parse, urllib.error
import json

#note that google is increasingly requiering keys for this api
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('ingresa la ubicacion: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'caracters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('======FAILURE TO RETRIEVE======')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    