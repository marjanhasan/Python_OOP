from abc import ABC, abstractmethod

# Abstract Base Class


class Animal(ABC):
    @abstractmethod  # enforced to all derived class to have eat method
    def eat(self):
        print(f"Hey nana, eating banana")

    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()

    def eat(self):
        print("Hey na nana, I am eating banana!")


layki = Monkey("lucky")
layki.eat()
