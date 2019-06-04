import sys
import os
from game_board import board

POSITIONS_PICKED = []
lets_play = True
while lets_play:
    print('Lets play tic-tac-toe')

    # User decides to be 'X' or 'O'
    valid = False
    while valid is not True:
        print("Player 1, do you want to be 'X' or 'O'? ")
        player1 = input().upper()
        player2 = ""

        if player1 == 'X':
            print("Player 1 will be 'X' and Player 2 will be 'O'.\n")
            player2 = "O"
            valid = True
        elif player1 == 'O':
            print("Player 1 will be 'O' and Player 2 will be 'X'.\n")
            player2 = "X"
            valid = True
        elif player1 != 'X' or player1 != 'O':
            print('That was not a valid input. Please try again...\n')

    #  Asks if they are ready to play to start game if not to close program
    valid = False
    while valid is not True:
        print('Ready to play? (Y)es or (N)o')
        ready = input().upper()

        if ready == 'Y' or ready == 'YES':
            print("Lets Begin!\nGood Luck!\n")
            valid = True
        elif ready == 'N' or ready == 'NO':
            print("Until next time... Good Bye!")
            sys.exit()
        elif ready != 'Y' or ready != 'YES' or ready != 'N' or ready != 'NO':
            print('That was not a valid input. Please try again...\n')

    # Display board
    board()

    counter = 0
    game_over = False
    # Keep playing until there is a winner or draw
    while game_over is not True:
        position_valid = False
        draw = False
        mark = ""
        counter = counter % 2
        player_turn = counter + 1

        if player_turn == 1:
            mark = player1
        elif player_turn == 2:
            mark = player2

        while position_valid is not True:
            # Declares draw if board is full and a winner has not been declared
            if len(POSITIONS_PICKED) == 9:
                print('We got ourselves a draw!')
                draw = True
                break

            # Asks where to place their marker
            print(f'\nPlayer {player_turn}, where do you want to place {mark}:')
            position = int(input())

            # Validates user input and places mark on board
            if position < 1 or position > 9:
                print(f'\nSorry, {position} is not an option on the board. Please pick again...\n')
            elif position in POSITIONS_PICKED:
                print(f'\nSorry, {position} was already picked. Please pick again...\n')
            else:
                # Moves down 100 lines so old boards dont show
                print('\n'*100)
                POSITIONS_PICKED.append(position)
                game_over = board(position, mark)
                position_valid = True

        counter += 1
        if draw:
            break

    valid = False
    # Asks if they want to play again or not
    while valid is not True:
        print('Play again? (Y)es or (N)o')
        play_again = input().upper()

        if play_again == 'Y' or play_again == 'YES':
            print('\n')
            # This will restart the program. It runs 'python tictactoe.py'
            os.execv(sys.executable, ['python'] + sys.argv)
        elif play_again == 'N' or play_again == 'NO':
            print("Until next time... Good Bye!")
            sys.exit()
        elif play_again != 'Y' or play_again != 'YES' or play_again != 'N' or play_again != 'NO':
            print('That was not a valid input. Please try again...\n')
