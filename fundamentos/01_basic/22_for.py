# loops : for is the most commonly used in Python

# for element in range(20): # out del 0 al 20
#     print(element)

# for item in range(1,10): # out de 1 al 9
#     print(item)

my_list = [23,45,67,43]

for element in my_list:
    print(element)


my_tuple = ('nicolle','juli','santy')

for elem in my_tuple:
    print(elem)


product = {
    'name':"mouse",
    'price':35,
    'stock': 89
}

for key in product:
    print(key,'-->',product[key])

print("*" * 12)
print('Otra forma de iterar')
for key, value in product.items():
    print(key,'-->',value)


people = [
    {
        'name': "nicolle",
        'age':32
    },
    {
        'name': "zulema",
        'age': 25
    },
    {
        'name': "santy",
        'age':21
    }
]

print("*" * 12)
for person in people:
    print('name : ',person['name'])

mi_lista = [1,-1,2,-2,3,-3,4,-4]
new_list=[]

for number in mi_lista:
    if number > 0:
        new_list.append(number)
print(new_list) 