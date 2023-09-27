""" 
taking input as a string

t = input()
ti = int(t)
while ti != 0:
    num = input()
    rev = num[::-1]
    for n in rev:
        print(n, end=" ")
    print()
    ti -= 1 """

# taking input as a number

n = int(input())
for _ in range(n):
    v = int(input())

    while True:
        print(v % 10, end=" ")
        v = v // 10

        if v == 0:
            break

    print()
