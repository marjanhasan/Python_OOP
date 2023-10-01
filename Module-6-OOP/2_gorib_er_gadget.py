class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f"Running laptop: {self.brand}"

    def coding(self):
        return f"Learning Python!!"


class Phone:
    def __init__(self, brand, price, color, sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.sim = sim

    def run(self):
        return f"Running phone: {self.brand}"

    def phone_call(self, number, text):
        return f"Sending SMS to {number} with {text}"


class Camera:
    def __init__(self, brand, color, price, pixel) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass
