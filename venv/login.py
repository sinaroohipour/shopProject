import json
import os.path
from subprocess import call
import hashlib

class Login:
    txt_one = 'username : '
    txt_two = 'password : '
    json_file_path = './DataBase/users.json'
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_info(self,username, password):
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()
        if os.path.exists(Login.json_file_path):
            with open(Login.json_file_path) as json_file:
                data = json.load(json_file)
                for u in data['users']:
                    if username == u['username']:
                        if password == u['password']:
                            return 1
                        else:
                            return 0
                return 0
        else:
            return 0
print('\nLogin page :\n')
username = input('{:^18}'.format(Login.txt_one))
password = input('{:^18}'.format(Login.txt_two))
request = Login(username, password)
if request.check_info(username, password):
    print('\nLet\'s go')
else:
    print('\nError: Something wrong!!')
    call(["python", "home.py"])
