def is_plural(number):
    return 's' if number > 1 else ''


class SimpleInterestCalculator(object):
    def calculate_simple_interest(self, principal, rate_of_interest, years):
        self.rate_of_interest = rate_of_interest
        rate_of_interest_in_percent = rate_of_interest / 100
        return [f'{(principal * (1 + rate_of_interest_in_percent * year)):.2f}' for year in range(1, years + 1)]

    def reports(self, interests):
        year_start = 1
        for year, interest_of_the_year in enumerate(interests, year_start):
            print(
                f'After {year} year{is_plural(year)} at {self.rate_of_interest} %, the investment will be worth ${interest_of_the_year}.')


def ask_question():
    principal = float(input('Enter the principal: '))
    rate_of_interest = float(input('Enter the rate of interest: '))
    years = int(input('Enter the number of years: '))
    return principal, rate_of_interest, years
