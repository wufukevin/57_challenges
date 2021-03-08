import RegulationFunction as rf

priceAndQuantity = []
taxRate = 5.5

def IsdigitOrNO(Parameter):
    if Parameter.isdigit() or Parameter=='NO':
        return True
    else:
        print('Please enter a valid number.')
        return False


print()
print('If there is no item to enter. Please enter NO.')
print()


while True:
    itemNumber = len(priceAndQuantity)+1
    priceInput = rf.InputFunction(f'Enter the price of item {itemNumber}: ', itemNumber, IsdigitOrNO)
    if priceInput=='NO':
        break
    quantityInput = rf.InputFunction(f'Enter the quantity of item {itemNumber}: ', itemNumber, IsdigitOrNO)
    priceAndQuantity.append((priceInput, quantityInput))
    

subtotal = 0
for price, quantity in priceAndQuantity:
    subtotal += float(price)*float(quantity)
subtotal = round(subtotal, 2)
tax = round(subtotal*taxRate/100, 2)
total = subtotal+tax

print(f'Subtotal: ${subtotal}')
print(f'Tax: ${tax}')
print(f'Total: ${total}')