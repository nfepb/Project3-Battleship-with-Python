"""
Legend:
"." = empty space
"O" = empty location hit
"@" = part of ship on player game board
"X" = part of ship that was hit
"""


from glob import glob
from random import randint

# Global variables for the boardgames
# Global variable to the grid
GRID = [[]]
# Global variable for the grid size
GRID_SIZE = 10
# Global variable for the number of ships to position
NUMBER_OF_SHIPS = 10
# Global variable for the number of tries remaining to win the game
TRIES_LEFT = 50
# Global variable for game over
GAME_OVER = False
# Global variable for the number of ennemy ships sunk
NUMBER_OF_SHIPS_SUNK = 0
# Global variable for the ship positions
SHIP_POSITION = [[]]
# Global variable for the alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Defining the functions to execute the game
def define_grid_and_place_ships(start_row, end_row, start_col, end_col):
    """
    Function that will check on the grid if it the location is good prior to placing a ship
    If there already is a ship, it will return false
    """
    global GRID
    global SHIP_POSITION
    ship_positioning_coordinates = True

    try:
        for row in range(start_row, end_row):
            for column in range(start_col, end_col):
                if GRID[row][column] != ".":
                    ship_positioning_coordinates = False

    except: # pylint: disable=W0702
        SHIP_POSITION.append([start_row, end_row, start_col, end_col])
        for row in range(start_row, end_row):
            for column in range(start_col, end_col):
                GRID[row][column] = "@"
    return ship_positioning_coordinates

def position_ship_on_grid(row, column, direction, length):
    """
    Function that will position a ship on the grid
    This function will call on define_grid_and_place_ships to check if this is an adequate position
    """
    global GRID_SIZE

    start_row, end_row, start_column, end_column = row, row + 1, column, column + 1
    if direction == "right":
        if column + length >= GRID_SIZE:
            return False
        end_column = column + length

    elif direction == "left":
        if column - length < 0:
            return False
        start_column = column - length + 1

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length < 0:
            return False
        end_row = row + length

    return define_grid_and_place_ships(start_row, end_row, start_column, end_column)

def create_grid():
    """
    Function will create 10x10 grid and position ships randomly of different sizes & positions
    """
    global GRID
    global GRID_SIZE
    global NUMBER_OF_SHIPS
    global SHIP_POSITION

    rows, columns = (GRID_SIZE, GRID_SIZE)
    GRID = []

    for r in range(rows):
        row = []
        for c in range(columns):
            row.append("| . ")
        GRID.append(row)

    number_of_remaining_to_place = 0

    SHIP_POSITION = []

    while number_of_remaining_to_place != NUMBER_OF_SHIPS:
        random_row_for_ship_placement = random.randint(0, rows -1)
        random_column_for_ship_placement = random.randint(0, columns -1)
        ship_direction = random.choice["right", "left", "up", "down"]
        ship_size = random.randint(2, 5)
        if position_ship_on_grid(random_row_for_ship_placement, random_column_for_ship_placement, ship_direction, ship_size):
            number_of_remaining_to_place += 1


def print_game_board_grid():
    """
    Function will print the grid.
    Rows are A to J and columns 1 to 10
    """
    
    pass

def validate_selected_coordinates():
    """
    Function will validate the player input for the selected coordinates
    """

    pass

def check_if_ship_is_sunk(row, column):
    """
    Function will check if all the parts of the ship have been found and it is sunk
    """

    pass

def select_coordinates():
    """
    Function will check the grid and return the outcome of the try
    This function will validate (validate_selected_coordinates) the value prior to running
    """

    pass

def is_game_over():
    """
    Function to check is the game is over following conditions:
    - all ships have been sunk (player or computer)
    - player ran out of tries
    """

    pass

def main():
    """
    Main function that will call on the other functions in order to run the game
    """
    pass

main()