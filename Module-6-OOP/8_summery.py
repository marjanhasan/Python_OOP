class Book:
    def __init__(self, author) -> None:
        self.author = author

    def read(self):
        raise NotImplementedError


class Physics(Book):
    def __init__(self, author, lab) -> None:
        self.lab = lab
        super().__init__(author)

    def read(self):
        print("Reading physics book")


topon = Physics("topon", True)
print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))
topon.read()
