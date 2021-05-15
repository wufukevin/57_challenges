import math
import RegulationFunction as rf

def calculateCompoundInterest(rate, principal, year, numPerYear):
    ans = principal
    comPerTime = 100+rate/numPerYear
    for i in range(year*numPerYear):
        ans = ans*comPerTime/100
    return(rf.roundUp(ans, 2))

input_principal = rf.InputFunction('What is the principal amount? ', 1, rf.isDigit)
input_rate = rf.InputFunction('What is the rate? ', 2, rf.isFloat)
input_year = rf.InputFunction('What is the number of years? ', 3, rf.isDigit)
input_numberPerYear = rf.InputFunction('What is the number of times the interest is compounded per year? ', 4, rf.isDigit)

principal = int(input_principal)
rate = float(input_rate)
year = int(input_year)
numberPerYear = int(input_numberPerYear)
compoundedInterest = calculateCompoundInterest(rate, principal, year, numberPerYear)

print(f'${principal} invested at {rate}% for {year} years compounded {numberPerYear} times per year is ${compoundedInterest}.')