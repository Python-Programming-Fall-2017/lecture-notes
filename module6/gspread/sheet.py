import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
scope = ['https://spreadsheets.google.com/feeds']
c = SAC.from_json_keyfile_name('python-test-a4398d4edde1.json', scope)
login = gspread.authorize(c)
sp = login.open_by_url('https://docs.google.com/spreadsheets/d/1FW6ZO_NWo9ooGMrx1mau6vGl0JtbLdy3I5lB-DJwvOI/edit#gid=0') # URL of spreadsheet
s1 = sp.worksheet('Sheet1')
s1.update_acell('A3', 99)


