import math


def timer(func):
    def inner(*args, **kwargs):
        print("time started")
        func(*args, **kwargs)
        print("time ended")

    return inner


@timer
def get_factorial(n):
    print("factorial starting")
    result = math.factorial(n)
    print(f"factorial of {n} is: {result}")


get_factorial(n=5)

# vejailla way to decorate
# timer(get_factorial)()
