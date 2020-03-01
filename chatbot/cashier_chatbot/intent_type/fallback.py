import json


class Fallback:

    def __init__(self):
        pass

    def default_response(self):
        with open('./fallback_content.json') as json_file:
            fallback_response = json.load(json_file)
            return fallback_response


if __name__ == '__main__':
    fallback = Fallback()
    fallback.default_response()