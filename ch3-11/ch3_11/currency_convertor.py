import requests

from ch3_11.ask_question import AskQuestion


class CurrencyConvertor(object):
    def __init__(self):
        self.exchange_rate = None
        self.amount = None
        self.currency_to = None
        self.currency_from = None
        self.base_url = 'http://api.exchangeratesapi.io/v1'
        self.api_params = {
            'access_key': 'c35984cf64f336618adfcbce1618b271'
        }

    def load_supported_currencies(self):
        url = self.create_url('symbols')
        self.supported_currencies = requests.get(url, params=self.api_params).json()['symbols']

    def create_url(self, function):
        url = f'{self.base_url}/{function}'
        return url

    def convert(self):
        self.api_params.update({
            'from': self.currency_from,
            'to': self.currency_to,
            'amount': self.amount
        })
        url = self.create_url('convert')
        result_json = requests.get(url, params=self.api_params).json()
        self.exchange_rate = result_json['info']['rate']
        self.result = result_json['result']
        print(
            f'{self.amount:.2f} {self.currency_from} dollars at an exchange rate of {self.exchange_rate:.2f} is {self.result:.2f} {self.currency_to} dollars')


if __name__ == '__main__':
    convertor = CurrencyConvertor()
    question = AskQuestion(convertor)
    question.ask()
    print(f'')
    print(convertor.convert())
