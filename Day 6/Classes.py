#methods or variable inside a class cannot access other variables or methods, only the objects of the class can do that

#* so we use self, which represents the object that is currently calling the method

import Atm
cust1 = Atm.Atm()

# cust1.create_pin()

# cust1.check_balance()
# cust1.deposit()
# cust1.check_balance()


import Fraction as Fr

x = Fr.Fraction(3,4)
print(x)