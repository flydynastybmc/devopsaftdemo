import requests
import urllib3
import json

# This py is used to manage condition
# -----------------
# run event::add
def add(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the condition :')
    conditionName = input()

    print('input enter date of the condition(MMDD, ODAT, STAT):')
    conditionDate = input()

    condition = {
        "name": conditionName,
        "date": conditionDate
    }
    endpoint = endPoint + '/run/event/' + ctms
    print(endpoint)

    r_condition_add = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=condition,
                                   verify=False)

    return r_condition_add

# -----------------
# run event::delete
def delete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the condition :')
    conditionName = input()

    print('input enter date of the condition(MMDD, ODAT, STAT):')
    conditionDate = input()

    endpoint = endPoint + '/run/event/' + ctms + '/' + conditionName + '/' + conditionDate
    print(endpoint)

    r_condition_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_condition_delete


# -----------------
# run events::get
def get(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input enter name of the condition :')
    conditionName = input()

    print('input enter date of the condition(MMDD, ODAT, STAT):')
    conditionDate = input()

    search_criteria = "name=" + conditionName + "*" + "&date=" + conditionDate + "*"
    #search_criteria = "name=" + conditionName
    endpoint = endPoint + '/run/events?' + search_criteria
    print(endpoint)

    r_condition_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_condition_get

