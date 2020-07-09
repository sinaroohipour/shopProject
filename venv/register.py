import json
import os.path
from subprocess import call
import hashlib

class Register:

    txt_one = 'username : '
    txt_two = 'password : '
    json_file_path = './DataBase/users.json'

    def __init__(self, username, password):
        self.username = username
        self.password = password
    def check_username(self, username):
        with open(Register.json_file_path) as json_file:
            data = json.load(json_file)
            for u in data['users']:
                if username == u['username']:
                    return 0
            return 1

    def hashing(self,password):
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()
        return password

    def register_handler(self, username, password):
        obj = {
            "username": username,
            "password": password
        }
        if os.path.exists(Register.json_file_path):
            with open(Register.json_file_path) as json_file:
                data = json.load(json_file)
                users = data['users']
                users.append(obj)
            with open(Register.json_file_path, 'w') as file:
                json.dump(data, file, indent=2)
        else:
            data = {'users': []}
            data['users'].append(obj)
            json_object = json.dumps(data, indent=2)
            with open(Register.json_file_path, 'a+') as outfile:
                json.dump(data, outfile)


print('\nRegister page :\n')
username = input('{:^18}'.format(Register.txt_one))
password = input('{:^18}'.format(Register.txt_two))
request = Register(username, password)
password = request.hashing(password)
if os.path.exists(request.json_file_path):
    if request.check_username(username):
        request.register_handler(username, password)
    else:
        print('\nError : username already exist!!')
        call(["python", "home.py"])
else:
    request.register_handler(username, password)
