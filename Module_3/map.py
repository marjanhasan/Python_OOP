numbers = [10, 20, 30, 40, 50, 60]
res = map(lambda x: x * 2, numbers)
print(list(res))

actors = [
    {"name": "john", "age": 10},
    {"name": "don", "age": 12},
    {"name": "bon", "age": 15},
]
jr = filter(lambda actor: actor["age"] < 15, actors)
print(list(jr))
