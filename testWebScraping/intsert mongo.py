import pymongo
import pprint
import json

# writing to mongodb
client = pymongo.MongoClient('mongodb+srv://green-eco-guy:accenture-team3@cluster0.ensebd0.mongodb.net/?retryWrites=true&w=majority')
db = client['grocer']

# This is the products Collection (table)
products_countdown = db.countdownproducts
products_american = db.americanproducts
products_indian = db.indianproducts
products_indian2 = db.indian2products
products_asia = db.asiaproducts
# products_pak = db.pakproducts


def insertCountdown():
    with open('countdownData.json', 'r', encoding='utf-8') as f:
        # clear old data
        products_countdown.delete_many({})

        # products_dict is the json file as a python list of dicts
        products_list = json.load(f)

        print(len(products_list))

        # This is a document (an item in the list)

        x = products_countdown.insert_many(products_list, ordered=False)

        # query = products.insert_many(products_list)

        #print(products_count.count())

def insertAmerican():
    with open('AmericanGrocorData.json', 'r', encoding='utf-8') as f:
        # clear old data
        products_american.delete_many({})

        # products_dict is the json file as a python list of dicts
        products_list = json.load(f)

        print(len(products_list))

        # This is a document (an item in the list)

        x = products_american.insert_many(products_list, ordered=False)

        # query = products.insert_many(products_list)

        #print(products_count.count())

def insertIndian():
    with open('indianGrocorData.json', 'r', encoding='utf-8') as f:
        # clear old data
        products_indian.delete_many({})

        # products_dict is the json file as a python list of dicts
        products_list = json.load(f)

        print(len(products_list))

        # This is a document (an item in the list)

        x = products_indian.insert_many(products_list, ordered=False)

        # query = products.insert_many(products_list)

        #print(products_count.count())

def insertIndian2():
    with open('Indain2GrocorData.json', 'r', encoding='utf-8') as f:
        # clear old data
        products_indian2.delete_many({})

        # products_dict is the json file as a python list of dicts
        products_list = json.load(f)

        print(len(products_list))

        # This is a document (an item in the list)

        x = products_indian2.insert_many(products_list, ordered=False)

        # query = products.insert_many(products_list)

        #print(products_count.count())

def insertAsia():
    with open('AsiaGrocorData.json', 'r', encoding='utf-8') as f:
        # clear old data
        products_asia.delete_many({})

        # products_dict is the json file as a python list of dicts
        products_list = json.load(f)

        print(len(products_list))

        # This is a document (an item in the list)

        x = products_asia.insert_many(products_list, ordered=False)

        # query = products.insert_many(products_list)

        #print(products_count.count())


if __name__ == "__main__":
    insertCountdown()
    insertAmerican()
    insertAsia()
    insertIndian()
    insertIndian2()

