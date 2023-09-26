t = int(input())
while t != 0:
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    sum = 0
    for i in range(a, b):
        if i == a:
            continue
        if i % 2 == 1:
            sum += i
    print(sum)
    t -= 1
