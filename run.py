import random

# Global variables for the boardgames
# Global variable for the welcome message
INTRO = """
**********************************************

Welcome admiral! This is a game of battleship.
The objective is to win the battle by finding
and sinking all the ennemy's ships.
You have 20 tries to sink the 5 ennemy ships before they overrun you.

Legend:
"_" = empty space
"O" = empty location hit
"X" = part of ship that was hit

Good luck admiral!

***********************************************\n
"""
# Global variable for the alphabet
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Global variable for the grid numbers
GRID_NUMBERS = "1234567"


class Grid:

    def __init__(self, grid):
        self.grid = grid

    def print_game_board_grid(self):
        """
        Method that defines the grid:
        - Letters for the header of the columns
        - Numbers for the margin of the rows
        Iterates for each row and increment number to print by 1.
        """
        header = '   ' + '   '.join(x for x in ALPHABET[0:6])
        print(header)
        grid_numbers_to_print = 1
        for row in self.grid:
            print("%d|%s|" % (grid_numbers_to_print, "|".join(row)))
            grid_numbers_to_print += 1


class Ship:

    def __init__(self, grid):
        self.grid = grid

    def generate_ships(self):
        """
        Creates 5 ships in random location and appends the grid.
        Iterates for each ship.
        """
        for i in range(5):
            self.ship_row, self.ship_column = random.randint(
                0, 5), random.randint(0, 5)
            while self.grid[self.ship_row][self.ship_column] == " X ":
                self.ship_row, self.ship_column = random.randint(
                    0, 5), random.randint(0, 5)
            self.grid[self.ship_row][self.ship_column] = " X "
        return self.grid

    def get_coordinates_input(self):
        """
        Method to allow player to provide coordinates for the next hit.
        Data validation is done for each input.
        """
        try:
            hit_row = input("Select the next row you wish to target:\n")
            while hit_row not in GRID_NUMBERS:
                # Checks input for the row
                print(
                    "Out of bound, please select a row displayed on the grid.")
                hit_row = input("Which row do you wish to hit?\n")

            hit_column = input(
                "Please select the column letter of the ship: \n").upper()
            while hit_column not in ALPHABET:
                # Checks input for the column, translate into a number
                print("Out of bounds, please select a valid column")
                hit_column = input(
                    "Please select the column letter of the ship: \n").upper()
            return int(hit_row) - 1, ALPHABET.index(hit_column)
        except ValueError and KeyError:  # pylint: disable=W0702
            # If error, will print message and call on method again.
            print("Invalid coordinates.")
            return self.get_coordinates_input()

    def counter_numbers_of_ships_hit(self):
        """
        Checks the number of ships that have been hit for win condition.
        """
        ships_hit = 0
        for row in self.grid:
            for column in row:
                if column == " X ":
                    ships_hit += 1
        return ships_hit


def execute_game():
    """
    Function to run the game. 
    It will define the grid size and call on the 2 classes.
    It will generate the ship locations and then populate the ships
    on the Grid based on the generated coordinates.
    Will check the coordinates input and run the game logic to check outcome.
    Decreases the count of number of tries after each hit.
    """
    computer_grid = Grid([[" _ "] * 6 for i in range(6)])
    player_grid = Grid([[" _ "] * 6 for i in range(6)])
    Ship.generate_ships(computer_grid)
    # Sets limit for the game and defines how many tries the player has
    tries = 20
    while tries > 0:
        Grid.print_game_board_grid(player_grid)
        # gets player coordinates for next hit
        player_hit_row, player_hit_column = Ship.get_coordinates_input(object)
        # checks if player already hit location
        while player_grid.grid[player_hit_row][
                player_hit_column] == " O " or player_grid.grid[
                    player_hit_row][player_hit_column] == " X ":
            print("You already hit this location.")
            player_hit_row, player_hit_column = Ship.get_coordinates_input(
                object)
        # checks for hit or miss
        if computer_grid.grid[player_hit_row][player_hit_column] == " X ":
            print("You hit a ship!")
            player_grid.grid[player_hit_row][player_hit_column] = " X "
        else:
            print("Missed! You hit water.")
            player_grid.grid[player_hit_row][player_hit_column] = " O "
        # checks if player won or lost
        if Ship.counter_numbers_of_ships_hit(player_grid) == 5:
            print("Congratulations! You sunk all ennemy ships!")
            break
        else:
            tries -= 1
            print(f"You have {tries} shots left. Make them count!")
            if tries == 0:
                print("The ennemy has won. You ran out of shots")
                Grid.print_game_board_grid(player_grid)
                break


def play_again():
    """
    At the end of the game, proposes to launch a new game.
    """
    restart = input("Do you want to play another game? (Y/N")
    if restart.upper() == "Y":
        execute_game()
    if restart.upper() == "N":
        print("Thank you for playing. Hope to see you again soon.")
    else:
        print("I did not understand.")
        restart = input("Do you want to play another game? (Y/N")


def main():
    """
    Main function that calls on the class methods and run the game.
    """
    print(INTRO)
    execute_game()
    play_again()


main()
