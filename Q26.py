import RegulationFunction as rf
import math


class CreditCard:
    def __init__(self, balance, APR, monthlPayment):
        self.balance = int(balance)
        self.APR = int(APR)
        self.monthlPayment = int(monthlPayment)

    @classmethod
    def from_input(cls):
        return cls(
            rf.InputFunction('What is your balance? ',1,rf.isInteger),
            rf.InputFunction('What is the APR on the card (as a percent)? ',1,rf.isInteger),
            rf.InputFunction('What is the monthly payment you can make? ', 1, rf.isInteger)
        )

    def monthsToPayOff(self):
        dailyRate = float(self.APR/365)
        print(dailyRate)
        x = 1+dailyRate
        print(f'x = {x}')
        y = math.pow(x,30)
        print(f'y = {y}')
        z = float(self.balance/self.monthlPayment)
        print(f'z = {z}')
        a = math.log((1+z*(1-y))*(-1))
        print(f'a = {a}')
        b = math.log(x)*30
        print(f'b = {b}')

        print(a/b)

    def printAns(self):
        print(f'It will take you {self.monthsToPayOff()} months to pay off this card.')

user = CreditCard.from_input()
user.printAns()