import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheet:
    def __init__(self):
        self.scope = [
            'https://spreadsheets.google.com/feeds'
        ]
        self.base_path = './chatbot/sample_chatbot/'
        # self.base_path = './'
        # self.json_file_name = 'quickstart-1562036748915-51f213f47658.json'
        self.json_file_name = 'vast-ethos-251302-b8a92651b359.json'
        json_file_name = 'vast-ethos-251302-b8a92651b359.json'
        # self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Rl82c4gSNdHm7wqwZlPUKZ6RiufNmbFangcaydeW8U0/edit#gid=0'
        self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1cln_wC0rRZfo1kfR1-6SYV-duJA4h4mTU3KIvQ0z38M/edit#gid=0'
        print('0001')
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.base_path+self.json_file_name, self.scope)
        # self.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, self.scope)
        print('0002')
        self.gc = gspread.authorize(self.credentials)
        print('0003')

    def get_items(self):
        print('000A')
        items = self.get_column_from(1)
        str = ' '.join(items)
        print('000B')
        return str

    def get_column_from(self, val):
        # 스프레스시트 문서 가져오기
        print('0004')
        print(self.spreadsheet_url)
        doc = self.gc.open_by_url(self.spreadsheet_url)

        # 시트 선택하기
        worksheet = doc.worksheet('시트1')

        column_data = worksheet.col_values(val)
        return column_data


if __name__ == "__main__":
    gss = GoogleSpreadSheet()
    gss.get_items()
