class Family:
    def __init__(self, address) -> None:
        self.address = address


class School:
    def __init__(self, s_id, level) -> None:
        self.id = s_id
        self.level = level


class Sports:
    def __init__(self, game) -> None:
        self.game = game


class Student(Family, School, Sports):
    def __init__(self, address, s_id, level, game) -> None:
        School.__init__(self, s_id, level)
        Sports.__init__(self, game)
        Family.__init__(self, address)
