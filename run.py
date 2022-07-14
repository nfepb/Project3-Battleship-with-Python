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
GRID = []
# Global variable for the alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Global variable for the grid numbers
GRID_NUMBERS = "123456789"
# Global variable for the number of tries remaining to win the game
TRIES_LEFT = 50


class Grid:

    def __init__(self, size, display, difficulty, boardgame, ships):
        self.difficulty = difficulty
        self.display = display
        self.size = size
        self.boardgame = boardgame
        self.ships = ships

    def input_difficulty_level_for_board_size(self):
        difficulty_level = [5, 6, 8]
        while True:
            print("[1]. Easy")
            print("[2]. Medium")
            print("[3]. Hard")
            player_difficulty_lvl = input(
                "Please select the board size by selecting a difficulty 1-3:\n"
            )
            if self.validate_input_difficulty_level(player_difficulty_lvl):
                print(f"You have chosen {player_difficulty_lvl}\n")
                break

        self.size = int(difficulty_level[int(player_difficulty_lvl) - 1])

        return self.size

    def validate_input_difficulty_level(self, player_difficulty_lvl):
        if player_difficulty_lvl == "1" or player_difficulty_lvl == "2" or player_difficulty_lvl == "3":
            return int(player_difficulty_lvl) - 1
        else:
            print("Incorrect value. Please try again.")

    def generate_ship_location(self):
        ship_position = set()
        while len(ship_position) < 5:
            random_location = (randint(0, self.size - 1),
                               randint(0, self.size - 1))
            ship_position.add(random_location)

        list_ship_position = list(ship_position)
        self.ships = list_ship_position

    def generate_game_board_grid(self):
        grid_separators = [["| . |" for x in range(self.size)]
                           for y in range(self.size)]

        self.display = grid_separators

    def position_ships_on_board_grid(self):
        print(" ", " ".join(GRID_NUMBERS))
        for ship in self.ships:
            self.display[ship[0]][ship[1]] = "@"

    def print_grid_with_ships(self, size):
        grid_letters_to_print = ALPHABET[0:size + 1]
        print(grid_letters_to_print)
        for cell in self.display:
            print(cell)


def main():
    print(INTRO)
    grid1 = Grid(0, 0, [], [], [])
    board_size = grid1.input_difficulty_level_for_board_size()
    grid1.generate_game_board_grid(board_size)
    grid1.generate_ship_location()
    grid1.position_ships_on_board_grid()

    grid1.print_grid_with_ships()


main()