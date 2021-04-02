class AskQuestion(object):
    def __init__(self, currency_convertor):
        self.convertor = currency_convertor

    def ask(self):
        self.convertor.load_supported_currencies()
        print(self.convertor.supported_currencies)
        self.convertor.currency_from = input('What currency would you like to convert from? ')
        if self.convertor.supported_currencies.get(self.convertor.currency_from) is None:
            raise Exception()
        self.convertor.currency_to = input('What currency would you like to convert to? ')
        if self.convertor.supported_currencies.get(self.convertor.currency_to) is None:
            raise Exception()
        self.convertor.amount = float(input('How much would you like to convert? '))
        self.convertor.convert()
