from chatbot.sample_chatbot.intent import Matcher
import json


def execute(data):
    # print(data)
    print('type of data')
    print(type(data))
    data = json.loads(data)
    intent = data['intent']['name']
    print('Intent: '+ intent)
    matcher = Matcher(intent)
    resp = matcher.execute()

    res = {
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': resp
                    }
                }
            ]
        }
    }

    data = json.dumps(res)

    return data