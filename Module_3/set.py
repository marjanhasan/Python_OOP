# set is a unique values collection
# List --> [1,2,3]
# tuple --> (1,2,3)
# set --> {1,2,3}
A = {1, 2, 3, 5}
B = {2, 5, 6, 9}
print(A & B)  # intersection
print(A | B)  # union
# we can not modify the value via index
# we can traverse, add and remove values
for n in A:
    print(n)
A.add(9)
print(A)
