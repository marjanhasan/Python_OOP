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

# 13)
# reversed (returns a reverse iterator object)
numbers = [1, 2, 3, 4, 5]
rev_num = reversed(numbers)
# print(list(rev_num)) [5, 4, 3, 2, 1]

# 14)
# round (return a round number)
x = round(5.76543, 2)
# print(x) 5.77
x = round(5.76543)
# print(x) 6

# 15)
# set (returns a set object)
x = set(("apple", "banana", "cherry"))  # {'banana', 'apple', 'cherry'}
# print(x)

# 16)
# slice (returns a slice object)
a = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = slice(2)  # ['a', 'b']
x = slice(3, 5)  # ["d", "e"]
x = slice(0, 8, 3)  # ['a', 'd', 'g']
# print(a[x])

# 17)
# sorted (returns a sorted list)
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
sort_des = sorted(numbers, reverse=True)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
tuple_values = (7, 2, 5, 1, 8)
sorted_tuple = sorted(tuple_values)  # [1, 2, 5, 7, 8]
word = "Python"
sorted_word = sorted(word)
# print("".join(sorted_word)) Phnoty
words = ["apple", "banana", "cherry", "date"]
sorted_words_by_length = sorted(words, key=len)  # ['date', 'apple', 'banana', 'cherry']
pairs = [(1, 5), (3, 2), (2, 8), (4, 7)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])  # [(3, 2), (1, 5), (4, 7), (2, 8)]

# 18)
# sum (returns sum)
a = (1, 2, 3, 4, 5)
x = sum(a)  # 15
x = sum(a, 7)  # 22
# print(x)

# 19)
# tuple (returns a tuple)
x = tuple(("apple", "banana", "cherry"))  # ('apple', 'banana', 'cherry')
# print(x)

# 20)
# type (returns type)
a = ("apple", "banana", "cherry")
b = "Hello World"
c = 33

x = type(a)  # <class 'tuple'>
y = type(b)  # <class 'str'>
z = type(c)  # <class 'int'>
# print(x, y, z)
