import requests
import json
from current_conditions import *
from ten_day_forecast import ten_day_forecast
from hurricanes import hurricanes

base_url = 'http://api.wunderground.com/api/1e9e2be706b781ee/'
conditions_extension = 'conditions/'
forecast_10_extension = 'forecast10day/'
hurricane_extension = 'currenthurricane/view.format'
json_ext = '.json'
q = 'q/'

def get_zip():
    zipcode = input('Zipcode?')
    return zipcode








def main():
    zipcode = get_zip()
    cc = current_conditions(zipcode)
    td = ten_day_forecast(zipcode)
    print('The temperature is:', cc['current_observation']['temperature_string'])
    print('The relative humidity is:', cc['current_observation']['relative_humidity'])
    print('The wind-speed is:', cc['current_observation']['wind_mph'],'mph')
    print('It feels like:', cc['current_observation']['feelslike_f'],'F')
    print('The barometric pressure is:', cc['current_observation']['pressure_mb'],'millibars')
    print('The visability is:', cc['current_observation']['visibility_mi'])


main()











#
# if __name__ == "__main__":
#     # execute only if run as a script
#     main()
