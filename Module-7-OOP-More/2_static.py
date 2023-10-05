class Shopping:
    cart = []  # class attribute or static attribute
    origin = "Chine"

    def __init__(self, name, location) -> None:
        self.name = "Jamu na City"  # instance attribute
        self.location = location  # jeta obj er sathe value change krte pare

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"Purchasing {item} for {price} and remaining {remaining}")

    @staticmethod  # eta use krle instance charai use krbo
    def multiply(a, b):
        res = a * b  # etar vetore self.name evabe kaj krbe na
        print(res)

    @classmethod
    def hudai(self, item):  # can be access without obj.hudai()
        print("hudai dekhbar aisi", item)


Shopping.hudai("lungi")
Shopping.multiply(4, 5)  # static method usage
