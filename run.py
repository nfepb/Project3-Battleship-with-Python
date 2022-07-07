"""
Legend:
"." = water or empty space
"@" = part of ship on player game board
"X" = part of ship that was hit
"""


from random import randint

# Global variables for the boardgames

HIDDEN_BOARD = [['+'] * 9 for x in range(9)]
PLAYER_BOARD = [['+'] * 9 for x in range(9)]

convert_letters_to_numbers_for_coordinates = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E':4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

# Definition of the functions to launch the games
# Represent the boardgame for the player and computer
# Create and add the ships on both boards
# Allow player input to select where to place a hit to find computer ship
# Keep track of the number of ship hit

def board_representation(game_board):
    print('     A B C D E F G H I')
    print('     +-+-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in game_board:
        print(row_number, '+'.join(row), end='|')
        row_number += 1
        print(game_board[column][letter])

# Function to populate the ships on the game board
# Populate on game game the result of the selected coordinates and result

def populate_ships_on_board(ship, game_board):
    for ship in range(len(game_board)):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while game_board[ship_row][ship_column] == '@':
            ship_row, ship_column = randint(0, 9), randint(0, 9)
        game_board[ship_row][ship_column] = 'X'

def player_input_coordinates_validation(row, column):
    try:
        row = int(input('Please enter a ship row between 1 and 9: \n'))
        if row < 0 or row > 9:
            print('Incorrect value. Please try with another value. \n')
            return False

    except:
        print('Incorrect value. Please try again. \n')
        return False

    return True


        column = input('Please enter a ship column between A and I: \n').upper()
        while column not in 'ABCDEFGHI':
            print('Incorrect value. Please try with another value. \n')
            column = input('Please enter a ship column between A and I: \n').upper()
    return int(row) - 1, letters_to_numbers[column]


def track_number_ship_hit():
    pass

def start_game():
    populate_ships_on_board()
    turns = 10