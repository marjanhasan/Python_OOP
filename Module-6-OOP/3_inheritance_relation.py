# base class, parent class, common attribute + functionality class
# derived class, child class, uncommont attribute + functionality class


# base class
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f"Running Gadget: {self.brand}"


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f"Learning Python!!"


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, sim) -> None:
        self.sim = sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f"Sending SMS to {number} with {text}"

    def __repr__(self) -> str:
        return f"{self.brand} phone having {self.price}, {self.color}, {self.origin} & {self.sim} sim."


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


my_phone = Phone("Samsung", 22000, "Silver", "Vietnam", 2)
print(my_phone)
