n = int(input())
arr = list(map(int, input().split()))
brr = arr[::-1]
if arr == brr:
    print("YES")
else:
    print("NO")
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G
