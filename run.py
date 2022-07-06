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
    print(' +---------------------+')
    row_number = 1
    for row in game_board:
        print(row_number, '+'.join(row), end='|')
        row_number += 1
        print(game_board[column][letter])

def populate_ships_on_board():
    pass

def player_select_coordinates():
    pass

def track_number_ship_hit():
    pass

def start_game():
    populate_ships_on_board()
    turns = 10