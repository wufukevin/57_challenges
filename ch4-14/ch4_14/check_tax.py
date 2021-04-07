TAX_IN_WISCONSIN = 0.55


class CheckTax(object):
    def check(self, amount, state):
        amount_value = float(amount)
        total = amount_value
        if state.upper() == 'WI' or state.upper() == 'WISCONSIN':
            print(f'The subtotal is ${amount_value :.2f}.')
            print(f'The tax is ${TAX_IN_WISCONSIN:.2f}.')
            total += TAX_IN_WISCONSIN

        print(f'The total is ${total:.2f}.')
