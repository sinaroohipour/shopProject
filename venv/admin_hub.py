import os.path
import json
import random
import string
from subprocess import call

class AdminHub:
    txt_one = '1- add'
    txt_two = '2- delete'
    txt_three = '3- edit'
    txt_four = '4- get list of products'
    txt_five = '5- get list of orders'
    txt_six = '6- change info'
    json_file_path = './DataBase/products.json'

    def __init__(self):
        pass

    def add_product(self):
        title = input('title :')
        price = input('price :')
        number = int(input('number :'))
        letters = string.ascii_letters
        code = ''.join(random.choice(letters) for i in range(10))
        obj = {
            "title": title,
            "code": code,
            "price": price,
            "number": number
        }
        with open(AdminHub.json_file_path) as json_file:
            info = json.load(json_file)
            products = info['products']
            products.append(obj)
        with open(AdminHub.json_file_path, 'w') as f:
            json.dump(info, f, indent=2)

    def delete_product(self):
        self.get_products()
        deleter = int(input('{:^20}'.format('witch one?')))
        with open(AdminHub.json_file_path) as json_file:
            info = json.load(json_file)
            products = info['products']
            idx = 1
            for item in products:
                if deleter == idx:
                    del products[idx - 1]
                    print('{:^16}'.format('Done!!'))
                idx = idx + 1
        with open(AdminHub.json_file_path, 'w') as json_file:
            info = json.dump(info, json_file, indent=2)

    def edit_product(self):
        self.get_products()
        editor = int(input('{:^20}'.format('witch one?')))
        with open(AdminHub.json_file_path) as json_file:
            info = json.load(json_file)
            products = info['products']
            idx = 1
            for item in products:
                if editor == idx:
                    products[idx - 1]['title'] = input('new title :' + 'last value' + '(' + products[idx - 1]['title'] + ') : ')
                    products[idx - 1]['price'] = input('new price :' + 'last value' + '(' + products[idx - 1]['price'] + ') : ')
                    products[idx - 1]['number'] = input('new number :' + 'last value' + '(' + str(products[idx - 1]['number']) + ') : ')
                    print('{:^16}'.format('Done!!'))
                idx = idx + 1
        with open(AdminHub.json_file_path, 'w') as json_file:
            info = json.dump(info, json_file, indent=2)

    def get_products(self):
        with open(AdminHub.json_file_path) as json_file:
            info = json.load(json_file)
            products = info['products']
            idx = 1
            print('\n')
            for i in products:
                index = str(idx) + '- '
                print(index +
                      'Name :' + '{:^16}'.format(i['title']) +
                      'Code :' + '{:^14}'.format(i['code']) +
                      'Price :' + '{:^8}'.format(i['price']) +
                      'Number :' + '{:^4}'.format(str(i['number'])))
                idx = idx + 1
    def get_orders(self):
        pass
    def change_info(self):
        pass



if os.path.exists(AdminHub.json_file_path):
    pass
else:
    data = {'products': []}
    json_object = json.dumps(data, indent=2)
    with open(AdminHub.json_file_path, 'a+') as outfile:
        json.dump(data, outfile)

print('\nAdmin Hub\n')
print('{:^16}'.format(AdminHub.txt_one))
print('{:^20}'.format(AdminHub.txt_two))
print('{:^18}'.format(AdminHub.txt_three))
print('{:^34}'.format(AdminHub.txt_four))
print('{:^32}'.format(AdminHub.txt_five))
print('{:^24}'.format(AdminHub.txt_six))
mentor = input('{:^20}'.format('witch one?'))
request = AdminHub()
if mentor == "1":
    request.add_product()
    call(["python", "admin_hub.py"])
elif mentor == "2":
    request.delete_product()
    call(["python", "admin_hub.py"])
elif mentor == "3":
    request.edit_product()
    call(["python", "admin_hub.py"])
elif mentor == "4":
    request.get_products()
    call(["python", "admin_hub.py"])
elif mentor == "5":
    request.get_orders()
    call(["python", "admin_hub.py"])
elif mentor == "6":
    request.change_info()
    call(["python", "admin_hub.py"])
else:
    pass

