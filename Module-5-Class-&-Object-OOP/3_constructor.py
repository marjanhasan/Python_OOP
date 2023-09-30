class Phone:
    manufacturar = "China"

    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color


my_phone = Phone("Xiaomi", 12000, "Mid Night Blue")
print(my_phone.name, my_phone.price, my_phone.color)  # Xiaomi 12000 Mid Night Blue
