import requests
import urllib3
import urllib.request
import json
import os


# This py is config service
# -----------------
# ctm reporting report::get
def reportGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input the reporting template you want to run:')
    template = input()

    search_criteria = template + "?format=pdf"
    endpoint = endPoint + '/reporting/report/' + search_criteria
    print(endpoint)

    r_report_get = requests.get(endpoint, headers={'Authorization': 'Bearer ' + token},
                      verify=False)

    return  r_report_get

# -----------------
# ctm reporting download
def reportDownload(reportURL):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Beginning file download, please input the filename(ext must be pdf, for example job.pdf)')
    filename = input()
    try:
        urllib.request.urlretrieve(reportURL, filename)
    except:
        print("File downloading failed")

    print('File has downloaded')


