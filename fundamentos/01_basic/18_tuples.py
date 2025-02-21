# Tuples: We can't make changes to them. We using ()

numbers = (1,2,3,4) # Tuple inmmutable
strings = ('nicolle','zule','santi','nicolle') # Tuple
print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

print(numbers)
print(strings.index('zule')) # zule is in position 1
print(strings.count('nicolle')) # 'nicolle' = appers twice

my_list = list(strings) # convert a tuple to a list
print(my_list)
print(type(my_list))

my_list[1] = 'juli' # Modify position 1
print(my_list)

my_tuple = tuple(my_list) # List-to-tuple convertion
print(my_tuple)