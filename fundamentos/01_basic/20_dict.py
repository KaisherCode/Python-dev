# Dict

person = {
    'name':"kaisher",
    'last_name':"Dev",
    'langs':['Python','JavaScript'],
    'age': 28
}

print(person)

person['name']='Wilsonne' # change name
print(person)
person['age'] -= 5
person['langs'].append('rust') # Add programing language
print(person)

del person['last_name'] # Delete last name
print(person)
person.pop('age') # Delete age
print(person)

print('items')
print(person.items()) # Display in a tuple all dict.

print('keys')
print(person.keys()) # Display dict key

print('values')
print(person.values()) # Display dict values