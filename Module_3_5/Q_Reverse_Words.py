s = input()
words = s.split(" ")
rev = [word[::-1] for word in words]
res = " ".join(rev)
print(res)
# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q
