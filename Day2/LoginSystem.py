users = {
    'vinig2411@gmail.com' : '1234',
    'smartytirtho@yahoo.in' : '3456'
}

email = input("Enter Email : ")
password = input("Enter Password : ")

if email == 'vinig2411@gmail.com' and password == '1234':
    print("Welcome")
elif email == 'vinig2411@gmail.com' and password!='1234':
    print("Galat Password")
    password = input("Akhri Mauka hai tere paas : ")
    if(password=='1234'):
        print("Bach gya beta")
    else :
        print("Nikal Ab")
else:
    print("Kat Le")


# present = False
# if users.keys()==email & users.items()==password:
#     print("Welcome")
# else :
#     print("Invalid user")
