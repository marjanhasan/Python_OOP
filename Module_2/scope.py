# global variable
balance = 3000


def expenses(home, outside):
    total = home + outside  # total is a local variable
    global balance  # to access global variable
    balance = balance - total
    return balance


res = expenses(1200, 700)
print(res)
