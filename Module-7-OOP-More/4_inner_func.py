def double_decker():
    print("Starting the double decker")

    def inner_fun():
        print("Inside the inner func")
        return f"return inner func"

    return inner_fun  # we can return a function in a function


def do_something(work):
    print("work started")
    work()  # we can pass function as a parameter and call it
    print("work ended")


def coding():
    print("Coding in python")


# print(double_decker())
print(double_decker()())
do_something(coding)
