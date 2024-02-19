class Bank():
    def __init__(self, account_number, account_holder, balance):
        self.account_number = str(account_number)
        self.account_holder = str(account_holder)
        self.balance = float(balance)
        with open("bank_db.txt", "a") as bank_db:
            bank_db.write(f"{self.account_number},{self.account_holder},{self.balance}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print(f"your amount is {amount} it's need to be positive! ")

    def withdraw(self, amount):
        if self.balance >= amount:
            if amount > 0:
                self.balance -= amount
            else:
                print(f"your amount is {amount} it's need to be a positive amount! ")
        else:
            print(f"sorry, you dont have enough money!")

    def get_balance(self):
        print(self.balance)

   # def transfer(self, target_account, amount):




mmm = Bank(1234, "mendy", 100)
mmm.withdraw(101)
mmm.get_balance()