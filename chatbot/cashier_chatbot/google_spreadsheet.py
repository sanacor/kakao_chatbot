import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheet:
    def __init__(self):
        self.scope = [
            'https://spreadsheets.google.com/feeds'
        ]
        self.base_path = './chatbot/cashier_chatbot/'
        # self.base_path = './'
        self.json_file_name = 'vast-ethos-251302-b8a92651b359.json'
        self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1cln_wC0rRZfo1kfR1-6SYV-duJA4h4mTU3KIvQ0z38M/edit#gid=0'
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.base_path+self.json_file_name, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.new_line = '\n'

    def get_used_title(self):
        sheet = 'sheet1'
        indices = self.get_column_from(1, sheet)
        title_names = self.get_column_from(2, sheet)
        stocks = self.get_column_from(4, sheet)

        result_string =''
        for index in indices:
            if not self._check_integer(index):
                continue

            if not self._check_integer(stocks[int(index)]):
                continue

            # print(int(stocks[int(index)]))
            if int(stocks[int(index)]) < 1:
                continue

            line = index + '.' + title_names[int(index)] + self.new_line
            result_string += line

        response = self._get_response_format(result_string)
        return response

    def get_column_from(self, val, sheet):
        doc = self.gc.open_by_url(self.spreadsheet_url)

        worksheet = doc.worksheet(sheet)
        column_data = worksheet.col_values(val)
        return column_data

    def _check_integer(self, val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    def _get_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '분리된 메시지 테스트'
                        }
                    },
                    {
                        'simpleText': {
                            'text': content
                        }
                    }
                ]
            }
        }
        return result


if __name__ == "__main__":
    gss = GoogleSpreadSheet()
    gss.get_used_title()
