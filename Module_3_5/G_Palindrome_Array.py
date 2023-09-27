n = int(input())
arr = list(map(int, input().split()))
brr = arr[::-1]
if arr == brr:
    print("YES")
else:
    print("NO")
