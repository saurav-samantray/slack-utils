import os
import slack

#This will extract the token from evironment variable
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

#Posting message to slack channel
response = client.chat_postMessage( channel='#sams-cxo-general', text="Hello")

#Uploading a file to slack channel
response = client.files_upload( channels='#sams-cxo-general', file="C:/test.png")

#Posting a message to a user as a user
response = client.chat_postMessage( channel='@vn0yu95', text="test",as_user=True)