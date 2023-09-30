class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehzabin = Shop("Mehjabin")
mehzabin.add_to_cart("Shoe")
mehzabin.add_to_cart("Phone")
print(mehzabin.cart)

nisho = Shop("Nishoo")
nisho.add_to_cart("Hat")
nisho.add_to_cart("Watch")
print(nisho.cart)
