class Atm:
    #action/behaviour
    #variable/data/property/attribute

    # ? data -> pin, balance
    #* action -> create pin, change pin, deposit, withdraw,check balance

    # ! constructor or INITIALIZER
    def __init__(self) -> None:
        self.balance = 0
        self.pin = ''


    def create_pin(self):
        pin = input("Enter a 4 digit pin : ")
        confirm_pin = input("Confirm pin : ")
        if pin == confirm_pin:
            self.pin = pin
            print("Pin Set Successfully")
        
        else :
            print("Did not match")
            self.create_pin()

    def change_pin(self):
        old_pin = input("Enter old pin : ")
        if old_pin==self.pin:
            self.create_pin()
        else:
            print("Incorrect Pin!")

    def deposit(self):
        pin = input("Enter pin : ")
        if pin == self.pin:
            deposit_amount = int(input("Enter amount to depsit : "))
            self.balance = self.balance + deposit_amount
        else :
            print("Incorrect Pin!")


    def withdraw(self):
        pin = input("Enter pin : ")
        if pin == self.pin:
            withdrawl_amount = int(input("Enter withdrawl amount : "))
            if withdrawl_amount<=self.balance :
                self.balance = self.balance - withdrawl_amount
            else:
                print("Bheek Chahiye??")
        else:
            print("Incorrect Pin!")

    def check_balance(self):
        pin = input("Enter pin : ")
        if pin == self.pin:
            print(self.balance)
        else:
            print("Incorrect Pin!")

