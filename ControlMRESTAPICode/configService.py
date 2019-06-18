import requests
import urllib3
import json

# This py is config service
# -----------------
# ctm config servers::get
def serverGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Get Control-M server status')

    endpoint = endPoint + '/config/servers'
    print(endpoint)

    r_server_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_server_get

# -----------------
# ctm config server::delete
def serverDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input Control-M server to delete : ')
    serverToDelete = input()

    endpoint = endPoint + '/config/server/' + serverToDelete
    print(endpoint)

    r_server_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_server_delete

# -----------------
# ctm config server::add
def serverAdd(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of Control-M server to add : ')
    host = input()

    print('Input id of Control-M server to add : ')
    id = input()

    print('Input name of Control-M server to add : ')
    ctm = input()

    print('Input CA port of Control-M server to add : ')
    port = input()

    ctmServer = {
        "host": host,
        "id": id,
        "ctm": ctm,
        "port": port
    }

    endpoint = endPoint + '/config/server/'
    print(endpoint)

    r_server_add = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=ctmServer,
                                   verify=False)

    return r_server_add

# -----------------
# config server:remotehost::add
def remotehostAdd(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of remotehost add : ')
    remotehost = input()

    print('Input port of rehost to add(default is 22) : ')
    port = input()
    if port == "":
        port = 22

    remotehostConfig = {
        "encryptAlgorithm": "BLOWFISH",
        "port": port,
        "remotehost": remotehost
    }

    endpoint = endPoint + '/config/server/' + ctms + "/remotehost/"
    print(endpoint)

    r_remotehost_add = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=remotehostConfig,
                                   verify=False)

    return r_remotehost_add

# -----------------
# config server:remotehost::delete
def remotehostDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of remotehost delete : ')
    remotehost = input()

    endpoint = endPoint + '/config/server/' + ctms + "/remotehost/" + remotehost
    print(endpoint)

    r_remotehost_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_remotehost_delete

# -----------------
# config server:remotehosts::get
def remotehostsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    endpoint = endPoint + '/config/server/' + ctms + "/remotehosts/"
    print(endpoint)

    r_remotehost_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_remotehost_get

# -----------------
# config server:remotehost::get
def remotehostGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('input the remotehost you want to check : ')
    remotehostToGet = input()
    endpoint = endPoint + '/config/server/' + ctms + "/remotehost/" + remotehostToGet
    print(endpoint)

    r_remotehost_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_remotehost_get


# -----------------
# config server:remotehost::delete
def remotehostDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of remotehost delete : ')
    remotehost = input()

    endpoint = endPoint + '/config/server/' + ctms + "/remotehost/" + remotehost
    print(endpoint)

    r_remotehost_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)

    return r_remotehost_delete

# -----------------
# config server:agent:params::get
def agentParamsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of agent to get params : ')
    agentName = input()
    endpoint = endPoint + '/config/server/' + ctms + "/agent/" + agentName + "/params"
    print(endpoint)
    r_agentparams_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_agentparams_get

# -----------------
# config server:agent:param::set
def agentParamsSet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of agent : ')
    agentName = input()

    print('Input parameter name : ')
    name = input()

    print('Input new value for the parameter : ')
    value = input()

    agentParam = {
        "value": value
    }
    endpoint = endPoint + '/config/server/' + ctms + "/agent/" + agentName + "/param/" + name
    print(endpoint)
    r_agentparams_set = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=agentParam,
                                   verify=False)
    return r_agentparams_set


# -----------------
# config server:agent::ping
def agentPing(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of agent to ping: ')
    agentName = input()

    agentParam = {
        "discover": "false",
        "timeout": 60
    }
    endpoint = endPoint + '/config/server/' + ctms + "/agent/" + agentName + "/ping"
    print(endpoint)
    r_agent_ping = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=agentParam,
                                   verify=False)
    return r_agent_ping

# -----------------
# config server:agents::get
def agentsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    endpoint = endPoint + '/config/server/' + ctms + "/agents"
    print(endpoint)
    r_agents_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_agents_get


# -----------------
# config server:agent::disable
def agentDisable(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of agent to disable: ')
    agentName = input()

    endpoint = endPoint + '/config/server/' + ctms + "/agent/" + agentName + "/disable"
    print(endpoint)
    r_agent_disable = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_agent_disable


# -----------------
# config server:agent::enable
def agentEnable(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostname of agent to enable: ')
    agentName = input()

    endpoint = endPoint + '/config/server/' + ctms + "/agent/" + agentName + "/enable"
    print(endpoint)
    r_agent_enable = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_agent_enable


# -----------------
# config server:hostgroup:agents::get
def hostgroupAgentsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostgroup name to check: ')
    hostgroup = input()

    endpoint = endPoint + '/config/server/' + ctms + "/hostgroup/" + hostgroup + "/agents"
    print(endpoint)
    r_hostgroup_agents_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_hostgroup_agents_get

# -----------------
# config server:hostgroup:agents::get
def hostgroupAgentsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostgroup name to check: ')
    hostgroup = input()

    endpoint = endPoint + '/config/server/' + ctms + "/hostgroup/" + hostgroup + "/agents"
    print(endpoint)
    r_hostgroup_agents_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_hostgroup_agents_get

# -----------------
# config server:hostgroups::get
def hostgroupsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    endpoint = endPoint + '/config/server/' + ctms + "/hostgroups"
    print(endpoint)
    r_hostgroups_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_hostgroups_get

# -----------------
# config server:hostgroup:agent::add
def hostgroupAgentAdd(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostgroup name: ')
    hostgroup = input()

    print('Input agent name to add: ')
    agentName = input()

    agentToAdd = {
        "host": agentName
    }

    endpoint = endPoint + '/config/server/' + ctms + "/hostgroup/" + hostgroup + "/agent"
    print(endpoint)
    r_hostgroup_agent_add = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=agentToAdd,
                                   verify=False)
    return r_hostgroup_agent_add

# -----------------
# config server:hostgroup:agent::delete
def hostgroupAgentDelete(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input hostgroup name: ')
    hostgroup = input()

    print('Input agent name to delete: ')
    agentName = input()

    endpoint = endPoint + '/config/server/' + ctms + "/hostgroup/" + hostgroup + "/agent/" + agentName
    print(endpoint)
    r_hostgroup_agent_delete = requests.delete(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_hostgroup_agent_delete

# -----------------
# config server:params::get
def serverParamsGet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    endpoint = endPoint + '/config/server/' + ctms + "/params"
    print(endpoint)
    r_serverparams_get = requests.get(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   verify=False)
    return r_serverparams_get

# -----------------
# config em:param::set
def emParamSet(endPoint, token, ctms):
    urllib3.disable_warnings()  # disable warnings when creating unverified requests

    print('Input em parameter name : ')
    name = input()

    print('Input new value for the em parameter : ')
    value = input()

    emParam = {
        "value": value
    }
    endpoint = endPoint + '/config/em/param/' + name
    print(endpoint)
    r_emparam_set = requests.post(endpoint,
                                   headers={'Authorization': 'Bearer ' + token},
                                   json=emParam,
                                   verify=False)
    return r_emparam_set
