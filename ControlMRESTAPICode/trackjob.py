import requests
import urllib3
import json

# -----------------
# run status
def status(endPoint, token, runId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print('The  status of runId' + runId + 'will be retrieved: ')
    r_job_status = requests.get(endPoint + '/run/status/' + runId,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)
    return r_job_status

# -----------------
# run jobs:status::get
def jobsStatusGet(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    #Note, you can customize the search criteria, for example jobname, fodlername, hostid,etc
    #please refer to the Automation API Guide for more details

    print('\n')
    print('The job status of ' + orderId + ' will be retrieved. If you want to continue, please Enter!'
            'if you want to track another job, please input its orderid: ')
    orderidByUser = input()
    if orderidByUser == "":
        searchquery = "jobid=" + ctms + ":" + orderId
    else:
        searchquery = "jobid=" + ctms + ":" + orderidByUser

    print(searchquery)

    r_jobs_status_get = requests.get(endPoint + '/run/jobs/status?' + searchquery,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_jobs_status_get

# -----------------
# run job:output::get
def jobOutputGet(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to retrieve its output: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    print("please input the runcnt(if you don't input anything,  the default is the last run.): ")
    runNo = input()
    if runNo == "":
        runNo = '0'

    endpoint = endPoint + '/run/job/' + searchquery + '/output/?runNo=' + runNo;
    print(endpoint)
    r_job_output_get = requests.get(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_output_get

# -----------------
# run job:log::get
def jobLogGet(endPoint, token, ctms, orderId):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('\n')
    print("Default orderid is " + orderId, "or please input the orderid you want to retrieve its log: ")
    orderidByUser = input()
    if orderidByUser != "":
        orderId = orderidByUser

    searchquery = ctms +":" + orderId

    endpoint = endPoint + '/run/job/' + searchquery + '/log'

    r_job_log_get = requests.get(endpoint,
                                headers={'Authorization': 'Bearer ' + token},
                                verify=False)

    return r_job_log_get
