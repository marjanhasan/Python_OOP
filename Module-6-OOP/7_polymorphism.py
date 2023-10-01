# poly --> many
# morph --> different shape


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal making sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Meow Meow")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Gheu Gheu")


class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Beh Beh Beh")


don = Cat("DonJon")
don.make_sound()

shepard = Dog("Desi Shepard")
shepard.make_sound()

mess = Goat("LM")
mess.make_sound()

less = Goat("GoraGori")

animals = [don, shepard, mess, less]

for animal in animals:
    animal.make_sound()
