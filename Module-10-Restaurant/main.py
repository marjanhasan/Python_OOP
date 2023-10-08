from menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from users import Chef, Customer, Server, Manager


def main():
    menu = Menu()
    pizza_1 = Pizza("Shutki Pizza", 600, "large", ["shutki", "onion"])
    menu.add_menu_item("pizza", pizza_1)
    pizza_2 = Pizza("Alur Vorta Pizza", 400, "large", ["potato", "onion", "oil"])
    menu.add_menu_item("pizza", pizza_2)
    pizza_3 = Pizza("Dal Pizza", 500, "large", ["dal", "oil"])
    menu.add_menu_item("pizza", pizza_3)

    burger_1 = Burger("Naga Buger", 1000, "chicken", ["bread", "chili"])
    menu.add_menu_item("burger", burger_1)
    burger_2 = Burger("Beef Burger", 1200, "beef", ["goru", "haddi"])
    menu.add_menu_item("burger", burger_2)

    coke = Drinks("Coke", 50, True)
    menu.add_menu_item("drinks", coke)
    coffee = Drinks("Mocha Coffee", 300, False)
    menu.add_menu_item("drinks", coffee)

    menu.show_menu()

    restaurant = Restaurant("Sai Baba restaurant", 2000, menu)

    manager = Manager(
        "kala chan manager", 5, "kala@chan.com", "kaliapur", 1500, "Jan1 2020", "core"
    )
    restaurant.add_employee("manager", manager)

    chef = Chef(
        "Rustom Baburchi",
        6,
        "chupa@rustom.com",
        "rustomNagar",
        3500,
        "Feb 1 2020",
        "Chef",
        "everything",
    )
    restaurant.add_employee("chef", chef)

    server = Server(
        "Chotu Server", 6, "nai@jai.com", "restaurant", 200, "March 1 2020", "server"
    )
    restaurant.add_employee("server", server)

    restaurant.show_employees()


if __name__ == "__main__":
    main()
