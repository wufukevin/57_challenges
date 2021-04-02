class AskQuestion(object):
    def __init__(self, currency_convertor):
        self.convertor = currency_convertor

    def ask(self):
        print(self.convertor.supported_currencies)
        self.convertor.currency_from = input('What currency would you like to convert from? ')
        self.convertor.currency_to = input('What currency would you like to convert to? ')
        self.convertor.amount = float(input('How much would you like to convert? '))
