from oauth2client.service_account import ServiceAccountCredentials
import gspread

def google_sheet():
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("./creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("US Cities").sheet1

    data = sheet.get_all_records()

    return data

