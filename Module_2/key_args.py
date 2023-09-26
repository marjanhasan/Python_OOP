def name(first, last):
    print(f"{first} {last}")
    return f"{first} {last}"


nam = name("marjan", "Hasan")
# print(nam)


ulta_nam = name(last="hasan", first="marjan")
# print(ulta_nam)


def hujur(first, last, **title):
    print(title["respect"])
    for key, val in title.items():
        print(key, val)
    return f"{first} {last} {title}"


taheri = hujur("Gias", "Uddin", respect="hajrat", titl="moulana", degree="sheikh")
# print(taheri)


# we can return multiple variable in python
def sum(a, b):
    jog = a + b
    biyog = a - b
    # return jog, biyog # return tuple
    return [jog, biyog]  # return list type


a_lot = sum(50, 10)
print(a_lot)  # return tuple
