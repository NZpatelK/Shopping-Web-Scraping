import requests
import re
import json
import random

# as per recommendation from @freylis, compile once only
products_output = []


def caluateSustainable():
    n = random.randint(0, 100)
    return n


page = 1
max_page = 5

while (page <= max_page):

    plist = requests.get('https://grabgrocery.co.nz/products.json?limit=1000&page='+str(page)).json()
    for product in plist['products']:

        try:
            newProduct = {}
            newProduct['businessName'] = 'Grab Grocery'
            newProduct['productName'] = product['title']
            newProduct['price'] = product['variants'][0]['price']
            newProduct['type'] = product['product_type']
            newProduct['Sustainable'] = caluateSustainable()
            newProduct['img'] = product['images'][0]['src']
            products_output.append(newProduct)

        except:
            print("no image")


    page += 1

print(products_output)

with open('../indianGrocorData.json', 'w', encoding='utf-8') as f:
    json.dump(products_output, f, ensure_ascii=False, indent=4)
