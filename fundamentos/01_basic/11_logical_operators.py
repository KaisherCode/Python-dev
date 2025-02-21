# Logical operators

# Operator AND

print('AND')
print('True and True: ', True and True) # output: True 
print('True and False: ', True and False) # output: False
print('False and True: ', False and True) # output: False
print('False and False: ', False and False) # output: False

print(10 > 5 and 5 <10) # output: True
print(10 >5 and 5 > 10) # output: False

stock = input('Enter stock number: =>')
stock = int(stock)
print(stock >= 100 and stock <= 1000)

# Operator OR
print('OR')
print('True or True', True or True) # output: True
print('True or False', True or False) # output: True
print('False or True', False or True) # output: True
print('False or False', False or False) # output: False

role = input('Enter the role: ')
print(role == 'admin' or role == 'seller')