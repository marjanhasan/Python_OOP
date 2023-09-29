maximum = max([10, 20, 40, 15, 50])
# print(maximum) 50
minimum = min([10, 20, 40, 15, 50])
# print(minimum) 10
summention = sum([10, 20, 40, 15, 50])
# print(summention) 135
count = len([10, 20, 40, 15, 50])
# print(count) 5
ch = len("Programming")
# print(ch) 11

# 1)
# abs (returns a positive value whether it was negative/positive)
# abs(n)
x = abs(-7.25)
# print(x) 7.25

# 2)
# enumerate (takes list, tuple, dict and return index and values)
# enumerate(var)
x = ("apple", "banana", "cherry")
y = enumerate(x)
# print(list(y)) [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# 3)
# float (returns a floating value)
x = float(3)
# print(x) 3.0

# 4)
# int (returns an integer number)
x = int(3.5)
# print(x) 3

# 5)
# dict (retuns a dictionary)
x = dict(name="John", age=36, country="Norway")
# print(x) {'name': 'John', 'age': 36, 'country': 'Norway'}

# 6)
# len (returns a length of an object/collections)
mylist = ["apple", "banana", "cherry"]
x = len(mylist)
# print(x) 3

# 7)
# list (retuns a list)
x = list(("apple", "banana", "cherry"))
# print(x) ['apple', 'banana', 'cherry']

# 8)
# map (returns value after executing function within it object)
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x**2, numbers))
# print(doubled_numbers) [1, 4, 9, 16, 25]

# 9)
# max (returns maximum value within it)
numbers = [1, 2, 3, 4, 5]
x = max(numbers)
# print(x) 5

# 10)
# min (returns the minimum values within it)
numbers = [1, 2, 3, 4, 5]
x = min(numbers)
# print(x) 1

# 11)
# pow (Returns the value of x to the power of y)
x = pow(2, 3)
# print(x) 8

# 12
# range (works like i in for loop)
# 0 to 9 (10 is not included)
# for n in range(0, 10, 2):
#     print(n)
