import math

''' 無條件進位 dig :小數點後第幾位
'''
def roundUp(num, dig):
    digNum = 1
    for i in range(dig):
        digNum *= 10

    return(math.ceil(num*digNum)/float(digNum))

def is_float(numStr):
    ''' 字符串是否是浮点数(整数算小数)
    '''
    flag = False
    numStr = str(numStr).strip().lstrip('-').lstrip('+')    # 去除正数(+)、负数(-)符号
    try:
        numFloat = float(numStr)
        flag = True
    except Exception as ex:
        print("is_float() - error: " + str(ex))
    return flag

def calculateCompoundInterest(rate, principal, year, numPerYear):
    ans = principal
    comPerTime = 1+rate/numPerYear/100
    for i in range(year*numPerYear):
        ans *= comPerTime
    return(roundUp(ans, 2))

while True:
    notrepeat = 1
    principal_input = input('What is the principal amount? ')
    if principal_input.isdigit():
        principal = int(principal_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break
while True:
    notrepeat = 1
    rate_input = input('What is the rate? ')
    if is_float(rate_input):
        rate = float(rate_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break
while True:
    notrepeat = 1
    year_input = input('What is the number of years? ')
    if year_input.isdigit():
        year = int(year_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break
while True:
    notrepeat = 1
    numberPerYear_input = input('What is the number of times the interest is compounded per year? ')
    if numberPerYear_input.isdigit():
        numberPerYear = int(numberPerYear_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break





print('$'+principal_input+' invested at '+rate_input+'%'+' for '+year_input+' years compounded '+numberPerYear_input+' times per year is $'+str(calculateCompoundInterest(rate, principal, year, numberPerYear))+'.')