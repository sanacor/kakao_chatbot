from apis.chatbot.post import api as chatbot

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
    chat_repsponse = chatbot.execute(body)

    response = {
        "statusCode": 200,
        "body": chat_repsponse
    }
    print(response)
    return response


def get_http_components(event):
    path = event['path']
    method = event['httpMethod']
    body = event['body']
    return path, method, body