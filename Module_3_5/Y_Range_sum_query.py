n, q = map(int, input().split())
a = list(map(int, input().split()))
pre = [0] * n

pre[0] = a[0]
for i in range(1, n):
    pre[i] = a[i] + pre[i - 1]

while q != 0:
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == 0:
        res = pre[r]
    else:
        res = pre[r] - pre[l - 1]
    print(res)
    q -= 1
