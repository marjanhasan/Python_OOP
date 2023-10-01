# Ena Poribohon


class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.buses = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisor = []
        self.fare = []


class Drivers:
    def __init__(self, name, age, licence) -> None:
        self.name = name
        self.age = age
        self.licence = licence


class Counter:
    def __init__(self) -> None:
        pass

    def purchase_a_ticket(self, departure, destination):
        pass


class Supervisor:
    pass


class Passenger:
    pass


lal_mia = Drivers("Lal", "12BA", 32)
