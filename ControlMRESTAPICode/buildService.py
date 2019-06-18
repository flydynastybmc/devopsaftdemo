import requests
import urllib3
import json
import os


# This py is build service
# -----------------
# ctm build <definitionsFile> [deployDescriptorFile]
def build(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    '''
    # -----------------
    # Built
    file = 'C:\\Users\\fwang\\PycharmProjects\\ControlMRESTAPICode\\sampleJobJson\\Jobs.json'

    def_files = {'definitionsFile': open(file, 'rb')}

    r_deployJob = requests.post(endPoint + '/deploy', files=def_files, headers={'Authorization': 'Bearer ' + token},
                      verify=False)
    '''

    # -----------------
    # Built
    file = 'C:\\Users\\fwang\\PycharmProjects\\ControlMRESTAPICode\\sampleJobJson\\Jobs.json'
    uploaded_files = [
        ('definitionsFile', ('Jobs.json', open(file, 'rb'), 'application/json'))
    ]

    r_build_Job = requests.post(endPoint + '/build', files=uploaded_files, headers={'Authorization': 'Bearer ' + token},
                      verify=False)
    print(r_build_Job.content)
    print(r_build_Job.status_code)

    return  r_build_Job

