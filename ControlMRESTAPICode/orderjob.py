import requests
import urllib3
import json

def orderjob(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    # -----------------
    # order a job
    # convert to Params
    # >>> payload = {'key1': 'value1', 'key2': 'value2'}
    # >>> r = requests.get('https://httpbin.org/get', params=payload)

    print('\n')
    print("By default, all the jobs under folder of FeiRESTAPIFolder will be ordered")
    print("If you want to order those default jobs, please enter!\n"
          "If you want to order your own jobs, please input the your folder name : ")
    folder = input()
    jobs = "*"
    if folder == "":
        folder = "notokFolder#2"
    else:
        print("please input your jobname to be ordered in folder of " + folder)
        jobs = input()

    # the job which needs to be ordered
    # if any field is not commented with mandatory, then it is optional
    #job = {
        #    "ctm": ctms, #mandatory
        # "folder": folder, #mandatory
        #"jobs": jobs,
        #"variables": [{"arg":"12345"}],
        #"hold": "false",
        #"ignoreCriteria": "true",
        #"independantFlow": "false",
        #"orderDate": "current",
        #"waitForOrderDate": "false",
        #"createDuplicate": "false",
        #"orderIntoFolder": "Recent"
    #}

    #order all
    job = {
        "ctm": ctms,  # mandatory
        "folder": folder,  # mandatory
        "variables": [{"arg": "12345"}],
        "hold": "false",
        "ignoreCriteria": "true",
        "independantFlow": "false",
        "orderDate": "current",
        "waitForOrderDate": "false",
        "createDuplicate": "false",
        "orderIntoFolder": "Recent"
    }
    r_order_job = requests.post(endPoint + '/run/order',
                                headers={'Authorization': 'Bearer ' + token},
                                json=job,
                                verify=False)

    print(r_order_job.status_code)
    print(json.dumps(r_order_job.json(), indent=4))

    return r_order_job

