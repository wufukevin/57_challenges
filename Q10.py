print()
print('If there is no item to enter. Please enter NO.')
print()

price = []
quantity = []
itemNumber = 0
taxRate = 5.5

while True:
    noMoreItem = 0
    while True:
        notrepeat = 1
        price_input = input('Enter the price of item '+str(itemNumber+1)+': ')
        if price_input.isdigit():
            price.append(float(price_input))
            itemNumber += 1
        elif price_input=='NO':
            noMoreItem = 1
        else:
            print('Please enter a valid number.')
            notrepeat = 0
        if notrepeat:
            break

    if noMoreItem:
        break

    while True:
        notrepeat = 1
        quantity_input = input('Enter the quantity of item '+str(itemNumber)+': ')
        if quantity_input.isdigit():
            quantity_flaot = float(quantity_input)
            if quantity_flaot%1 == 0:
                quantity.append(int(quantity_flaot))
            else:
                print('Please enter an integer.')
                notrepeat = 0
        else:
            print('Please enter a valid number.')
            notrepeat = 0
        if notrepeat:
            break


    

subtotal = 0
for i in range(itemNumber):
    subtotal += price[i]*quantity[i]

subtotal = round(subtotal, 2)

tax = round(subtotal*taxRate/100, 2)

total = subtotal+tax

print('Subtotal: $'+str(subtotal))
print('Tax: $'+str(tax))
print('Total: $'+str(total))