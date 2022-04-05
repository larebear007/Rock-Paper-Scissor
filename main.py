# ROCK, PAPER, SCISSORS GAME

import random
import time


def play():
    print('\nRock . . .')
    time.sleep(1)
    print('Paper . . .')
    time.sleep(1)
    print('Scissors . . .')
    time.sleep(1)
    print('GO!')

    u_win = 0
    c_win = 0
    while True:
        # User choice
        u_choice = None
        while True:
            x = input('Type  Rock,  Paper,  or  Scissors:  ')
            x = x.lower()
            if x == 'rock' or x == 'r':
                u_choice = 'r'
                break
            elif x == 'paper' or x == 'p':
                u_choice = 'p'
                break
            elif x == 'scissors' or x == 'scissor' or x == 's':
                u_choice = 's'
                break
            else:
                print('Sorry, try that again... ')
                continue

        # Computer choice
        game_list = ['Rock', 'Paper', 'Scissors']
        y = random.choice(game_list)
        c_choice = None
        if y == 'Rock':
            c_choice = 'r'
        elif y == 'Paper':
            c_choice = 'p'
        elif y == 'Scissors':
            c_choice = 's'

        # Record keeping
        print('Computer:', y)
        if u_choice == c_choice:
            u_win += 0
            c_win += 0
            print('Tie')
        elif (u_choice == 'r' and c_choice == 's') or (u_choice == 'p' and c_choice == 'r') \
                or (u_choice == 's' and c_choice == 'p'):
            u_win += 1
            print('Wahoo!')
        elif (c_choice == 'r' and u_choice == 's') or (c_choice == 'p' and u_choice == 'r') \
                or (c_choice == 's' and u_choice == 'p'):
            c_win += 1
            print('Ahh rats.')
        else:
            print('bug in "RECORD KEEPING" code')

        print('Score: you', u_win, ', computer', c_win)

        # user or computer win
        if u_win == 3:
            print('YOU WIN!  :) ')
            break
        elif c_win == 3:
            print('COMPUTER WINS! ... sorry :(')
            break

    # restart game option
    restart = input('Would you like to play again?:  ')
    re = restart.lower()
    if re == 'yes' or re == 'y' or re == 'yeah' or re == 'yah':
        print('Let\'s go!')
        play()
    else:
        print('Thanks for playing. Come again any time!')
        quit()


def intro():
    while True:
        print('Welcome to Rock, Paper, Scissors')
        time.sleep(.5)
        print('Best 3 out of 5 turns wins the game!')
        start = input('\nReady to play Rock, Paper, Scissors?: ')
        st = start.lower()
        if st == 'yes' or st == 'y' or st == 'yeah' or st == 'yah':
            print('Let\'s go!')
            play()
            break
        elif st == 'no' or st == 'n' or st == 'nah' or st == 'nope':
            print('Come back any time!')
            quit()
        else:
            print('Sorry, I didn\'t understand. Type "yes" to get started!')
            continue


intro()
play()
