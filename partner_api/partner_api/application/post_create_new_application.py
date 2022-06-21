import json
from datetime import datetime
import random

import requests

# import config
from partner_api.partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Creates a new application
# POST {{baseUrl}}/application
def post_create_new_application():
    url = config.get("baseUrl") + "/application"

    token = '3bedf587d3b21eaad83d667e1cf05712314f713a82feb492f681c5b6139ce3a8'
    new_application_json = "./sanity_test/post_create_new_application.json"

    with open(new_application_json) as json_file:
        json_data = json.load(json_file)
        json_data["owners"][0]["first_name"] = datetime.now().strftime('%m%d%y%H%M%S') + "_FN"
        json_data["owners"][0]["last_name"] = datetime.now().strftime('%m%d%y%H%M%S') + "_LN"
        json_data["owners"][0]["ssn"] = ""
        json_data["owners"][0]["phonenumbers"][0]["number"] = "212" + str(random.randint(0, 9999999)).zfill(7)
        json_data["owners"][0]["emails"][0]["email"] = "email_owner+" + datetime.now().strftime('%m%d%y%H%M%S') + "@example.com"
        json_data["business"]["locations"][0]["phonenumbers"][0]["number"]["value"] = "212" + str(random.randint(0, 9999999)).zfill(7)
        json_data["business"]["locations"][0]["phonenumbers"][1]["number"]["value"] = "212" + str(random.randint(0, 9999999)).zfill(7)
        json_data["business"]["locations"][0]["landlord_mortgage_phonenumber"] = "212" + str(random.randint(0, 9999999)).zfill(7)

    headers = {
        'Token': token,
    }

    response = requests.post(url, headers=headers, json=json_data)

    print("\n")
    print("///REQUEST///\n")
    print("POST " + response.request.url + "\n")
    print(response.request.body)
    print("\n")
    print("///RESPONSE///\n")
    print(response.json())
    print("\n")

    return response


post_create_new_application()
