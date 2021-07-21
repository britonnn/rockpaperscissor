from random import randint

t = ['rock', 'paper', 'scissors']

while True:
    player_choice = input(' paper or rock or scissors?')
    if player_choice not in t:
        print('invalid command')
    else:
        computer_choice = t[randint(0, 2)]
        print('computer choice is: '+computer_choice)
        if player_choice == 'rock':
            if player_choice == computer_choice:
                print("Tie")
            elif computer_choice == 'paper':
                print('You lose')
            elif computer_choice == 'scissors':
                print('you win')

        if player_choice == 'paper':
            if player_choice == computer_choice:
                print("Tie")
            elif computer_choice == 'scissors':
                print('You lose')
            elif computer_choice == 'rock':
                print('you win')

        if player_choice == 'scissors':
            if player_choice == computer_choice:
                print("Tie")
            elif computer_choice == 'rock':
                print('You lose')
            elif computer_choice == 'paper':
                print('you win')
