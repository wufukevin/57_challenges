import RegulationFunction as rf
import math
import random
import json
filePath = 'Q44_productData.json'

class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantiy = quantity

    def show(self):
        print(f'Name: {self.name}')
        print(f'Price: ${self.price}')
        print(f'Quantity on hand: {self.quantiy}')
        print('')

class ProductSearch:
    def __init__(self):
        self.productList = []
        with open(filePath) as f:
            self.data = json.load(f)
        for productData in self.data['products']:
            self.productList.append(product(productData['name'],productData['price'],productData['quantity']))

    def searchByName(self, name):
        for product in self.productList:
            if product.name == name:
                product.show()
                return(0)
        print('Sorry, that product was not found in our inventory.')
        addProduct = input('Do you want to add the product? ')
        if addProduct == 'y':
            self.addProduct(name, input('What is the product price? '), input('What is the product quantity? '))

    def addProduct(self, name, price, quantity):
        self.productList.append(product(name, price, quantity))

mainFunction = ProductSearch()
while True:
    mainFunction.searchByName(input('What is the product name? '))