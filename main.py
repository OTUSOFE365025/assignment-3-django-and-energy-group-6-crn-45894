from decimal import Decimal

import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from db.models import *

def loadProducts(filename='sampleProducts.txt'):
    
    #Read UPC, name, and price from sampleproducts.txt and
    #saves them to the database
    
    #Checks if file exists
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    #Reads and stores product UPC, name, and price
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            sections = line.strip().split()
            if len(sections) >= 3:
                upc = sections[0]
                name = sections[1]
                price_str = sections[-1].replace('$', '')
                try:
                    price = Decimal(price_str)
                except:
                    print(f"Skipping invalid price on line: {line.strip()}")
                    continue
                
                #Insert/update product using Django ORM
                Product.objects.update_or_create(
                    upc=upc,
                    defaults={'name': name, 'price': price}
                )
                count += 1

    print(f"Loaded {count} products into the database.")

def showProducts():
    
    products = Product.objects.all()
    if not products:
        print("There are no products in the database.")
        return

    print("\nProducts in the database:")
    for i in products:
        print(f"UPC: {i.upc:10} | Name: {i.name:15} | Price: ${i.price}")
    print("")

loadProducts('sampleProducts.txt')
showProducts()