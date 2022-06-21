import requests

# import config
from partner_api.partner_api import partner_api_config

# set up config
config = partner_api_config.CONF.get("DEV")


# Returns a list of applications.
# GET {{baseUrl}}/application?params
def get_return_list_of_applications(token, filter_param, limit, page, direction, sort):
    url = config.get("baseUrl") + "/application"

    headers = {
        'Token': token
    }

    params = {"filter[]": filter_param, 'limit': limit, 'page': page, 'direction': direction, 'sort': sort}

    response = requests.get(url, headers=headers, params=params)

    print("\n")
    print("///REQUEST///\n")
    print("GET " + response.request.url + "\n")
    print("///RESPONSE///\n")
    print(response.json())
    print("\n")

    return response


# token = ''
# filter_param = ''
# limit = 20
# page = 2
# direction = 'desc'
# sort = 'requested_funding'

# get_return_list_of_applications(token, filter_param, limit, page, direction, sort)
