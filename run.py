from curses.ascii import isalpha
from glob import glob
from random import randint

# Global variables for the boardgames
# Global variable for the welcome message
INTRO = """
Welcome admiral! This is a game of battleship.
The objective is to win the battle by finding and sinking all the ennemy's ships.
You have 50 tries to sink the ennemy fleet before they overrun you.

Legend:
"." = empty space
"O" = empty location hit
"@" = part of ship on player game board
"X" = part of ship that was hit

Good luck admiral! \n
"""
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
# Function to build grid visibile to the player
def define_grid_and_place_ships(start_row, end_row, start_col, end_col):
    """
    Function that will check on the grid if it the location is good prior to placing a ship
    If there already is a ship, it will return false
    """
    ship_positioning_coordinates = True

    try:
        for row in range(start_row, end_row):
            for column in range(start_col, end_col):
                if GRID[row][column] != ".":
                    ship_positioning_coordinates = False

    except:  # pylint: disable=W0702
        SHIP_POSITION.append([start_row, end_row, start_col, end_col])
        for row in range(start_row, end_row):
            for column in range(start_col, end_col):
                GRID[row][column] = "@"
    return ship_positioning_coordinates

# Function to populate the ships on the grid in any direction
def position_ship_on_grid(row, column, direction, length):
    """
    Function that will position a ship on the grid
    This function will call on define_grid_and_place_ships to check if this is an adequate position
    """

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

    return define_grid_and_place_ships(start_row, end_row, start_column,
                                       end_column)


def create_grid():
    """
    Function will create 10x10 grid and position ships randomly of different sizes & positions
    """

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
        random_row_for_ship_placement = random.randint(0, rows - 1)
        random_column_for_ship_placement = random.randint(0, columns - 1)
        ship_direction = random.choice["right", "left", "up", "down"]
        ship_size = random.randint(2, 5)
        if position_ship_on_grid(random_row_for_ship_placement,
                                 random_column_for_ship_placement,
                                 ship_direction, ship_size):
            number_of_remaining_to_place += 1


def print_game_board_grid():
    """
    Function will print the grid.
    Rows are A to J and columns 1 to 10
    """

    ALPHABET = ALPHABET[0:len(GRID) + 1]
    validate_characters_in_correct_coordinates = True

    # Print out the alphabet based on the length of the grid
    for row in range(len(GRID)):
        print(ALPHABET[row], end="|")
        for column in range(len(GRID[row])):
            if GRID[row][column] == "@":
                if validate_characters_in_correct_coordinates:
                    # Print @ for the ship parts that should be seen
                    print("@", end=" ")
                else:
                    # print . for the ship parts that should not be visible to the player
                    print(".", end=" ")
            else:
                print(GRID[row][column], end=" ")
        print("")

    print("  ", end=" ")
    # Print out the numbers on the grid based on the length of the grid
    for i in range(len(GRID[0])):
        print(str(i), end=" ")
    print("")


def validate_selected_coordinates():
    """
    Function will validate the player input for the selected coordinates and uncover grid at location
    """

    row = -1
    column = -1
    is_valid_coordinates = False

    while is_valid_coordinates is False:
        coordinates = input(
            "Please enter coordinates to try uncover an ennemy ship (eg. B5 or D1): \n"
        )
        coordinates = coordinates.upper()
        #Check if input coordinates have 2 characters
        if len(coordinates) <= 0 or len(coordinates) > 2:
            print(
                "Incorrect input. Please enter coordinates in the following format: B5\n"
            )
            continue
# Define row and column based on the 2 characters from input
        row = coordinates[0]
        column = coordinates[1]
        # Check if input coordinates is a letter and a number
        if not row.isalpha() or not column.isnumeric():
            print(
                f"Incorrect input. Please enter a letter (A-I) for row and (0-{len(GRID)}) for column."
            )
            continue
        row = ALPHABET.find(row)
        # Check if row input is within the grid size
        if not (-1 < row < GRID_SIZE):
            print(
                f"Incorrect input. Please enter a letter (A-I) for row and (0-{len(GRID)}) for column."
            )
            continue
# Convert input in integer and check if column input is within the grid size (alphabet)
        column = int(column)
        if not (-1 < column < GRID_SIZE):
            print(
                f"Incorrect input. Please enter a letter (A-I) for row and (0-{len(GRID)}) for column."
            )
            continue
# Check if location of coordinates have already been uncovered with a previous try
        if GRID[row][column] == "O" or GRID[row][column] == "X":
            print("This location is already uncovered. Try another location.")


# Uncover location based on coordinates
        if GRID[row][column] == "." or GRID[row][column] == "@":
            is_valid_coordinates = True

    return row, column


def check_if_ship_is_sunk(row, column):
    """
    Function will check if all the parts of the ship have been found and it is sunk
    """

    for ship in SHIP_POSITION:
        start_row = ship[0]
        end_row = ship[1]
        start_column = ship[2]
        end_column = ship[3]
        if start_row <= row <= end_row and start_column <= column <= end_column:
            # Check to see if ship is sunk by being covered in "X" by iterating over the grid
            for row_hit in range(start_row, end_row):
                for column_hit in range(start_column, end_column):
                    if GRID[row_hit][column_hit] != "X":
                        return False
    return True


def select_coordinates():
    """
    Function will check the grid and return the outcome of the try
    This function will validate (validate_selected_coordinates) the value prior to running
    """

    row, column = validate_selected_coordinates()
    print("")
    print("- - - - - - - - - - - - - - - - - - - ")

    # Check on grid what is located on these coordinates and print outcome
    # Decrease by 1 the number of tries left for the player regardless of outcome
    if GRID[row][column] == ".":
        print("Empty space, no ship were hit.")
        GRID[row][column] = "O"
    elif GRID[row][column] == "@":
        print("This is a hit!", end=" ")
        GRID[row][column] = "X"
        # If ship is hit, increase the count of ships sunk
        if check_if_ship_is_sunk(row, column):
            print("The ship has been sunk!")
            NUMBER_OF_SHIPS_SUNK += 1
        else:
            print("The ship has been hit!")

    TRIES_LEFT -= 1


def is_game_over():
    """
    Function to check is the game is over following conditions:
    - all ships have been sunk (player or computer)
    - player ran out of tries
    """

    if NUMBER_OF_SHIPS == NUMBER_OF_SHIPS_SUNK:
        print("Congratulations admiral! You have won the battle!")
        GAME_OVER = True
    elif TRIES_LEFT <= 0:
        GAME_OVER = True
        print("Sorry admiral, you have ran out of tries. \n")
        restart_game = input("Do you wish to try again? (Y/N)\n")
        is_valid_input_restart_game = False

        # Allow player to restart a game if the game is over
        while GAME_OVER is True and is_valid_input_restart_game is False:
            if restart_game.upper() == "N":
                print("Too bad. See you another time.")
                exit = True
                break
            elif restart_game.upper() == "Y":
                print("Fantastic!")
                break
            else:
                print("incorrect value. Please enter Y for Yes and N for No")

            if exit:
                break


def main():
    """
    Main function that will call on the other functions in order to run the game
    """

    print(INTRO)
    create_grid()

    while GAME_OVER is False:
        print_game_board_grid()
        print("There are " + str(NUMBER_OF_SHIPS - NUMBER_OF_SHIPS_SUNK) +
              " ennemy ships left.\n")
        print("You have " + str(TRIES_LEFT) + " tries left.")
        select_coordinates()
        print("- - - - - - - - - - - - - - - -")
        print("")
        is_game_over()


main()