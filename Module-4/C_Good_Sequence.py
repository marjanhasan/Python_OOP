n = int(input())
arr = list(map(int, input().split()))
ans = {}
for val in arr:
    if val not in ans.keys():
        ans[val] = 0
    ans[val] += 1
# print(ans)
res = 0
for key, val in ans.items():
    if val < key:
        res += val
    else:
        res += val - key
print(res)
