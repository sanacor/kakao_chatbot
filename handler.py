import json
import datetime
import json
from apis.chatbot.post import api as chatbot
from chatbot.sample_chatbot.intent import Matcher


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


    path = event['path']
    method = event['httpMethod']
    body = event['body']

    chatbot = ROUTER[path][method]
    product_list = chatbot.execute(body)
    # current_time = datetime.datetime.now().time()
    body = {
        # "message": "Hello, the current time is " + str(current_time)
        "message": "Hello, the current time is "
    }

    response = {
        "statusCode": 200,
        "body": product_list
    }

    return response


# @application.route('/chatbot', methods=['post', 'POST'])
# def register():
#     data = get_response(request)
#     print(data)
#     intent = data['intent']['name']
#     matcher = Matcher(intent)
#     resp = matcher.execute()
#
#     res = {
#         'version': "2.0",
#         'template': {
#             'outputs': [
#                 {
#                     'simpleText': {
#                         # 'text': 'hello I am SANA_002'
#                         'text': resp
#                     }
#                 }
#             ]
#         }
#     }
#
#     data = json.dumps(res)
#     response = make_response(data)
#     response.headers['Content-Type'] = 'application/json'
#     return response
#
#
# @application.route('/summary', methods=['post'])
# def summary():
#     res = {
#         'values': [
#             [1, 'q', 'w', 'e', 'r', 't', 'a b c d', 'q w e r', '', '']
#         ],
#         'name': 'sanacor chatbot',
#         'schema_type': '1.0'
#
#     }
#
#     response = application.response_class(
#         response=json.dumps(res),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
#
#
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     application.debug = True
#     application.run()
#
