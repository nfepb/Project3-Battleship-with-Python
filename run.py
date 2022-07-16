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
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# Global variable for the grid numbers
GRID_NUMBERS = "123456789"


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
            print((ship_position))

        list_ship_position = list(ship_position)
        self.ships = list_ship_position

    def generate_game_board_grid(self, size):
        grid_separators = [[' . ' for x in range(self.size)]
                           for y in range(self.size)]

        self.display = grid_separators

    def position_ships_on_board_grid(self):
        for ship in self.ships:
            self.display[ship[0]][ship[1]] = ' @ '

    def print_grid_with_ships(self, size):
        grid_numbers_to_print = 1
        header = '      '.join(x for x in ALPHABET[0:size])
        print('     ' + header)
        for row in self.display:
            print(str(grid_numbers_to_print) + ' ' + str(row))
            grid_numbers_to_print += 1


def main():
    print(INTRO)
    player_board = Grid(0, 0, [], [], [])
    board_size = player_board.input_difficulty_level_for_board_size()
    player_board.generate_game_board_grid(board_size)
    player_board.generate_ship_location()
    player_board.position_ships_on_board_grid()
    player_board.print_grid_with_ships(board_size)

    computer_board = Grid(0, 0, [], [], [])
    computer_board.generate_game_board_grid(board_size)
    computer_board.generate_ship_location()
    #to be removed when working:
    computer_board.position_ships_on_board_grid()
    computer_board.print_grid_with_ships(board_size)


main()