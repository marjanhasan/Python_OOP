s = input()
words = s.split(" ")
rev = [word[::-1] for word in words]
res = " ".join(rev)
print(res)
