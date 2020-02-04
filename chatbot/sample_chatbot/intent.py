from chatbot.sample_chatbot.google_spreadsheet import GoogleSpreadSheet

gss = GoogleSpreadSheet()

intent_to_action = {
    '상품 리스트': gss.get_items,
    '가격 문의': gss.get_items
}


class Matcher:

    def __init__(self, intent):
        self.intent = intent

    def execute(self):
        try:
            action = intent_to_action[self.intent]
            print('Before action')
            return action()
        except KeyError:
            return 'Sorry I cant :('
