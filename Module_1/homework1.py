# take 3 nums, output max value
a = input()
b = input()
c = input()
result = max(a, b, c)
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
# print(result)
