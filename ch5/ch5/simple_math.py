class SimpleMath(object):
    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.second_input = None
        self.first_input = None

    def ask_two_numbers(self):
        self.first_input = input("What is the first number? ")
        self.first_number = int(self.first_input)
        self.second_input = input("What is the second number? ")
        self.second_number = int(self.second_input)

    def calculate(self):
        add_statement = f'{self.first_number} + {self.second_number} = {self.first_number + self.second_number}'
        subtract_statement = f'{self.first_number} - {self.second_number} = {self.first_number - self.second_number}'
        multiply_statement = f'{self.first_number} * {self.second_number} = {self.first_number * self.second_number}'
        divide_statement = f'{self.first_number} / {self.second_number} = {int(self.first_number / self.second_number)}'
        print(f'{add_statement}\n{subtract_statement}\n{multiply_statement}\n{divide_statement}')