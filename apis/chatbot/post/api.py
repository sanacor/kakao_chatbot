from chatbot.cashier_chatbot.intent import Matcher
import json


def execute(data):
    request = json.loads(data)
    intent = request['intent']['name']
    print('Intent: ' + intent)

    matcher = Matcher(intent, request)
    response = matcher.execute()
    data = json.dumps(response)

    return data