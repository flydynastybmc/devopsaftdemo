import requests
import urllib3
import json

# This py is used to manage quantitative resource
# -----------------
# run resource::add
def add(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the quantitative resource:')
    qrName = input()

    print('input enter maximum quantity of quantitative resources available:')
    quantity = input()

    resource = {
        "name": qrName,
        "max": quantity
    }
    endpoint = endPoint + '/run/resource/' + ctms
    print(endpoint)

    r_resource_add = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=resource,
                                   verify=False)

    return r_resource_add

# -----------------
# run resource::delete
def delete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the quantitative resource:')
    qrName = input()

    endpoint = endPoint + '/run/resource/' + ctms + '/' + qrName
    print(endpoint)

    r_resource_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_resource_delete


# -----------------
# run resource::get
def get(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the quantitative resource you want to search, * is for all')
    qrName = input()

    search_criteria = "ctm=" + ctms + "&name=" + qrName + "*"
    endpoint = endPoint + '/run/resources?' + search_criteria
    print(endpoint)

    r_resource_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_resource_get