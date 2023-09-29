n = int(input())
fib = [0, 1]
if n == 1:
    print(0)
elif n == 2:
    for i in fib:
        print(i, end=" ")
else:
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    for n in fib:
        print(n, end=" ")
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y
