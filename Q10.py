import RegulationFunction as rf

price = []
quantity = []
itemNumber = 0
taxRate = 5.5
noMoreItem = False

def IsdigitOrNO(Parameter):
    global itemNumber
    global noMoreItem
    if Parameter.isdigit():
        return True
    elif Parameter=='NO':
        noMoreItem = True
        return True
    else:
        print('Please enter a valid number.')
        return False


print()
print('If there is no item to enter. Please enter NO.')
print()


while True:
    
    price.append(rf.InputFunction(f'Enter the price of item {itemNumber+1}: ', itemNumber+1, IsdigitOrNO))

    if noMoreItem:
        break
    
    quantity.append(rf.InputFunction(f'Enter the quantity of item {itemNumber+1}: ', itemNumber+1, IsdigitOrNO))
    itemNumber += 1
    

subtotal = 0
for i in range(itemNumber):
    subtotal += float(price[i])*float(quantity[i])

subtotal = round(subtotal, 2)
tax = round(subtotal*taxRate/100, 2)
total = subtotal+tax

print(f'Subtotal: ${subtotal}')
print(f'Tax: ${tax}')
print(f'Total: ${total}')