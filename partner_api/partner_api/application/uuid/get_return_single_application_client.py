import json
import requests

# import config
from partner_api.partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Returns a single application
# GET {{baseUrl}}/application/:uuid
def get_return_single_applications(token, uuid):
    url = config.get("baseUrl") + "/application/" + uuid

    headers = {
        'Token': token
    }

    response = requests.get(url, headers=headers)

    print("\n")
    print("///REQUEST///\n")
    print("GET " + response.request.url + "\n")
    print("///RESPONSE///\n")
    print(json.dumps(response.json(), indent=2))
    print("\n")

    return response
