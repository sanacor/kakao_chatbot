import gspread
import pandas
from oauth2client.service_account import ServiceAccountCredentials
import time


class GoogleSpreadSheet:
    def __init__(self):
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]

        self.base_path = './'
        self.json_file_name = 'vast-ethos-251302-b8a92651b359.json'
        self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1cln_wC0rRZfo1kfR1-6SYV-duJA4h4mTU3KIvQ0z38M/edit#gid=0'
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.base_path+self.json_file_name, self.scope)
        self.new_line = '\n'
        self.client = gspread.authorize(self.credentials)
        self.used_game_sheet_name = '중고 게임'
        self.new_release_sheet_name = '신규 게임'

    def foo(self):

        excel_file = './우리동네 플스샵.xlsx'  # Please set the filename and path of csv file.

        sh = self.client.open_by_url(self.spreadsheet_url)
        print(time.time())

        #엑셀 읽기
        df = pandas.read_excel(excel_file, encoding=)
        print(time.time())

        # 엑셀 --> csv
        df.to_csv(r'./name.csv', index=None, header=True, encoding='UTF-8')
        print(time.time())

        content = open('./name.csv', 'r').read()
        print(time.time())

        # csv --> gs
        self.client.import_csv(sh.id, content.encode(encoding='utf-8'))
        print(time.time())

print(time.time())
gs = GoogleSpreadSheet()
gs.foo()