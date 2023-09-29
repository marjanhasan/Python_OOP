n = int(input())
arr = list(map(int, input().split()))
cnt = 0
flag = False
while True:
    for i in range(n):
        if arr[i] % 2 != 0:
            flag = True
            break
        arr[i] /= 2
    if flag:
        break
    cnt += 1
print(cnt)
