n = int(input())
arr = list(map(int, input().split()))
mn = min(arr)
mx = max(arr)
for i in range(n):
    if arr[i] == mx:
        arr[i] = mn
        print(arr[i], end=" ")
        continue
    if arr[i] == mn:
        arr[i] = mx
        print(arr[i], end=" ")
        continue
    print(arr[i], end=" ")
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
