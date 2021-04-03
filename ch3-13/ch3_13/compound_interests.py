class CompoundInterestCalculator(object):
    def calculate_compound_interest(self, principal, rate_of_interest, years, times):
        rate_of_interest_in_percent = rate_of_interest / 100
        result = principal * pow((1 + rate_of_interest_in_percent / times), years * times)
        print(
            f'${principal:.2f} invested at {rate_of_interest}% for {years} years compounded {times} times per year is ${result:.2f}.')


def ask_question():
    principal = float(input('What is the principal amount? '))
    rate_of_interest = float(input('What is the rate? '))
    years = int(input('What is the number of years? '))
    times = int(input('What is the number of times the interest is compounded per year? '))
    return principal, rate_of_interest, years, times
