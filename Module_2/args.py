def num(*args):
    # print(args)
    for n in args:
        print(n)
    return args


alll = num(1, 2, 3, 4)
no_val = num()
print(alll)  # return tuple first bracket wala values (1, 2, 3, 4)
print(no_val)  # return () empty tuple
