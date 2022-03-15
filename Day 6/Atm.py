class Atm:
    #action/behaviour
    #variable/data/property/attribute

    # ? data -> pin, balance
    #* action -> create pin, change pin, deposit, withdraw,check balance

    # ! constructor or INITIALIZER
    def __init__(self) -> None:
        self.__balance = 0
        self.__pin = ''

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if(type(new_balance)==int):
            self.__balance = new_balance
        else:
            print("baap se chalu panti nai!")

    def create_pin(self):
        pin = input("Enter a 4 digit pin : ")
        confirm_pin = input("Confirm pin : ")
        if pin == confirm_pin:
            self.__pin = pin
            print("Pin Set Successfully")
        
        else :
            print("Did not match")
            self.create_pin()

    def change_pin(self):
        old_pin = input("Enter old pin : ")
        if old_pin==self.__pin:
            self.create_pin()
        else:
            print("Incorrect Pin!")

    def deposit(self):
        pin = input("Enter pin : ")
        if pin == self.__pin:
            deposit_amount = int(input("Enter amount to depsit : "))
            self.__balance = self.__balance + deposit_amount
        else :
            print("Incorrect Pin!")


    def withdraw(self):
        pin = input("Enter pin : ")
        if pin == self.__pin:
            withdrawl_amount = int(input("Enter withdrawl amount : "))
            if withdrawl_amount<=self.__balance :
                self.__balance = self.__balance - withdrawl_amount
            else:
                print("Bheek Chahiye??")
        else:
            print("Incorrect Pin!")

    def check_balance(self):
        pin = input("Enter pin : ")
        if pin == self.__pin:
            print(self.__balance)
        else:
            print("Incorrect Pin!")

