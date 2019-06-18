import requests
import urllib3
import json
import os


# This py is config service
# -----------------
# ctm deploy <definitionsFile>
def deploy(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    # -----------------
    # Built
    file = 'C:\\Users\\fwang\\PycharmProjects\\ControlMRESTAPICode\\sampleJobJson\\Jobs.json'

    def_files = {'definitionsFile': open(file, 'rb')}

    r_deployJob = requests.post(endPoint + '/deploy', files=def_files, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    return  r_deployJob

# -----------------
# deploy jobs::get
def deployJobsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input the folder you want to export:')
    folder = input()

    search_criteria = "ctm=" + ctms + "&folder=" + folder + "&format=JSON"
    endpoint = endPoint + '/deploy/jobs?' + search_criteria
    print(endpoint)

    r_deploy_jobs_get = requests.get(endpoint, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    return  r_deploy_jobs_get

# -----------------
# deploy connectionprofiles::get
def connectionprofilesGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input agent you want to export:')
    agent = input()

    print('input connectoin profile type you want to export:')
    type = input()

    search_criteria = "ctm=" + ctms + "&agent=" + agent + "&type=" + type
    endpoint = endPoint + '/deploy/connectionprofiles?' + search_criteria
    print(endpoint)

    r_connectionprofile_get = requests.get(endpoint, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    return  r_connectionprofile_get

# -----------------
# deploy connectionprofile::delete
def connectionprofilesDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input agent:')
    agent = input()

    print('input connectoin profile type you want to delete:')
    type = input()

    print('input connectoin profile name you want to delete:')
    name = input()

    search_criteria = ctms + "/" + agent + "/" + type + "/" + name
    endpoint = endPoint + '/deploy/connectionprofile/' + search_criteria
    print(endpoint)

    r_connectionprofile_delete = requests.delete(endpoint, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    print(r_connectionprofile_delete.content)
    print( r_connectionprofile_delete.status_code )
    return  r_connectionprofile_delete

# -----------------
# deploy folder::delete
def folderDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input folder name you want to delete:')
    folder = input()

    search_criteria = ctms + "/" + folder
    endpoint = endPoint + '/deploy/folder/' + search_criteria
    print(endpoint)

    r_folder_delete = requests.delete(endpoint, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    return  r_folder_delete
