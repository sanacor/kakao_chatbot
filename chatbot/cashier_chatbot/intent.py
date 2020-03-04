from chatbot.cashier_chatbot.google_spreadsheet import GoogleSpreadSheet
from chatbot.cashier_chatbot.fallback_block.fallback import Fallback
gss = GoogleSpreadSheet()
fallback = Fallback()


class Intent:
    NEW_PS4_GAME_LIST = '신규 PS4 게임 리스트'
    USED_PS4_GAME_LIST = '중고 PS4 게임 리스트'
    PRICE_OF_NEW_PS4_GAME = '신규 PS4 게임 가격 문의'
    PRICE_OF_USED_PS4_GAME = '중고 PS4 게임 가격 문의'
    FALL_BACK = '폴백 블록'


intent_to_action = {
    Intent.NEW_PS4_GAME_LIST: gss.get_items,
    Intent.USED_PS4_GAME_LIST: gss.get_items,
    Intent.PRICE_OF_NEW_PS4_GAME: gss.get_items,
    Intent.PRICE_OF_USED_PS4_GAME: gss.get_items,
    Intent.FALL_BACK: fallback.default_response
}

block_to_block_id = {
    Intent.NEW_PS4_GAME_LIST: '5e5f9e8c15e0d80001bd7f90',
    Intent.USED_PS4_GAME_LIST: '5e5f9e99c209c10001dcfd24',
    Intent.PRICE_OF_NEW_PS4_GAME: '5e5f9ea863420a0001e3691d',
    Intent.PRICE_OF_USED_PS4_GAME: '5e5f9eb13ad5250001d682b2'
}


class Matcher:

    def __init__(self, intent):
        self.intent = intent

    def execute(self):
        try:
            if self.intent not in intent_to_action:
                print('No matching intent'+self.intent)
                return
            action = intent_to_action[self.intent]
            print('Before action')
            return action()
        except KeyError:
            return 'Sorry I cant :('
