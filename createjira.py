import requests
from requests.auth import HTTPBasicAuth
import json

#url = "http://localhost:8123"
#url = "https://outage.atlassian.net/rest/api/2/issue/{NOC-1}"
#data = {'auth_token': 'auth1', 'widget': 'id1', 'title': 'Something1', 'text': 'Some   text', 'moreinfo': 'Subtitle'}
postdata = '{"update":{"worklog": [{"add": {"timeSpent":"started": "2011-07-05T11:05:00.000+0000"}}]},"fields": {"project": {"id": "10000"},"summary": "something wrong","issuetype": {"id": "10000" },"assignee": {"name": "homer"},"reporter": {"name": "smithers"},"priority": {"id": "20000"},"labels": ["bugfix","blitz_test"],"timetracking": { "originalEstimate": "10","remainingEstimate": "5"},"security": {"id": "10000"},"versions": [{"id": "10000"}],"environment": "environment","description": "description","duedate": "2011-03-11","fixVersions": [{"id": "10001"}],"components": [{"id": "10000"}],"customfield_30000": [  "10000","10002"],"customfield_80000": {"value": "red"},"customfield_20000": "06/Jul/11 3:25 PM","customfield_40000": "this is a text field","customfield_70000": ["jira-administrators","jira-software-users"], "customfield_60000": "jira-software-users","customfield_50000": "this is a text area. big text.","customfield_10000": "09/Jun/81"}    }'
data = json.dumps(postdata)
url = "https://outage.atlassian.net/rest/api/2/issue"
headers = {'Content-Type': 'application/json'}
#headers = {'Accept' : 'application/json' }
###############################################################################################################

##############################################################################################################
#headers = {'Accept': 'application/json','Authorization': 'access_token cg4prtq6ErGIKCLa1AHTCDFA' }
#r = requests.get(url, headers=headers)

r = requests.post(url,data=data, headers=headers,auth=HTTPBasicAuth('bitwisher@ukr.net', 'Revolution_123'))
print (r.status_code)
print (r)
