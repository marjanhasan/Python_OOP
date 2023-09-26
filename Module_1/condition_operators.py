# conditional operator

# >, <, >=, <=, ==, !=
# ++, -- nai
# +=, -=, *=, /=
# in, not, is, is not, not in,

a = 7
if a > 5 and a % 2 == 1:
    print("5 er beshi")
elif a > 3 or a % 2 == 0:
    print("3 er beshi")
else:
    print("5 & 3 er kom")

is_vip = True

if is_vip is True:
    print("Priority Queue")
else:
    print("Normal Queue")


vip = False

if vip is not True:
    print("Thabra halare")
else:
    print("Boshen Sir")
