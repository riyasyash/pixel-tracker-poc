import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account
def writeToSheet(values):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        secret_file = os.path.join(os.getcwd(), 'credentials.json')

        spreadsheet_id = '<replace-sheet-id>'
        range_name = 'Sheet1!A2:C2'

        credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
        service = discovery.build('sheets', 'v4', credentials=credentials)
        
        data = {
            'values' : values 
        }

        service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()



    except OSError as e:
        print(e)