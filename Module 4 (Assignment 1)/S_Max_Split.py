s = input()
l = 0
r = 0
arr = []
for c in s:
    if c == "L":
        l += 1
    else:
        r += 1
    if l == r:
        sz = l + r
        arr.append(s[:sz])
        s = s[sz:]
        l = 0
        r = 0
print(len(arr))
for c in arr:
    print(c)
