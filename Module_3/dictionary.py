# dictionary
# key value pair
# object
# hash table
person = {"name": "Marjan", "Age": 26, "Job": "Bekar"}
print(person)
print(person["name"])
print(person.keys())
print(person.values())
person["language"] = "Python"
person["name"] = "Marjan Hasan"
del person["Job"]
print(person)

# looping
for key, value in person.items():
    print(key, value)
