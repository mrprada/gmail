import requests
from requests.auth import HTTPBasicAuth
import json

#url = "http://localhost:8123"
#url = "https://outage.atlassian.net/rest/api/2/issue/{NOC-1}"
#data = {'auth_token': 'auth1', 'widget': 'id1', 'title': 'Something1', 'text': 'Some   text', 'moreinfo': 'Subtitle'}
#postdata = '{  "fields": { "project": { "key" : "NOC"} ,"summary": "customer outage",  "issuetype": { "name": "Outage Task"  },    "description": "h3. BLA BLA BLA",   "assignee": {      "name": "testing"    },    "status": {      "key": "In Progress "      }  }'
postdata = '{ "fields": { "project": { "key": "NOC" }, "summary": " cutomer outage ", "description": "Creating of an issue using project keys and issue type names using the REST API", "assignee": {     "name": "bitwisher"   }, "issuetype": { "name": "Outage task" } } }'
postdata = json.loads(postdata)
url = "https://outage.atlassian.net/rest/api/2/issue"
headers = {'Content-Type': 'application/json'}
#headers = {'Accept' : 'application/json' }
###############################################################################################################

##############################################################################################################
#headers = {'Accept': 'application/json','Authorization': 'access_token cg4prtq6ErGIKCLa1AHTCDFA' }
#r = requests.get(url, headers=headers)

r = requests.post(url,json=postdata, headers=headers,auth=HTTPBasicAuth('bitwisher@ukr.net', 'Revolution_123'))
print (r.text)
print (r.status_code)
print (r)
