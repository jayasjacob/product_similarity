import requests
import json


url = "https://apistaging.revmeup.in/api/v1/user/login"
response = requests.post(url, json={
    "userid": "ZKh5adE6Lvb2lQGrru9LEKWQUXq2",
    "password": "ZKh5adE6Lvb2lQGrru9LEKWQUXq2"
})
a = response.json()
tok = a['token']

header = {'Authorization': 'Bearer ' + tok, 'content-type': "application/json"}

with open(r'/home/jayas/PycharmProjects/RevMeUp/ProductCreationBatch/Flipkart/Flipkart_electronics/Mobile.json','r') as flip_file:
    prod_flip = json.load(flip_file)
with open(r'/home/jayas/PycharmProjects/RevMeUp/ProductCreationBatch/Croma/Croma_electronics/Mobile.json','r') as croma_file:
    prod_croma = json.load(croma_file)


l = requests.get(url2, headers=header)
l.status_code
prod_info = l.json()

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
            if item['product_name'] == prod_info['product_name']:
                payload_ = item['stores']['storePrice']

