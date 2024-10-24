import requests
#
from .wr_json import scan_json
#
from .wr_json import create_json
#
import json
#
data_api = scan_json(name_file= 'config_api.json')
#
def request_api_data(city_index: int):
    API_KEY = data_api['api_key']
    #
    CITY_NAME = data_api['city_name'][city_index]
    #
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=ua"
    #
    response = requests.get(URL)
    #
    if response.status_code == 200:
        #
        data_dict = json.loads(response.content)
        #
        create_json(name_file= "config_weather.json", value_file= data_dict)
        #
        print(json.dumps(data_dict, indent= 4))
    else:
        #
        print(f"Error: {response.status_code}")