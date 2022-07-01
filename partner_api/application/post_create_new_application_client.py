import json
from datetime import datetime
import random
import requests

# import config
from partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Creates a new application
# POST {{baseUrl}}/application
def post_create_new_application(token, new_application_json):
    url = config.get("baseUrl") + "/application"

    with open(new_application_json) as json_file:
        json_data = json.load(json_file)
        json_data["owners"][0]["first_name"] = "qa_" + datetime.now().strftime('%m%d%y%H%M%S') + "_FN"
        json_data["owners"][0]["last_name"] = "qa_" + datetime.now().strftime('%m%d%y%H%M%S') + "_LN"
        json_data["owners"][0]["ssn"] = ""
        json_data["owners"][0]["phonenumbers"][0]["number"] = "212" + str(random.randint(0, 9999999)).zfill(10)
        json_data["owners"][0]["emails"][0]["email"] = "email_owner+" + datetime.now().strftime('%m%d%y%H%M%S') + "@example.com"
        json_data["business"]["locations"][0]["phonenumbers"][0]["number"]["value"] = "212" + str(random.randint(0, 9999999)).zfill(10)
        json_data["business"]["locations"][0]["phonenumbers"][1]["number"]["value"] = "212" + str(random.randint(0, 9999999)).zfill(10)
        json_data["business"]["locations"][0]["landlord_mortgage_phonenumber"] = "212" + str(random.randint(0, 9999999)).zfill(10)

    headers = {
        'Token': token,
    }

    response = requests.post(url, headers=headers, json=json_data)

    print("\n")
    print("///REQUEST///\n")
    print("POST " + response.request.url + "\n")
    print(json.dumps(json.loads(response.request.body), indent=2))
    print("\n")
    print("///RESPONSE///\n")
    print(json.dumps(response.json(), indent=2))
    print("\n")

    return response
