import requests
import urllib3
import json

def loginAAPI(endPoint, username, password):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    # -----------------
    # retrieve login credential as parameter from main.py
    endpoint = endPoint
    user = username
    passwd = password

    # pass the credential as params
    credentialAAPI = {
        "username": user,
        "password": passwd
    }

    # -----------------
    # login
    #r_login = requests.post(endpoint + '/session/login', json={"username": user, "password": passwd}, verify=False)
    r_login = requests.post(endpoint + '/session/login', json=credentialAAPI, verify=False)

    # Demo how to get the response result
    # print response in default format
    print('print response in default format: ')
    print(r_login)

    # print response in json format
    print('print response in json format: ')
    response_json = r_login.json()
    print(json.dumps(response_json, indent=4))

    # print response in rar/binary/unicode format
    print('print response in raw format: ')
    print(r_login.raw)
    print('print response in unicode format: ')
    print(r_login.text)
    print('print response in binary format: ')
    print(r_login.content)

    # Demo how to use the result in json format
    token = response_json['token']
    print("token is : " + token)

    return r_login


def logoutAAPI(endPoint, token):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    # -----------------
    # retrieve login credential as parameter from main.py
    endpoint = endPoint + '/session/logout'

    #r_login = requests.post(endpoint + '/session/login', json={"username": user, "password": passwd}, verify=False)
    r_logout = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_logout
