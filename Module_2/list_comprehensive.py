numbers = [34, 23, 24, 65, 76, 5, 33, 57, 24, 32, 12, 89, 90]
odds = []
for num in numbers:
    if num % 2 == 1:
        odds.append(num)
print(odds)
odd = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odd.append(num)
print(odd)

oddx = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
print(oddx)
