import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheet:
    def __init__(self):
        self.scope = [
            'https://spreadsheets.google.com/feeds'
        ]
        self.base_path = './chatbot/cashier_chatbot/'
        self.json_file_name = 'vast-ethos-251302-b8a92651b359.json'
        self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1cln_wC0rRZfo1kfR1-6SYV-duJA4h4mTU3KIvQ0z38M/edit#gid=0'
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.base_path+self.json_file_name, self.scope)
        self.gc = gspread.authorize(self.credentials)

    def get_items(self):
        items = self._get_column_from(1)
        str = ' '.join(items)
        response = self._get_response_format(str)
        return response

    def _get_column_from(self, val):
        doc = self.gc.open_by_url(self.spreadsheet_url)

        worksheet = doc.worksheet('시트1')
        column_data = worksheet.col_values(val)
        return column_data

    def _get_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
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
    gss.get_items()
