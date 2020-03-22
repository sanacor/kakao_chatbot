import json
import emoji
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

        self.used_game_sheet_name = '중고 게임'
        self.new_release_sheet_name = '신규 게임'

    def get_used_game_price(self, request=None):
        index = self.get_ordinal(request)
        title_names = self.get_column_from(2, self.used_game_sheet_name)
        price_list = self.get_column_from(3, self.used_game_sheet_name)

        content = title_names[index] + '의 가격은 ' + price_list[index] + '입니다'
        response = self._get_used_game_price_response_format(content)
        return response

    def get_new_release_game_price(self, request=None):
        index = self.get_ordinal(request)
        title_names = self.get_column_from(2, self.new_release_sheet_name)
        price_list = self.get_column_from(3, self.new_release_sheet_name)

        content = title_names[index] + '의 가격은 ' + price_list[index] + '입니다'
        response = self._get_new_release_game_price_response_format(content)
        return response

    def get_used_game_list(self, request=None):
        indices = self.get_column_from(1, self.used_game_sheet_name)
        title_names = self.get_column_from(2, self.used_game_sheet_name)
        stocks = self.get_column_from(4, self.used_game_sheet_name)

        result_string =''
        for index in indices:
            if not self._check_integer(index):
                continue

            if not self._check_integer(stocks[int(index)]):
                continue

            if int(stocks[int(index)]) < 1:
                continue

            line = index + '.' + title_names[int(index)] + self.new_line
            result_string += line

        response = self._get_used_game_list_response_format(result_string)
        return response

    def get_new_release_game_list(self, request=None):
        indices = self.get_column_from(1, self.new_release_sheet_name)
        title_names = self.get_column_from(2, self.new_release_sheet_name)
        stocks = self.get_column_from(4, self.new_release_sheet_name)

        result_string =''
        for index in indices:
            if not self._check_integer(index):
                continue

            if not self._check_integer(stocks[int(index)]):
                continue

            if int(stocks[int(index)]) < 1:
                continue

            line = index + '.' + title_names[int(index)] + self.new_line
            result_string += line

        response = self._get_new_release_game_list_response_format(result_string)
        return response

    def get_ordinal(self, request):
        try:
            c = request['action']['params']['sys_number_ordinal']
            cc = json.loads(c)
            ordinal_number = cc['amount']
            return ordinal_number

        except KeyError:
            raise

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

    def _get_used_game_list_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': emoji.emojize(
                                ":video_game:") + '오늘의 PS4 중고게임이에요!\n' + '"중고 {번호}번\" 를 입력하시면 \n가격을 알려드려요' + emoji.emojize(
                                ":grinning_squinting_face:") + '\n\n' + '예시) 중고 3번'
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

    def _get_new_release_game_list_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': emoji.emojize(
                                ":video_game:") + 'PS4 신규 발매 게임이에요\n' + '"신규 {번호}번\" 를 입력하시면 \n가격을 알려드려요' + emoji.emojize(
                                ":grinning_squinting_face:") + '\n\n' + '예시) 신규 3번'
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


    def _get_used_game_price_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': emoji.emojize(
                                ":video_game:") + content + emoji.emojize(
                                ":grinning_squinting_face:")
                        }
                    }
                ]
            }
        }
        return result

    def _get_new_release_game_price_response_format(self, content):
        result = {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': emoji.emojize(
                                ":video_game:") + content + emoji.emojize(
                                ":grinning_squinting_face:")
                        }
                    }
                ]
            }
        }
        return result


if __name__ == "__main__":
    request = {
  "resource": "/chatbot",
  "path": "/chatbot",
  "httpMethod": "POST",
  "headers": {
    "Accept": "*/*",
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Desktop-Viewer": "True",
    "CloudFront-Is-Mobile-Viewer": "False",
    "CloudFront-Is-SmartTV-Viewer": "False",
    "CloudFront-Is-Tablet-Viewer": "False",
    "CloudFront-Viewer-Country": "KR",
    "Content-Type": "application/json",
    "Host": "ogv6sidwb4.execute-api.ap-northeast-2.amazonaws.com",
    "User-Agent": "AHC/2.1",
    "Via": "1.1 2c60662be4c7e65fe5154df4f9f5d798.cloudfront.net (CloudFront)",
    "X-Amz-Cf-Id": "39YfaL2q07bvBzgkEX-bLg2YNaTB-BrrBM5RtZEJRE7bI6oTqsjxDA==",
    "X-Amzn-Trace-Id": "Root=1-5e626271-b5cfe159acd99ebab49262f3",
    "X-Chappie-Footprint": "chp-4d41d8d966524400805509b08f0206ba",
    "X-Forwarded-For": "219.249.231.42, 130.176.30.140",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https",
    "X-Request-Id": "chp-ea31ab22161e492faa1cb4bbf23416d5"
  },
  "multiValueHeaders": {
    "Accept": [
      "*/*"
    ],
    "CloudFront-Forwarded-Proto": [
      "https"
    ],
    "CloudFront-Is-Desktop-Viewer": [
      "True"
    ],
    "CloudFront-Is-Mobile-Viewer": [
      "False"
    ],
    "CloudFront-Is-SmartTV-Viewer": [
      "False"
    ],
    "CloudFront-Is-Tablet-Viewer": [
      "False"
    ],
    "CloudFront-Viewer-Country": [
      "KR"
    ],
    "Content-Type": [
      "application/json"
    ],
    "Host": [
      "ogv6sidwb4.execute-api.ap-northeast-2.amazonaws.com"
    ],
    "User-Agent": [
      "AHC/2.1"
    ],
    "Via": [
      "1.1 2c60662be4c7e65fe5154df4f9f5d798.cloudfront.net (CloudFront)"
    ],
    "X-Amz-Cf-Id": [
      "39YfaL2q07bvBzgkEX-bLg2YNaTB-BrrBM5RtZEJRE7bI6oTqsjxDA=="
    ],
    "X-Amzn-Trace-Id": [
      "Root=1-5e626271-b5cfe159acd99ebab49262f3"
    ],
    "X-Chappie-Footprint": [
      "chp-4d41d8d966524400805509b08f0206ba"
    ],
    "X-Forwarded-For": [
      "219.249.231.42, 130.176.30.140"
    ],
    "X-Forwarded-Port": [
      "443"
    ],
    "X-Forwarded-Proto": [
      "https"
    ],
    "X-Request-Id": [
      "chp-ea31ab22161e492faa1cb4bbf23416d5"
    ]
  },
  "queryStringParameters": None,
  "multiValueQueryStringParameters": None,
  "pathParameters": None,
  "stageVariables": None,
  "requestContext": {
    "resourceId": "ftvrqj",
    "resourcePath": "/chatbot",
    "httpMethod": "POST",
    "extendedRequestId": "I-RRzFPtoE0Fm5w=",
    "requestTime": "06/Mar/2020:14:47:13 +0000",
    "path": "/dev/chatbot",
    "accountId": "113154357195",
    "protocol": "HTTP/1.1",
    "stage": "dev",
    "domainPrefix": "ogv6sidwb4",
    "requestTimeEpoch": 1583506033803,
    "requestId": "e7477f0c-fb1b-409f-be58-b9e553bc2ab1",
    "identity": {
      "cognitoIdentityPoolId": None,
      "accountId": None,
      "cognitoIdentityId": None,
      "caller": None,
      "sourceIp": "219.249.231.42",
      "principalOrgId": None,
      "accessKey": None,
      "cognitoAuthenticationType": None,
      "cognitoAuthenticationProvider": None,
      "userArn": None,
      "userAgent": "AHC/2.1",
      "user": None
    },
    "domainName": "ogv6sidwb4.execute-api.ap-northeast-2.amazonaws.com",
    "apiId": "ogv6sidwb4"
  },
  "body": {
    "bot": {
      "id": "5e0c5cd9b617ea00015aaab8",
      "name": "AIChatbot"
    },
    "intent": {
      "id": "5e5f9ea863420a0001e3691d",
      "name": "중고 PS4 게임 가격 문의",
      "extra": {
        "reason": {
          "code": 1,
          "message": "OK"
        }
      }
    },
    "action": {
      "id": "5e5b9a62377aa80001df8fba",
      "name": "price",
      "params": {
        "sys_number_ordinal": {
          "amount": 3
        }
      },
      "detailParams": {
        "sys_number_ordinal": {
          "origin": "3번",
          "value": {
            "amount": 3
          }
        }
      },
      "clientExtra": {}
    },
    "userRequest": {
      "block": {
        "id": "5e5f9ea863420a0001e3691d",
        "name": "중고 PS4 게임 가격 문의"
      },
      "user": {
        "id": "ea582eb0ab49a28d547ef44a95f06dcc744f2025cb92face5659e201fe40d50c60",
        "type": "botUserKey",
        "properties": {
          "botUserKey": "ea582eb0ab49a28d547ef44a95f06dcc744f2025cb92face5659e201fe40d50c60",
          "plusfriendUserKey": "ScNvVZVG5XH2",
          "bot_user_key": "ea582eb0ab49a28d547ef44a95f06dcc744f2025cb92face5659e201fe40d50c60",
          "plusfriend_user_key": "ScNvVZVG5XH2"
        }
      },
      "utterance": "중고 3번",
      "params": {
        "surface": "Kakaotalk.plusfriend"
      },
      "lang": "ko",
      "timezone": "Asia/Seoul"
    },
    "contexts": []
  },
  "isBase64Encoded": False
}
    gss = GoogleSpreadSheet()
    gss.get_used_game_price(request)
