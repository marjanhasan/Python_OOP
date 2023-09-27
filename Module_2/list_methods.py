# 1)
# append (add to the last index)
# syntax: listName.append(element)
nums = [10, 20, 30, 40, 50]
nums.append(60)
# print(nums) [10, 20, 30, 40, 50, 60]

# 2)
# insert (add value to the specific position)
# syntax: listName.insert(pos,val)
nums.insert(2, 70)
# print(nums) [10, 20, 70, 30, 40, 50, 60]

# 3)
# remove (remove the element if exists)
# listName.remove(val)
if 30 in nums:
    nums.remove(30)
# print(nums) [10, 20, 70, 40, 50, 60]

# 4)
# pop (remove the value at specific positions and returns the pop value)
# syntax list.pop(pos)
# listName.pop() will remove the last element
last = nums.pop()
# print(nums, last) [10, 20, 70, 40, 50] 60

# 5)
# clear (remove all the element from a list)
# syntax listName.clear()
fruits = ["apple", "banana", "cherry", "orange"]
fruits.clear()
# print(fruits) []

# 6)
# copy (returns a copy of a list)
# listName.copy()
fruits = ["apple", "banana", "cherry", "orange"]
x = fruits.copy()
# print(x) ['apple', 'banana', 'cherry', 'orange']

# 7)
# count (returns the number of element with the specific values)
# listName.count()
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
# print(x) 2

# 8)
# extend (add list b to list a's end)
# a.extend(b)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)  # returns [1,2,3,4,5,6,7,8]
# print(a) [1, 2, 3, 4, 5, 6, 7, 8]

# 9)
# index (returns the specific position/index)
# listName.index(val)
fruits = ["apple", "banana", "cherry"]
x = fruits.index("cherry")
# print(x) 2

# 10)
# reverse (reverse the list)
# listName.reverse()
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
# print(fruits) ['cherry', 'banana', 'apple']

# 11)
# sort (sort in ascending order by default)
# listName.sort()
cars = ["Ford", "BMW", "Volvo"]
cars.sort()

# sort (sort in descending order)
# listName.sort(reverse=True)
cars = ["Ford", "BMW", "Volvo"]
cars.sort(reverse=True)
