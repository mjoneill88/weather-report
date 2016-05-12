import requests
import json

base_url = 'http://api.wunderground.com/api/1e9e2be706b781ee/'
conditions_extension = 'conditions/'
forecast_10_extension = 'forecast10day/'
hurricane_extension = 'currenthurricane/view.format'
json_ext = '.json'
q = 'q/'

def hurricanes():
    response = requests.get(base_url + hurricane_extension)
    response = response.json()
    return response
