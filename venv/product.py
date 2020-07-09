import json
import os.path
import os
import uuid


class Product:
    json_file_path = './DataBase/products.json'

    def __init__(self):
        pass

    def add_product(self, name, price, number):
        code = uuid.uuid4().hex[:8]
        obj = {
            "code": code,
            "name": name,
            "price": price,
            "number": number
        }
        if os.path.exists(Product.json_file_path):
            if os.stat(Product.json_file_path).st_size == 0:
                data = {'products': []}
                data['products'].append(obj)
                json_object = json.dumps(data, indent=4)
                with open(Product.json_file_path, 'a+') as outfile:
                    json.dump(data, outfile)
            else:
                with open(Product.json_file_path) as json_file:
                    data = json.load(json_file)
                    users = data['products']
                    users.append(obj)
                with open(Product.json_file_path, 'w') as f:
                    json.dump(data, f, indent=4)
        else:
            data = {'products': []}
            data['products'].append(obj)
            json_object = json.dumps(data, indent=4)
            with open(Product.json_file_path, 'a+') as outfile:
                json.dump(data, outfile)
