x, n = map(int, input().split())
sum = 0
for i in range(2, n + 1, 2):
    sum += x**i
print(sum)
# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F
