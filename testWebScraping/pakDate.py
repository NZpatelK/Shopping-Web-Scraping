from bs4 import BeautifulSoup
import requests
import json
import math

# departments = ['pantry', 'fresh-foods-and-bakery', 'baby-toddler-and-kids', 'beer-cider-and-wine',
#                'chilled-frozen-and-desserts', 'drinks', 'personal-care', 'baby-toddler-and-kids',
#                'kitchen-dining-and-household']

products_output = []

# for department in departments:

page = 1

page_num = 50

while page <= page_num:
    # html_doc = requests.get('https://grabgrocery.co.nz/collections/groceries?page='.format(department, page)).content
    html_doc = requests.get('https://grabgrocery.co.nz/collections/groceries?page='+str(page))

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    # if page == 1:
    #     page_num_container = soup.find("div", {
    #         "class": "respimgsize tt-product product-parent options-js product-nohover"})
    #     print(page_num_container)
    #     # split = page_num_container.split(" ")
    #     # products_num = split[5]
    #     # page_num = math.ceil(int(products_num) / 20)

    containers = soup.find_all("div", {'class': 'respimgsize tt-product product-parent options-js product-nohover'})

    #print(containers)

    for container in containers:
        product = {}

        # footer = container.find("div", {"class": "respimgsize tt-product product-parent options-js product-nohover"})
        #
        # data = footer.get("data-options")
        #
        # data = json.loads(data)

        name = container.find("h2", {"class": "tt-title prod-thumb-title-color"})
        product["productName"] = name.find("a").getText()

        price = container.find("div", {"class" : "tt-price"})
        product['price'] = price.find("span").getText()

        product['description'] = container.find("div", {"class": "description"}).getText()

        product['img'] = container.find_all("span", {"class": "tt-img"})
        print(container)

        products_output.append(product)
        #print(product)

    page = page + 1
