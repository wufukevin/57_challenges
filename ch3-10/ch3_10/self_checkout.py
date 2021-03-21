def ask_for_continue():
    more_price_and_quantity = input('More price and quantity? (y/N)')
    return more_price_and_quantity.lower() == 'y'


class SelfCheckOut(object):
    def __init__(self):
        self.items = []

    def ask_for_price_and_quantity(self):
        item_number = self.items_count() + 1
        price = int(input(f'Enter the price of item {item_number}: '))
        quantity = int(input(f'Enter the quantity of item {item_number}: '))
        self.items.append({'price': price, 'quantity': quantity})

    def items_count(self):
        return len(self.items)
