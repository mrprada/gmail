"""Send an email message from the user's account.
"""
from __future__ import print_function
import httplib2
import base64
import email
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import mimetypes
import os
import sys
from apiclient import discovery,errors
import datetime
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
def first():
    return ('Alexander Shpiller')
def second():
    return('Artavazad Tanoyan')
def Another():
    another = raw_input('Enter a case manager :'  )
    return another

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = '/home/opryadka/.credentials/client_secret.json'
APPLICATION_NAME = 'test'
manage = { 1 : first,
           2 : second,
           3 : Another,
}
environment = raw_input('Name of impacted customer Environment  : ')
time = (datetime.datetime.utcnow() - datetime.timedelta(hours=5)).strftime('%H:%M AM %m/%d/%Y EDT')
#time = str(input('Date of Outage in (UTC+2) like %s : ' %datetime.datetime.now))
case_manage = manage[input('\n\n1)Alexander Shpiller\n2)Artavazd Tanoyan\n3)Another\n\nSelect Case Manager: ')]()
impact_time = raw_input('\nTime of ipact in minutes : ')
action = raw_input('\nAction to date: ')



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

credentials = get_credentials()
https = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=https)

sender =  'pryadka1990@gmail.com'
to = 'opryadka@determine.com'
subject = '[noc-outage-alert] %s outage init' %environment
#message_text  = '1)Time: {time} \n2)Case Manage: {case_manage} \n3)Time of impact: {impact_time}\n3)Time of impact: {action}'
message_text = '1. Time: %s \n' %time + '2. Case Manage: %s \n' %case_manage + '3. Time of impact: %s \n'  %impact_time +'4. Action to date: %s \n' %action
def SendMessage(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                         "(or 'y' or 'n').\n")

if (query_yes_no('Do you like to create  Outage ? ', default="no")) == True:
    print('Outage ticket "#"number was created. Let`s create init mail message : \n')
    SendMessage(service,"me",msg_to_send)
print('Result of outage-init message :\n\n','Subject :  %s \n' %subject,'\n%s'%message_text)
if (query_yes_no('Do you like to send this Message ? ', default="no")) == True:
    msg_to_send = CreateMessage(sender, to, subject, message_text)
    SendMessage(service,"me",msg_to_send)
else:
    print('You dont want to create an init message. See you later')



#msg_to_send = CreateMessage(sender, to, subject, message_text)
#SendMessage(service,"me",msg_to_s
