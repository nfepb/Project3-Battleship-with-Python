import random

# Global variables for the boardgames
# Global variable for the welcome message
INTRO = """
Welcome admiral! This is a game of battleship.
The objective is to win the battle by finding 
and sinking all the ennemy's ships.
You have 50 tries to sink the ennemy fleet before they overrun you.

Legend:
"." = empty space
"O" = empty location hit
"@" = part of ship on player game board
"X" = part of ship that was hit

Good luck admiral! \n
"""
# Global variable for the alphabet
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# Global variable for the grid numbers
GRID_NUMBERS = "12345678"


class Grid:

    def __init__(self, grid):
        self.grid = grid

    def print_game_board_grid(self):
        header = '   ' + '   '.join(x for x in ALPHABET[0:7])
        print(header)
        grid_numbers_to_print = 1
        for row in self.grid:
            print("%d|%s|" % (grid_numbers_to_print, "|".join(row)))
            grid_numbers_to_print += 1


class Ship:

    def __init__(self, grid):
        self.grid = grid

    def generate_ships(self):
        # creates 5 ships in random location and appends the grid
        for i in range(5):
            self.ship_row, self.ship_column = random.randint(
                0, 6), random.randint(0, 6)
            while self.grid[self.ship_row][self.ship_column] == " @ ":
                self.ship_row, self.ship_column = random.randint(
                    0, 6), random.randint(0, 6)
        self.grid[self.ship_row][self.ship_column] = " @ "
        return self.grid

    def get_coordinates_input(self):
        try:
            hit_row = input("Select the next row you wish to target:\n")
            while hit_row not in GRID_NUMBERS:
                print(
                    "Out of bound, please select a row displayed on the grid.")
                hit_row = input("Which row do you wish to hit?\n")

            hit_column = input(
                "Please select the column letter of the ship: \n").upper()
            while hit_column not in ALPHABET:
                print("Out of bounds, please select a valid column")
                hit_column = input(
                    "Please select the column letter of the ship: \n").upper()
            return int(hit_row) - 1, ALPHABET.index(hit_column)
        except ValueError and KeyError:
            print("Invalid coordinates.")
            return self.get_coordinates_input()

    def counter_numbers_of_ships_hit(self):
        ships_hit = 0
        for row in self.grid:
            for column in row:
                if column == " X ":
                    ships_hit += 1
            return ships_hit


def execute_game():
    computer_grid = Grid([[" _ "] * 7 for i in range(7)])
    player_grid = Grid([[" _ "] * 7 for i in range(7)])
    Ship.generate_ships(computer_grid)
    # Sets limit for the game and defines how many tries the player has
    tries = 13
    while tries > 0:
        Grid.print_game_board_grid(player_grid)
        # gets player coordinates for next hit
        player_hit_row, player_hit_column = Ship.get_coordinates_input(object)
        # checks if player already hit location
        while player_grid.grid[player_hit_row][
                player_hit_column] == " _ " or player_grid.grid[
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


def main():
    print(INTRO)
    execute_game()


main()