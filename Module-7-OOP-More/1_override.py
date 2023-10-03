class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("VAT diye mangsho khay")

    def exercise(self):
        # person class jara inherit krbe tader forcefully override krabe
        # ei method ta call dile kisu akta krte hbei nahole error dibe na
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # Person class er eat methodk override krlam
    def eat(self):
        print("Sea Food")

    def exercise(self):
        print("Gym is going by neighbours")

    # Overloading
    # + overload
    def __add__(self, other):
        return self.age + other.age

    # * overload
    def __mul__(self, other):
        return self.weight * other.weight

    # greater than operator overloads
    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer("Hasan", 38, 68, 75, "BD")
mushi = Cricketer("Rahim", 36, 60, 65, "BD")
# sakib.eat()
# sakib.exercise()

# Over Loading
print(sakib + mushi)
print(sakib * mushi)
print(sakib > mushi)
