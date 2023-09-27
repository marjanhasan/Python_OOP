def doubled(n):
    return n * 2


res = doubled(4)
print(res)

doubled_fun = lambda num: num * 2
res_l = doubled_fun(4)
print(res_l)

squared = lambda num: num**2
res_ll = squared(4)
print(res_ll)

add = lambda x, y: x + y
res_lll = add(10, 20)
print(res_lll)
