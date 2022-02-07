import requests
import json

# import config
from requests.auth import HTTPBasicAuth

from learning_config import CONF


# simple get example
def get_example():
    url = 'https://www.w3schools.com/python/demopage.js'

    # get request example
    response = requests.get(url)
    # get status code
    print(response.status_code)
    # get json
    print(response.json())

    return response


# get example with params
def get_example_params():
    url = 'http://api.open-notify.org/iss-pass.json'
    # demonstrate how to use the 'params' parameter:
    query = {'lat': '45', 'lon': '180'}
    response = requests.get(url, params=query)
    print(response.json())

    return response


# get example with params inside test
def get_example_parametrized(lat, lon):
    url = 'http://api.open-notify.org/iss-pass.json'
    # demonstrate how to use the 'params' parameter:
    query = {'lat': lat, 'lon': lon}
    response = requests.get(url, params=query)
    print(response.json())

    return response


# get example with params from config file
def get_example_config():
    url = 'http://api.open-notify.org/iss-pass.json'
    # demonstrate how to use the 'params' parameter:
    query = {'lat': CONF.get("lat"), 'lon': CONF.get("lon")}
    response = requests.get(url, params=query)
    print(response.json())

    return response


# simple post example
def post_example():
    url = 'https://www.w3schools.com/python/demopage.php'
    # json as object
    json_obj = {'somekey': 'somevalue'}
    # post example
    response = requests.post(url, data=json_obj)
    print(response.status_code)

    return response


# post example with json file
def post_example_json_file():
    url = 'https://www.w3schools.com/python/demopage.php'
    # json as file
    with open('learning_post_json.json') as json_file:
        json_data = json.load(json_file)
    response = requests.post(url, json=json_data)
    print(response.status_code)

    return response


# get example with basic auth
def get_example_basic_auth():
    requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))


# get example with bearer token
def get_example_bearer_token():
    my_headers = {'Authorization': 'Bearer {access_token}'}
    response = requests.get('http://httpbin.org/headers', headers=my_headers)
