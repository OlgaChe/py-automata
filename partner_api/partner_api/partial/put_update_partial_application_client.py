import json
from datetime import datetime
import random

import requests

# import config
from partner_api.partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Update an partial application
# PUT {{baseUrl}}/partial/:uuid
def put_update_partial_application(token, new_application_json, uuid):
    url = config.get("baseUrl") + "/partial/" + uuid

    headers = {
        'Token': token,
    }

    response = requests.put(url, headers=headers, json=new_application_json)

    print("\n")
    print("///REQUEST///\n")
    print("PUT " + response.request.url + "\n")
    print(response.request.body)
    print("\n")
    print("///RESPONSE///\n")
    print(response.json())
    print("\n")

    return response


# token = '3bedf587d3b21eaad83d667e1cf05712314f713a82feb492f681c5b6139ce3a8'
# new_application_json = "./sanity_test/post_create_new_partial_application.json"
# uuid = "test"

# put_update_partial_application(token, new_application_json, uuid)