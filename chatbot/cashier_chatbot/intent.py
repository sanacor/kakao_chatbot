from chatbot.cashier_chatbot.google_spreadsheet import GoogleSpreadSheet
from chatbot.cashier_chatbot.fallback_block.fallback import Fallback
from chatbot.cashier_chatbot.welcome_block.welcome import Welcome

gss = GoogleSpreadSheet()
fallback = Fallback()
welcome = Welcome()


class Intent:
    WELCOME = '웰컴 블록'
    FALL_BACK = '폴백 블록'

    NEW_PS4_GAME_LIST = '신규 PS4 게임 리스트'
    USED_PS4_GAME_LIST = '중고 PS4 게임 리스트'
    PRICE_OF_NEW_PS4_GAME = '신규 PS4 게임 가격 문의'
    PRICE_OF_USED_PS4_GAME = '중고 PS4 게임 가격 문의'




intent_to_action = {
    Intent.WELCOME: welcome.default_response,
    Intent.FALL_BACK: fallback.default_response,

    Intent.NEW_PS4_GAME_LIST: gss.get_new_release_game_list,
    Intent.USED_PS4_GAME_LIST: gss.get_used_game_list,
    Intent.PRICE_OF_NEW_PS4_GAME: gss.get_new_release_game_price,
    Intent.PRICE_OF_USED_PS4_GAME: gss.get_used_game_price

}

# block_to_block_id = {
#     Intent.NEW_PS4_GAME_LIST: '5e5f9e8c15e0d80001bd7f90',
#     Intent.USED_PS4_GAME_LIST: '5e5f9e99c209c10001dcfd24',
#     Intent.PRICE_OF_NEW_PS4_GAME: '5e5f9ea863420a0001e3691d',
#     Intent.PRICE_OF_USED_PS4_GAME: '5e5f9eb13ad5250001d682b2'
# }


class Matcher:

    def __init__(self, intent, request):
        self.intent = intent
        self.request = request

    def execute(self):
        try:
            if self.intent not in intent_to_action:
                print('No matching intent'+self.intent)
                return
            action = intent_to_action[self.intent]
            # fallback_response = fallback.default_response()
            # quick_replies = fallback_response['template']['quickReplies']
            print('Before action')
            result_response = action(self.request)

            fallback_response = fallback.default_response()
            quick_replies = fallback_response['template']['quickReplies']
            result_response['template'].update({'quickReplies': quick_replies})
            return result_response
        except KeyError:
            return 'Sorry I cant :('
