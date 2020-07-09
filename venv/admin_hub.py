from subprocess import call
from product import Product


class AdminHub:

    txt_one = '1- add product'
    txt_two = '2- remove product'
    txt_three = '3- edit product'
    txt_four = '4- change info'
    txt_five = '5- exit'

    def __init__(self):
        pass

    def add_product(self, code, name, price, number):
        req = Product()
        req.add_product(name, price, number)


print('\nAdmin Side\n')
print('{:^22}'.format(AdminHub.txt_one))
print('{:^26}'.format(AdminHub.txt_two))
print('{:^24}'.format(AdminHub.txt_three))
print('{:^22}'.format(AdminHub.txt_four))
print('{:^16}'.format(AdminHub.txt_five))
mentor = input('{:^20}'.format('witch one ? '))
request = AdminHub()
if mentor == "1":

    request.add_product('joorab', 5000, 20)
elif mentor == "2":
    pass
elif mentor == "3":
    pass
elif mentor == "4":
    pass
else:
    call(["python", "home.py"])
