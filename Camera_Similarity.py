import requests
import json


with open(r'/home/jayas/PycharmProjects/RevMeUp/ProductCreationBatch/Flipkart/Flipkart_electronics/Camera.json','r') as flip_file:
    prod_flip = json.load(flip_file)
with open(r'/home/jayas/PycharmProjects/RevMeUp/ProductCreationBatch/Croma/Croma_electronics/Camera.json','r') as croma_file:
    prod_croma = json.load(croma_file)

for item in prod_flip:
    a = item['description']
    b = dict(a)
    mn_flip = b.get('Model Number')
    fl_brand = item['brand']
    for item2 in prod_croma:
        c = item2['description']
        d = dict(c)
        mn_croma = d.get('Model Number')
        cr_brand = item2['brand']
        if mn_flip == mn_croma and fl_brand == cr_brand:
            print(item['product_name'])
            print("Flipkart Price:",item['stores']['storePrice'])
            print("Croma Price:", item2['stores']['storePrice'])
