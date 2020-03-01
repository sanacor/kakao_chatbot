from chatbot.cashier_chatbot.google_spreadsheet import GoogleSpreadSheet
from chatbot.cashier_chatbot.intent_type.fallback import Fallback
gss = GoogleSpreadSheet()
fallback = Fallback()

intent_to_action = {
    '신규 PS4 게임 리스트': gss.get_items,
    '중고 PS4 게임 리스트': gss.get_items,
    '가격 문의': gss.get_items,
    '폴백 블록': fallback.default_response
}


class Intent:
    pass


class Matcher:

    def __init__(self, intent):
        self.intent = intent

    def execute(self):
        try:
            if self.intent not in intent_to_action:
                return
            action = intent_to_action[self.intent]
            print('Before action')
            return action()
        except KeyError:
            return 'Sorry I cant :('
