from kakao_chatbot.intent_adapter import IntentAdapter
import json


def execute(data):
    request = json.loads(data)
    intent = request['intent']['name']
    print('Intent: ' + intent)

    matcher = IntentAdapter(intent, request)
    response = matcher.execute()
    data = json.dumps(response)

    return data