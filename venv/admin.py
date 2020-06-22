import json
import os.path
from subprocess import call
import hashlib

class Admin:
    txt_one = 'username : '
    txt_two = 'password : '
    json_file_path = './DataBase/admin.json'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_info(self, username, password):
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()
        with open(Admin.json_file_path) as json_file:
            data = json.load(json_file)
            for u in data['admins']:
                if username == u['username']:
                    if password == u['password']:
                        return 1
                    else:
                        return 0
            return 0


if os.path.exists(Admin.json_file_path):
    pass
else:
    hash_object = hashlib.md5('admin'.encode())
    password = hash_object.hexdigest()
    data = {}
    data['admins'] = []
    data['admins'].append({
        "username": 'admin',
        "password": password
    })
    json_object = json.dumps(data, indent=2)
    with open(Admin.json_file_path, 'a+') as outfile:
        json.dump(data, outfile)

print('\nAdmin Side\n')
username = input('{:^18}'.format(Admin.txt_one))
password = input('{:^18}'.format(Admin.txt_two))
request = Admin(username, password)
if request.check_info(username, password):
    print('yeees')
else:
    print('\nError: Something wrong!!')
    call(["python", "home.py"])