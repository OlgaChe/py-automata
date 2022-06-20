import requests

# import config
from partner_api.partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Generates an Access Token
# GET {{baseUrl}}/authenticate
def generate_access_token(client_id, client_secret):
    url = config.get("baseUrl") + "/authenticate"
    headers = {
        'client_id': client_id,
        'client_secret': client_secret,
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    print("\n")
    print("///REQUEST///\n")
    print("GET " + response.request.url + "\n")
    print("///RESPONSE///\n")
    print(response.json())
    print("\n")

    return response
