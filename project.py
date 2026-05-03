import random
game_images=['rock','paper','pen']
user_choice = int(input('enter the choice Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number,you loose")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("computer choose:")
    print(game_images[user_choice])
    if user_choice == computer_choice:
        print('it is draw')
    elif user_choice > computer_choice:
        print('u wins')
    elif user_choice<computer_choice:
        print('computer wins')
    elif computer_choice == 0 and user_choice == 2:
        print('computer wins')
    elif user_choice == 0 and computer_choice == 2:
        print('you win')
