# Conditional

if True:
    print('Should be executed')

if False:
    print('Never executed')

pet = input('What is your favorite pet?')
if pet == 'dog':
    print('Great, you have good taste')
elif pet == 'cat':
    print('I hope you are lucky')
elif pet == 'fish':
    print(' your are the best')
else:
    print("You don't have any interesting pets.")

stock = int(input('Enter the stock: '))
if stock >= 100 and stock <= 1000:
    print('Sctock is correct')
else:
    print('Sctock is incorrect')