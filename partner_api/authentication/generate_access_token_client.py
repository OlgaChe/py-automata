import requests

# import global config
from partner_api.global_config import URL

url = URL.get("baseUrl") + "/authenticate"


def generate_access_token(client_id, client_secret):
    headers = {
        'client_id': client_id,
        'client_secret': client_secret,
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.text)

    return response
