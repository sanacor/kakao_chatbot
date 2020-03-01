import json
import datetime
import json
from apis.chatbot.post import api as chatbot
from chatbot.cashier_chatbot.intent import Matcher


ROUTER = {
    '/chatbot': {
        'POST': chatbot
    }
}


def endpoint(event, context):
    print('Event')
    print(event)
    print('Context')
    print(context)

    path, method, body = get_http_components(event)

    chatbot = ROUTER[path][method]
    product_list = chatbot.execute(body)

    response = {
        "statusCode": 200,
        "body": product_list
    }
    print(response)
    return response


def get_http_components(event):
    path = event['path']
    method = event['httpMethod']
    body = event['body']
    return path, method, body