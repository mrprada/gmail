"""Get Message with given ID.

"""
from __future__ import print_function

import base64
import email

import httplib2
import os

from apiclient import discovery,errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import re

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'test'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

"""Get a list of Messages from the user's mailbox.
"""

credentials = get_credentials()
https = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=https)


    
def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

#    print ('Message snippet: %s' % message['snippet'])

    return message
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)


def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    print ('Message snippet: %s' % message['snippet'])

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)


def content(msg_id):
    """ Get needed content for Reports from init daily message`s 

    Args : msd_id received from another function

    Returns : 
        A dictionary of lists  with  needed rows from message
    """

    result = (GetMessage(service,'me',msg_id))
    r = base64.urlsafe_b64decode(result['payload']['parts'][1]['body']['data'].encode('ASCII'))
    ololo = re.findall(r'<li.*?>(.*?)</li.*?>', r)
    good = ""
    for i in (ololo):            
#                i.replace("",'')
        good = good + i.replace("<br>"," ") + ","
        good = good.replace("\xc2\xa0", " ")
    good = list(good.split(','))
    max = (len(good)) 
    print(good.min())
    return good
    

print (content('1622532123eb643e'))
#print (len(content('1622532123eb643e')))
    






#    print (re.sub(r'<br>','',i))
        
