import json
import requests

# import config
from partner_api import partner_api_config

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
    print(json.dumps(json.loads(response.request.body), indent=2))
    print("\n")
    print("///RESPONSE///\n")
    print(json.dumps(response.json(), indent=2))
    print("\n")

    return response
