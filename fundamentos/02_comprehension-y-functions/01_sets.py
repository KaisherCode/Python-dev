# sets | conjuntos
# Un conjunto no acepta elementos duplicados

set_countries = {'colombia','mexico','perú'}
print(set_countries)
print(type(set_countries))

set_number = {1,2,2,443,23}
print(set_number)

set_types = {1,'hola',False,12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc','cbv','as','abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)