PERCENT = 1 / 100
TAX_RATE = 5.5 * PERCENT


def ask_for_continue():
    more_price_and_quantity = input('More price and quantity? (y/N)')
    return more_price_and_quantity.lower() == 'y'


class SelfCheckOut(object):
    def __init__(self):
        self.subtotal = 0
        self.items = []

    def ask_for_price_and_quantity(self):
        item_number = self.items_count() + 1
        price = int(input(f'Enter the price of item {item_number}: '))
        quantity = int(input(f'Enter the quantity of item {item_number}: '))
        self.items.append((price, quantity))

    def items_count(self):
        return len(self.items)

    def checkout(self):
        for price, quantity in self.items:
            self.subtotal += price * quantity
        self.tax = self.subtotal * TAX_RATE
        self.total = self.subtotal + self.tax

    def report(self):
        order = 1
        for price, quantity in self.items:
            print(f'Total of {quantity} Item {order} is {price * quantity}')
            order += 1
        print(f'Subtotal: ${self.subtotal:.2f}')
        print(f'Tax: ${self.tax:.2f}')
        print(f'Total: ${self.total:.2f}')


if __name__ == '__main__':
    checker = SelfCheckOut()
    continue_input = True
    while continue_input:
        checker.ask_for_price_and_quantity()
        continue_input = ask_for_continue()
    checker.checkout()
    checker.report()
