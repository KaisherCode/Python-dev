# Dictionaries : They are of key-value pairs. We using {}

my_dict = {}
print(type(my_dict))

my_dict = {
    'name': "Kaisher",
    'last_name':"Dev",
    'age': 27,
    'city': "Lima"
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age')) # With get prevent error

print('city' in my_dict)
print('avion' in my_dict)