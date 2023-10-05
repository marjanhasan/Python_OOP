# read-only --> you can not set the value. Value can not be changed
# getter --> get a value of a property through a method. Most of time, you will get the value of a private attribute
# setter --> set a value of a property through a method. Most of time, you will set the value of a private property
class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money

    # getter without setter
    @property  # method re attibute banay felte use hoy
    def age(self):
        return self._age  # access krte obj.age dilei hbe

    # getter with setter
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return f"Can not be negative"
        else:
            self.__money += value


samsu = User("Kopa", 21, 12000)
# the way to access getter and setter property
print(samsu.age)
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)
