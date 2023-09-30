class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item["price"] * item["quantity"]
        print("Total Price:", total)
        if amount < total:
            print(f"Please provide more {total-amount}")
        else:
            changes = amount - total
            print(f"Here is your item and changes {changes}")


shopon = Shopping("Shopon")
shopon.add_to_cart("Rice", 80, 5)
shopon.add_to_cart("Egg", 15, 12)
shopon.add_to_cart("Potato", 35, 3)
print(shopon.cart)
shopon.checkout(690)
