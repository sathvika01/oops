class Account:
    def __init__(self,balance,account_number):
        #private attributes
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self,dep):
        #dep = int(input("Enter deposit amount?"))
        self.__balance = self.__balance+dep
        return f"Your total available balance is {self.__balance} for {self.__account_number}"


    def withdraw(self):
        draw = int(input("Enter amount to withdraw"))
        if draw <= self.__balance:
            self.__balance = self.__balance - draw
            return f"Your {self.__account_number} remaining balance is {self.__balance}"
        else:
            print("Insufficient balance")

transaction1 = Account(200,12345)
print(transaction1.deposit(800))
transaction2 = Account(1000,12345)
print(transaction2.withdraw())

