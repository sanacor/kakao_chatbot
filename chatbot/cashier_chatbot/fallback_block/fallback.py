import json


class Fallback:

    def __init__(self):
        pass

    def default_response(self, request=None):
        # with open('./fallback_content.json') as json_file:
        with open('./chatbot/cashier_chatbot/fallback_block/fallback_content.json') as json_file:
            fallback_response = json.load(json_file)
            print('fallback_response')
            print(fallback_response)
            return fallback_response


if __name__ == '__main__':
    fallback = Fallback()
    fallback.default_response()