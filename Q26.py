import RegulationFunction as rf
import math


class CreditCard:
    def __init__(self, balance, APR, monthlPayment):
        self.balance = int(balance)
        self.APR = float(int(APR)/100)
        self.monthlPayment = int(monthlPayment)

    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('What is your balance? ',1,rf.isInteger),
            rf.InputFunction('What is the APR on the card (as a percent)? ',1,rf.isInteger),
            rf.InputFunction('What is the monthly payment you can make? ', 1, rf.isInteger)
        )

    def monthsToPayOff(self):
        dailyRate = float(self.APR/365)
        x = 1+dailyRate
        y = math.pow(x,30)
        z = float(self.balance/self.monthlPayment)
        a = math.log(1+z*(1-y))
        b = math.log(x)*30
        return(math.ceil(-1*a/b))

    def printAns(self):
        print(f'It will take you {self.monthsToPayOff()} months to pay off this card.')

user = CreditCard.fromInput()
user.printAns()