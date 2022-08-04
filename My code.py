from random import *

score = 0
played = 0
RPScom = ['rock','paper','scissors']


computer = choice(RPScom)

while True:
    RPS = input("rock, paper, scissors: ")
    print("You have chosen", RPS, "\n", "The computer chose", computer)

    if RPS == 'rock' and computer == 'scissors':
        print("You win")
        score += 1
        played += 1

    elif RPS == 'rock' and computer == 'paper':
        print('You lose')
        played += 1

    elif RPS == 'rock' and computer == 'rock':
        print("Draw")
        played += 1

    elif RPS == 'scissors' and computer == 'rock':
        print("You lose")
        played += 1

    elif RPS == 'scissors' and computer == 'paper':
        print("You win")
        score += 1
        played += 1

    elif RPS == 'scissors' and computer == 'scissors':
        print("Draw")
        played += 1

    elif RPS == 'paper' and computer == 'rock':
        print("You win")
        score += 1
        played += 1

    elif RPS == 'paper' and computer == 'scissors':
        print("You lose")
        played += 1

    elif RPS == 'paper' and computer == 'paper':
        print("Draw")
        played += 1

    else:
        print("enter an option")

    print("Your score is", score)

    if played % 3 == 0:
        game_end = input("Do you want to play again?: ")
        if game_end == 'no':
            break
        else:
            continue
