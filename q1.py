import sys

notrepeat = 1
while True:
    notrepeat = 1
    bill_input = input('What is the bill ? $')
    if bill_input.isdigit():
        bill = float(bill_input)
    else:
        print('Please enter a valid number for the bill amount.')
        notrepeat = 0
    if notrepeat:
        break

while True:
    notrepeat = 1
    tipRate_input = input('What is the tip percentage ? ')
    if tipRate_input.isdigit():
        tipRate = float(tipRate_input)
    else:
        print('Please enter a valid number for the tip rate.')
        notrepeat = 0
    if notrepeat:
        break
def tipFunc(bill, tiprate):
    ans = bill*tiprate/100
    return ans
tip = tipFunc(bill, tipRate)
# '%.2f': 控制小數位 , sep : 控制 print 結尾  
print('The tip is $', '%.2f'%tip, sep="")
print('The total is $', '%.2f'%(bill+tip), sep="")