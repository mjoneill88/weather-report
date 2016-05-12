import requests
import json

base_url = 'http://api.wunderground.com/api/1e9e2be706b781ee/'
conditions_extension = 'conditions/'
forecast_10_extension = 'forecast10day/'
hurricane_extension = 'currenthurricane/view.format'
json_ext = '.json'
q = 'q/'

# http://api.wunderground.com/api/1e9e2be706b781ee/conditions/q/CA/San_Francisco.json

def current_conditions(zipcode):
    response = requests.get(base_url + conditions_extension + q + zipcode + json_ext)
    response = response.json()
    return response









# http://api.wunderground.com/api/1e9e2be706b781ee/currenthurricane/view.format
# http://api.wunderground.com/api/1e9e2be706b781ee/forecast10day/q/CA/San_Francisco.json



#







# saved_ten_day = ten_day_forecast('27012')
# print(saved_ten_day)
    # 'http://api.wunderground.com/api/1e9e2be706b781ee/{}.json'.format(zipcode))

# http://api.wunderground.com/api/1e9e2be706b781ee/forecast10day/q/CA/San_Francisco.json




# class CurrentConditions():
#     '''This class simply will
#     make an HTTP request to an
#     API endpoint and then return the
#     value, based on a zipcode'''


# response = requests.get('http://api.wunderground.com/api/1e9e2be706b781ee/{}.json'.format(zipcode))



#response.json()
