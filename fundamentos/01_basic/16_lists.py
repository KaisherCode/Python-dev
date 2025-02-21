# Lists: use square brackets[]

numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes','play videogames']
print(tasks)

types = [1,'True','hello']
print(types)

print(numbers[0])
print(tasks[0])
text ='Hello'
# text[0]='W' --> INMMUTABLE can not be modified

tasks[0] = 'watch netflix movies'
print(tasks)

print(numbers[:3])
print(True in types)
print('hello' in types)