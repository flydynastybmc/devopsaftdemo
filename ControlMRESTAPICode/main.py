import requests
import urllib3
import urllib.request
import json
import session
import orderjob
import trackjob
import actionjob
import resourceManagement
import conditionManagement
import configService
import deployService
import reportingService
import buildService

urllib3.disable_warnings()  # disable warnings when creating unverified requests

# -----------------
#Define the login credential
endPoint = 'https://clm-tlv-sucicm:8443/automation-api'
username = 'emuser'
password = 'empass'

# -----------------
#Define the Control-M server and orderId for demo use
ctms = 'clm-tlv-sucicm'
orderId = '001f8'

# -----------------
# login
# -----------------
response_login = session.loginAAPI(endPoint, username, password)

# check if the http request is ok
print(response_login.status_code)
if response_login.status_code != requests.codes.ok:
    exit(1)
else:
    token = response_login.json()['token']
# -----------------
# deploy deploy job
# -----------------
r_deployJob = deployService.deploy(endPoint, token, ctms)
if r_deployJob.status_code != requests.codes.ok:
    errors_in_response = r_deployJob.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("job has been deployed successfully")
    print(json.dumps(r_deployJob.json(), indent=4))


# -----------------
# orderjob
# -----------------
response_orderjob = orderjob.orderjob(endPoint, token, ctms)

# check if the http request is ok
print(response_orderjob.status_code)
if response_orderjob.status_code != requests.codes.ok:
    exit(1)
else:
    print("Folder has been successfully ordered, and its status is ")
    # -----------------
    # track job status, its command is ctm run status <runId> [startIndex]
    # -----------------
    #runId = response_orderjob.json()['runId']
    #r_job_run_status = trackjob.status(endPoint, token, runId)
    #if r_job_run_status.status_code != requests.codes.ok:
    #   exit(1)
    #else:
    #    print(json.dumps(r_job_run_status.json(), indent=4))


# -----------------
# logout
# -----------------
response_logout = session.logoutAAPI(endPoint, token)

# check if the http request is ok
print(response_logout.status_code)
if response_login.status_code != requests.codes.ok:
    exit(1)
else:
    message = response_logout.json()['message']
    print(message)

'''
# -----------------
# orderjob
# -----------------
response_orderjob = orderjob.orderjob(endPoint, token, ctms)

# check if the http request is ok
print(response_orderjob.status_code)
if response_orderjob.status_code != requests.codes.ok:
    exit(1)
else:
    print("Folder has been successfully ordered, and its status is ")
    # -----------------
    # track job status, its command is ctm run status <runId> [startIndex]
    # -----------------
    runId = response_orderjob.json()['runId']
    r_job_run_status = trackjob.status(endPoint, token, runId)
    if r_job_run_status.status_code != requests.codes.ok:
        exit(1)
    else:
        print(json.dumps(r_job_run_status.json(), indent=4))


# -----------------
# build job
# -----------------
r_buildJob = buildService.build(endPoint, token, ctms)
if r_buildJob.status_code != requests.codes.ok:
    errors_in_response = r_buildJob.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("job has been built successfully")
    print(json.dumps(r_buildJob.json(), indent=4))

# -----------------
# free job log by ctm run job::free <jobId>
# -----------------
r_job_free = actionjob.free(endPoint, token, ctms, orderId)
if r_job_free.status_code != requests.codes.ok:
    message = orderId + " was not successfully freed"
else:
    message = r_job_free.json()['message']

print(message)




# -----------------
# orderjob
# -----------------
response_orderjob = orderjob.orderjob(endPoint, token, ctms)

# check if the http request is ok
print(response_orderjob.status_code)
if response_orderjob.status_code != requests.codes.ok:
    exit(1)
else:
    print("Folder has been successfully ordered, and its status is ")
    # -----------------
    # track job status, its command is ctm run status <runId> [startIndex]
    # -----------------
    runId = response_orderjob.json()['runId']
    r_job_run_status = trackjob.status(endPoint, token, runId)
    if r_job_run_status.status_code != requests.codes.ok:
        exit(1)
    else:
        print(json.dumps(r_job_run_status.json(), indent=4))

# -----------------
# track job status by run jobs:status::get
# -----------------
orderId = '001fc'
r_jobs_status_get = trackjob.jobsStatusGet(endPoint, token, ctms, orderId)
if r_jobs_status_get.status_code != requests.codes.ok:
    exit(1)
else:
    print(json.dumps(r_jobs_status_get.json(), indent=4))

# -----------------
# retrieve job output by run job:output::get
# -----------------
r_job_output_search = trackjob.jobLogGet(endPoint, token, ctms, orderId)
if r_job_output_search.status_code != requests.codes.ok:
    exit(1)
else:
    #print(r_job_output_search.content)
    #print(r_job_output_search.raw)
    #print(json.dumps(r_jobs_status_get.json(), indent=4))
    print(r_job_output_search.text)


# -----------------
# retrieve job log by run job:log::get
# -----------------
r_job_log_get = trackjob.jobLogGet(endPoint, token, ctms, orderId)
if r_job_log_get.status_code != requests.codes.ok:
    exit(1)
else:
    print(r_job_log_get.text)


# -----------------
# hold job log by ctm run job::hold <jobId>
# -----------------
r_job_hold = actionjob.hold(endPoint, token, ctms, orderId)
if r_job_hold.status_code != requests.codes.ok:
    message = orderId + " was not successfully held"
else:
    message = r_job_hold.json()['message']

print(message)


# -----------------
# free job log by ctm run job::free <jobId>
# -----------------
r_job_free = actionjob.free(endPoint, token, ctms, orderId)
if r_job_free.status_code != requests.codes.ok:
    message = orderId + " was not successfully freed"
else:
    message = r_job_free.json()['message']

print(message)


# -----------------
# rerun job log by ctm run job::rerun <jobId>
# -----------------
r_job_rerun = actionjob.rerun(endPoint, token, ctms, orderId)
if r_job_rerun.status_code != requests.codes.ok:
    message = orderId + " has not been rerun successfully"
else:
    print(json.dumps(r_job_rerun.json(), indent=4))
    message = orderId + " has been rerun successfully"

print(message)

# -----------------
# setToOk  job log by ctm run job::setToOk  <jobId>
# -----------------
orderId = '001f7'
r_job_setToOk  = actionjob.setToOk(endPoint, token, ctms, orderId)
if r_job_setToOk.status_code != requests.codes.ok:
    message = orderId + " has not been setToOk successfully"
else:
    message = r_job_setToOk.json()['message']

print(message)


# -----------------
# Resource Management run resource::add
# -----------------
r_resource_add = resourceManagement.add(endPoint, token, ctms)
if r_resource_add.status_code != requests.codes.ok:
    message = "QR has not been added successfully"
else:
    message = r_resource_add.json()['message']

print(message)

# -----------------
# Resource Management run resource::delete
# -----------------
r_condition_delete = resourceManagement.delete(endPoint, token, ctms)
if r_condition_delete.status_code != requests.codes.ok:
    print(r_condition_delete.status_code)
    print(json.dumps(r_condition_delete.json(), indent=4))
    errors_in_response = r_condition_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    message = r_condition_delete.json()['message']

print(message)

# -----------------
# Resource Management run resource::get
# -----------------
r_condition_get = resourceManagement.get(endPoint, token, ctms)
if r_condition_get.status_code != requests.codes.ok:
    message = 'Failed to get the QR'
else:
    print(json.dumps(r_condition_get.json(), indent=4))
    message = 'QR has been listed'

print(message)


# -----------------
# Condition Management run condition::add
# -----------------
r_condition_add = conditionManagement.add(endPoint, token, ctms)
if r_condition_add.status_code != requests.codes.ok:
    message = "condition has not been added successfully"
else:
    message = r_condition_add.json()['message']

print(message)

# -----------------
# Condition Management run condition::delete
# -----------------
r_condition_delete = conditionManagement.delete(endPoint, token, ctms)
if r_condition_delete.status_code != requests.codes.ok:
    print(r_condition_delete.status_code)
    print(json.dumps(r_condition_delete.json(), indent=4))
    errors_in_response = r_condition_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    message = r_condition_delete.json()['message']

print(message)

# -----------------
# Resource Management run resource::get
# -----------------
r_condition_get = conditionManagement.get(endPoint, token, ctms)
if r_condition_get.status_code != requests.codes.ok:
    message = "Failed to get the condition"
else:
    print(json.dumps(r_condition_get.json(), indent=4))
    message = 'conditions has been listed'

print(message)

# -----------------
# Config Service ctm config servers::get
# -----------------
r_server_get = configService.serverGet(endPoint, token, ctms)
if r_server_get.status_code != requests.codes.ok:
    message = "Failed to get the server status"
else:
    print(json.dumps(r_server_get.json(), indent=4))
    message = 'server status has been retrieved'

print(message)


# -----------------
# Config Service ctm config server::delete
# -----------------
r_server_delete = configService.serverDelete(endPoint, token, ctms)
if r_server_delete.status_code != requests.codes.ok:
    print(r_server_delete.status_code)
    print(json.dumps(r_server_delete.json(), indent=4))
    errors_in_response = r_server_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    print(json.dumps(r_server_delete.json(), indent=4))
    message = r_server_delete.json()['message']

print(message)


# -----------------
# Config Service ctm config server::add
# -----------------
r_server_add = configService.serverAdd(endPoint, token, ctms)
if r_server_add.status_code != requests.codes.ok:
    print(r_server_add.status_code)
    print(json.dumps(r_server_add.json(), indent=4))
    errors_in_response = r_server_add.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    print(json.dumps(r_server_add.json(), indent=4))
    message = r_server_add.json()['message']

print(message)

# -----------------
# Config Service  config server:remotehosts::get
# -----------------
r_remotehost_get = configService.remotehostsGet(endPoint, token, ctms)
if r_remotehost_get.status_code != requests.codes.ok:
    errors_in_response = r_remotehost_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    print(" The remotehost are as below")
    print(r_remotehost_get.text)


# -----------------
# Config Service  config server:remotehost::delete
# -----------------
r_remotehost_delete = configService.remotehostDelete(endPoint, token, ctms)
if r_remotehost_delete.status_code != requests.codes.ok:
    errors_in_response = r_remotehost_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    message = r_remotehost_delete.json()['message']

print(message)


# -----------------
# Config Service  config server:remotehost::add
# -----------------
r_remotehost_add = configService.remotehostAdd(endPoint, token, ctms)
if r_remotehost_add.status_code != requests.codes.ok:
    errors_in_response = r_remotehost_add.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
else:
    message = r_remotehost_add.json()['message']

print(message)


# -----------------
# Config Service  config server:remotehost::get
# -----------------
r_remotehost_get = configService.remotehostGet(endPoint, token, ctms)
if r_remotehost_get.status_code != requests.codes.ok:
    errors_in_response = r_remotehost_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The remotehost are as below")
    print(json.dumps(r_remotehost_get.json(), indent=4))

# -----------------
# config server:agent:params::get
# -----------------
r_agentparams_get = configService.agentParamsGet(endPoint, token, ctms)
if r_agentparams_get.status_code != requests.codes.ok:
    errors_in_response = r_agentparams_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The agent params are as below")
    print(json.dumps(r_agentparams_get.json(), indent=4))


# -----------------
# config server:agent:params::get
# -----------------
r_agentparams_set = configService.agentParamsSet(endPoint, token, ctms)
if r_agentparams_set.status_code != requests.codes.ok:
    errors_in_response = r_agentparams_set.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The new parameter is as below")
    print(json.dumps(r_agentparams_set.json(), indent=4))

# -----------------
# config server:agent:ping
# -----------------
r_agent_ping = configService.agentPing(endPoint, token, ctms)
if r_agent_ping.status_code != requests.codes.ok:
    errors_in_response = r_agent_ping.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The agent ping result is as below")
    message = r_agent_ping.json()['message']
    print(message)

# -----------------
# config server:agents:get
# -----------------
r_agents_get = configService.agentsGet(endPoint, token, ctms)
if r_agents_get.status_code != requests.codes.ok:
    errors_in_response = r_agents_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The agent list is as below")
    print(json.dumps(r_agents_get.json(), indent=4))

# -----------------
# Condition Management run condition::add
# -----------------
r_condition_add = conditionManagement.add(endPoint, token, ctms)
if r_condition_add.status_code != requests.codes.ok:
    message = "condition has not been added successfully"
else:
    message = r_condition_add.json()['message']

print(message)

# -----------------
# config server:agent::disable
# -----------------
r_agent_disable = configService.agentDisable(endPoint, token, ctms)
if r_agent_disable.status_code != requests.codes.ok:
    errors_in_response = r_agent_disable.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The agent list is as below")
    print(json.dumps(r_agent_disable.json(), indent=4))

# -----------------
# config server:agent::enable
# -----------------
r_agent_enable = configService.agentEnable(endPoint, token, ctms)
if r_agent_enable.status_code != requests.codes.ok:
    errors_in_response = r_agent_enable.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The agent list is as below")
    print(json.dumps(r_agent_enable.json(), indent=4))


# -----------------
# config server:hostgroup:agents::get
# -----------------
r_hostgroup_agents_get = configService.hostgroupAgentsGet(endPoint, token, ctms)
if r_hostgroup_agents_get.status_code != requests.codes.ok:
    errors_in_response = r_hostgroup_agents_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The hostgroup detail is as below")
    print(json.dumps(r_hostgroup_agents_get.json(), indent=4))

# -----------------
# config server:hostgroups::get
# -----------------
r_hostgroups_get = configService.hostgroupsGet(endPoint, token, ctms)
if r_hostgroups_get.status_code != requests.codes.ok:
    errors_in_response = r_hostgroups_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(" The hostgroups are as below")
    print(json.dumps(r_hostgroups_get.json(), indent=4))

# -----------------
# config server:hostgroup:agent::add
# -----------------
r_hostgroup_agent_add = configService.hostgroupAgentAdd(endPoint, token, ctms)
if r_hostgroup_agent_add.status_code != requests.codes.ok:
    errors_in_response = r_hostgroup_agent_add.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(json.dumps(r_hostgroup_agent_add.json()['message'], indent=4))


# -----------------
# config server:hostgroup:agent::delete
# -----------------
r_hostgroup_agent_delete = configService.hostgroupAgentDelete(endPoint, token, ctms)
if r_hostgroup_agent_delete.status_code != requests.codes.ok:
    errors_in_response = r_hostgroup_agent_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(json.dumps(r_hostgroup_agent_delete.json()['message'], indent=4))

# -----------------
# config server:params::get
# -----------------
r_serverparams_get = configService.serverParamsGet(endPoint, token, ctms)
if r_serverparams_get.status_code != requests.codes.ok:
    errors_in_response = r_serverparams_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(json.dumps(r_serverparams_get.json(), indent=4))


# -----------------
# config em:param::set
# -----------------
r_emparam_set = configService.emParamSet(endPoint, token, ctms)
if r_emparam_set.status_code != requests.codes.ok:
    errors_in_response = r_emparam_set.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print(json.dumps(r_emparam_set.json(), indent=4))


# -----------------
# deploy deploy job
# -----------------
r_deployJob = deployService.deploy(endPoint, token, ctms)
if r_deployJob.status_code != requests.codes.ok:
    errors_in_response = r_deployJob.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("job has been deployed successfully")
    print(json.dumps(r_deployJob.json(), indent=4))


# -----------------
# deploy jobs::get
# -----------------
r_deploy_jobs_get = deployService.deployJobsGet(endPoint, token, ctms)
if r_deploy_jobs_get.status_code != requests.codes.ok:
    errors_in_response = r_deploy_jobs_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("job has been exported")
    print(json.dumps(r_deploy_jobs_get.json(), indent=4))


# -----------------
# deploy connectionprofile::delete
# -----------------
r_connectionprofile_delete = deployService.connectionprofilesDelete(endPoint, token, ctms)
if r_connectionprofile_delete.status_code != requests.codes.ok:
    errors_in_response = r_connectionprofile_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("connection profile has been deleted")
    message = r_connectionprofile_delete.json()["message"]
    print(message)

# -----------------
# deploy folder::delete
# -----------------
r_folder_delete = deployService.folderDelete(endPoint, token, ctms)
if r_folder_delete.status_code != requests.codes.ok:
    errors_in_response = r_folder_delete.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("folder has been deleted")
    message = r_folder_delete.json()["message"]
    print(message)


# -----------------
# ctm reporting report::get
# -----------------
r_report_get = reportingService.reportGet(endPoint, token, ctms)
reportURL = ""
if r_report_get.status_code != requests.codes.ok:
    errors_in_response = r_report_get.json()['errors']
    error_message = errors_in_response[0]
    message = error_message["message"]
    print(message)
else:
    print("report has been generated deleted")
    print(json.dumps(r_report_get.json(), indent=4))
    reportURL = r_report_get.json()["reportURL"]

reportingService.reportDownload(reportURL)
'''

