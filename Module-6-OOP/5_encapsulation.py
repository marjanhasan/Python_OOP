# encapsulation --> hide details
# access modifier --> public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name
        self._branch = "Banani 11"  # _ dile protected variable
        self.__balance = initial_deposite  # __ dile private hye jay

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f"Fokira taka nai"


rafsun = Bank("Chota Vai", 10000)
print(rafsun.holder_name)
# print(rafsun.__balance)  # AttributeError: 'Bank' object has no attribute '__balance'
rafsun.deposite(40000)
print(rafsun.get_balance())  # 50000
rafsun.holder_name = "Boro vai"  # property acessed and changed
print(rafsun.holder_name)
print(rafsun._branch)
# print(dir(rafsun)) to get the trick
print(rafsun._Bank__balance)  # jor kre private jinis dekha
