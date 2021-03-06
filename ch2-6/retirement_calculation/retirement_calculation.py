from datetime import date


def current_year():
    return date.today().year


class RetirementCalculator(object):

    def ask_current_age(self):
        self.current_age = input("What is your current age? ")

    def ask_retire_age(self):
        self.retire_age = input("What is your current age? ")

    def show_years_left(self):
        print(f"You have {self.years_left()} years left until you can retire.")

    def show_retire_year(self):
        print(f"It's {current_year()}, so you can retire in {self.retire_year()}.")

    def retire_year(self):
        return current_year() + self.years_left()

    def years_left(self):
        return int(self.retire_age) - int(self.current_age)
