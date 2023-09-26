t = input()
ti = int(t)
while ti != 0:
    num = input()
    rev = num[::-1]
    for n in rev:
        print(n, end=" ")
    print()
    ti -= 1
