import requests
import urllib3
import json

# -----------------
# run job::hold
def hold(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to hold: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    endpoint = endPoint + '/run/job/' + searchquery + '/hold'

    r_job_hold = requests.post(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_hold

# -----------------
# run job::rerun
def free(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to free: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    endpoint = endPoint + '/run/job/' + searchquery + '/free'

    r_job_free = requests.post(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_free

# -----------------
# run job::rerun
def rerun(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to rerun: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    endpoint = endPoint + '/run/job/' + searchquery + '/rerun'

    r_job_rerun = requests.post(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_rerun

# -----------------
# ctm run job::setToOk <jobId>
def setToOk(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to setToOk: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    endpoint = endPoint + '/run/job/' + searchquery + '/setToOk'

    r_job_setToOk = requests.post(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_setToOk

#For other actions like confirm, kill etc.
#They are similar to rerun. Just use rerun as sample to develop confirm, kill, etc