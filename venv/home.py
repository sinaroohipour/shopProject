from subprocess import call


welcome = '\nWelcome to shop\n'
reg = '1- register'
log = '2- login'
admin = '3- admin'
exit = '4- exit'

print(welcome)
print('{:^22}'.format(reg))
print('{:^18}'.format(log))
print('{:^18}'.format(admin))
print('{:^18}'.format(exit))

mentor = input('{:^22}'.format('witch one ? '))
if mentor == "1":
    call(["python", "register.py"])
elif mentor == "2":
    call(["python", "login.py"])
elif mentor == "3":
    call(["python", "admin.py"])
else:
    pass
