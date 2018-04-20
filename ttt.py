from IPython.display import clear_output
import random

def display_board(board):

    clear_output() #clears previous board

    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():

    marker=' '

    '''
    Output is in the form of a Tuple(Player1 marker, Player2 marker)
    '''

    while not (marker == 'X' and marker == 'O'):
        marker = input("Player 1, choose X or O:").upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, mark):
    #Win check
    #check all rows, columns and diagonals
    return ((board[7] == board[8] == board[9] == mark) or #row
    (board[4] == board[5] == board[6] == mark) or #row
    (board[1] == board[2] == board[3] == mark) or #row
    (board[7] == board[4] == board[1] == mark) or #column
    (board[8] == board[5] == board[2] == mark) or #column
    (board[9] == board[6] == board[3] == mark) or #column
    (board[7] == board[5] == board[3] == mark) or #diagonal
    (board[9] == board[5] == board[1] == mark)) #diagonal

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):

        if space_check(board,i):
            return False
    #board is full
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position): #incorrect entry
        position = int(input("Choose a position: (1-9)"))

    return position

def replay():

    return input("Play again? Y or N:").lower().startswith('y')

print("Welcome to the game!")

while True:
    #turns
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n:")

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    #gameplay
    while game_on:

        if turn == 'Player 1':

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

             display_board(the_board)
             position = player_choice(the_board)
             place_marker(the_board, player2_marker, position)

             if win_check(the_board, player2_marker):
                 display_board(the_board)
                 print("Player 2 has won the game!")
                 game_on = False
             else:
                 if full_board_check(the_board):
                     display_board(the_board)
                     print("Tie!")
                     game_on = False
                 else:
                     turn = 'Player 1'


    if not replay():
        break
