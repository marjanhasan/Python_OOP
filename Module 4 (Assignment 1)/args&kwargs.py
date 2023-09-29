def numbers(*args):
    for n in args:
        print(n, end=" ")
    print()


numbers(10, 20, 30, 40)


def age(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" ")
    print()


age(Musfiq=10, Rakib=20, Fatema=30, Sakib=40)
