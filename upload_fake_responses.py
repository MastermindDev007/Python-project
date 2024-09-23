import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your service account credentials
SCOPES = ['https://www.googleapis.com/auth/forms']
SERVICE_ACCOUNT_FILE = 'path/to/service_account_key.json'

# Load the service account credentials
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, SCOPES)

# Create the Google Forms API client
forms_service = build('forms', 'v1', credentials=creds)

# Replace with your form ID
FORM_ID = 'your_form_id'

# Load the CSV file
with open('fake_responses.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    responses = [row for row in reader]

# Upload the responses to the Google Form
for response in responses:
    body = {
        'requests': [{
            'createResponse': {
                'response': response
            }
        }]
    }
    forms_service.forms().batchUpdate(formId=FORM_ID, body=body).execute()