# Project - Rock-paper-scissors game

import random
options = ('rock','paper','scissor')
rouns = 1
computer_wins = 0
user_wins = 0

while True:
    print('*'*10)
    print('ROUND', rouns)
    print('*'*10)

    print('computer wins: ', computer_wins)
    print('user wins:', user_wins)

    user_option = input('Enter Rock, Paper or Scissor: ')
    user_option = user_option.lower()

    if  not user_option in options:
        print('This option is not valid')

    computer_option = random.choice(options)

    print('User option: ', user_option)
    print('Computer option: ', computer_option)

    if user_option == computer_option:
        print('Tie')
    elif user_option == 'rock':
        if computer_option == 'scissor':
            print('rock wins over scissor')
            print('user gana')
            user_wins += 1
        else:
            print('Paper wins over rock')
            print('computer wins')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('paper wins over rock')
            print('user win')
            user_wins += 1
        else:
            print('scissor wins over paper')
            print('computer wins')
            computer_wins += 1
    elif user_option == 'scissor':
        if computer_option == 'paper':
            print('Scissor wins over paper')
            print('user wins')
            user_wins += 1
        else:
            print('rock wins over scissors')
            print('computer wins')
            computer_wins += 1
    if computer_wins == 3:
        print('Winner is the computer')
        break
    if user_wins == 3:
        print('Winner is the user')
        break
    rouns += 1