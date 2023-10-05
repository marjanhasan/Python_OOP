class Product:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f"Product id: {self.id} & Product name: {self.name}"


class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_products(self, item):
        id = len(self.products) + 11
        product = Product(id, item)
        self.products.append(product)

    def buy_products(self, item):
        for product in self.products:
            if product.name == item:
                print(item, "Purchase successfully")
                return
        print(item, "is not available")


puddar = Shop("puddar")
puddar.add_products("Rice")
puddar.add_products("Potato")
print(puddar.products)
puddar.buy_products("rice")
