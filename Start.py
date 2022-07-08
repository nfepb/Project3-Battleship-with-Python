"""
Legend:
"." = empty space
"O" = empty location hit
"@" = part of ship on player game board
"X" = part of ship that was hit
"""


from random import randint

# Global variables for the boardgames

GRID = [[]]

convert_letters_to_numbers_for_coordinates = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E':4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

# Definition of the functions to launch the game
# Ask for input to define the size of the game board

def game_board_representation(game_board, board_size):
    while True:
        board_size = input("How big do you want the game board to be? Please enter a value between 5 and 9: \n")
        try:
            row_size_integer = int(board_size)
            if row_size_integer < 5 or row_size_integer > 9:
                print("Please enter a number included between 5 and 9. \n")
                return False
        except:
            print("Incorrect value. Please enter a number included between 5 and 9. \n")
            return False

        return True

    game_board = [["+_" for x in range(game_board.board_size)] for y in range(game_board.board_size)]
    game_board.display = game_board
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

# Represent the boardgame for the player and computer
# Allow player input to select where to place a hit to find computer ship

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

"""
        column = input('Please enter a ship column between A and I: \n').upper()
        while column not in 'ABCDEFGHI':
            print('Incorrect value. Please try with another value. \n')
            column = input('Please enter a ship column between A and I: \n').upper()
    return int(row) - 1, letters_to_numbers[column]

"""

# Keep track of the number of ship hit

def track_number_ship_hit():
    pass

def start_game():
    populate_ships_on_board()
    turns = 10
    pass

def main():
    """
    The main function to call on the previously defined functions
    main() will launch the game 
    """
    player = Player("", 0, [])
    game_board_representation()