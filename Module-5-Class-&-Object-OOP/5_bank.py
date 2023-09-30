class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"You can not withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"You can not withdraw more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"Here is your money {amount}")
            # both this line do the same
            print(f"Your current balance is {self.balance}")
            print(f"Your current balance is {self.get_balance()}")


brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(15000)
brac.withdraw(10000)

dbbl = Bank(5000)
dbbl.deposite(2000)
print(dbbl.get_balance())
