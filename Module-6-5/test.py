class Product:
    def __init__(self, item) -> None:
        self.item = item

    def __repr__(self) -> str:
        return f"Product name: {self.item}"


class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_product(self, item):
        product = Product(item)
        self.products.append(item)

    def buy_product(self, item):
        for product in self.products:
            if product == item:
                print("Successfully Purchase", item)
                return
        print(item, "is not available")

    def __repr__(self) -> str:
        for product in self.products:
            print(product)
        return f"Thank you for shopping"


raj_store = Shop("raj")
raj_store.add_product("Sugar")
raj_store.add_product("Dandy")
raj_store.buy_product("Sugar")
print(raj_store)
