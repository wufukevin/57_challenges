def ask_for_continue():
    more_price_and_quantity = input('More price and quantity? (y/N)')
    return more_price_and_quantity.lower() == 'y'


class SelfCheckOut(object):
    def __init__(self):
        self.items = []

    def ask_for_price_and_quantity(self):
        price = int(input('Enter the price of item 1: '))
        quantity = int(input('Enter the quantity of item 1: '))
        self.items.append({'price': price, 'quantity': quantity})

    def items_count(self):
        return len(self.items)