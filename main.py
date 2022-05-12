from game_images import game_images
from random import randint


def main():
    print('ROCK, PAPER, SCISSORS')
    player = int(input('''
Player's Turn
================
'0' for Rock
'1' for Paper
'2' for Scissors
================
'''))
    print('\nYou chose:')
    print(game_images[player])

    computer = randint(0, 2)
    print('\nComputer chose: ')
    print(game_images[computer])

    if player == computer:
        print('IT\'S A TIE!')
    elif player == 0 and computer == 2:
        print('YOU WIN!')
    elif player == 2 and computer == 0:
        print('YOU LOSE')
    elif player > computer:
        print('YOU WIN!')
    else:
        print('YOU LOSE!')


if __name__ == '__main__':
    main()
