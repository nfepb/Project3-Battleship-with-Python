from random import randint

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
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# Global variable for the grid numbers
GRID_NUMBERS = "123456789"


class Grid:

    def __init__(self, name, size, display, difficulty, ships):
        self.name = name
        self.difficulty = difficulty
        self.display = display
        self.size = size
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
        if (player_difficulty_lvl == "1" or player_difficulty_lvl == "2"
                or player_difficulty_lvl == "3"):
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

    def generate_game_board_grid(self, size):
        grid_separators = [[' _ ' for x in range(self.size)]
                           for y in range(self.size)]

        self.display = grid_separators

    def position_ships_on_board_grid(self):
        for ship in self.ships:
            self.display[ship[0]][ship[1]] = ' @ '

    def print_grid_with_ships(self, size):
        grid_numbers_to_print = 1
        header = '      '.join(x for x in ALPHABET[0:size])
        print('     ' + header.upper())
        for row in self.display:
            print(str(grid_numbers_to_print) + ' ' + str(row))
            grid_numbers_to_print += 1
        print(' \n')
        print('##########################################')


class Player:

    def __init__(self, name, tries):
        self.name = name
        self.tries_made = tries

    def get_player_name(self):
        player_name = input("Please enter your name: \n")
        while player_name.isspace(
        ) or not player_name or player_name == "Computer":
            print("Your name cannot be blank or Computer," +
                  "please provide a valid name!\n")
            player_name = input("Please enter your name: \n")

        self.name = player_name

    def input_hit_location(self, size, ships, display):
        if self.name == "Computer":
            while True:
                computer_column = randint(0, size - 1)
                computer_row = randint(0, size - 1)
                if self.verify_outcome_coordinates(
                        size, [computer_column, computer_row], ships, display):
                    continue
                self.tries_made.append([computer_column, computer_row])
                self.display_outcome(ships, display)
                break

        else:
            try:
                row_response_location = input(
                    "Please select the row for your next hit based" +
                    " on the numbers displayed on your grid.\n")
                while (row_response_location < 0
                       or row_response_location > size - 1):
                    print("Incorrect input. Please enter a row based " +
                          "on the numbers displayed on the grid.")

                column_response_location = input(
                    "Please select the column for your next hit based " +
                    "on the letters displayed on your grid.\n")
                while column_response_location not in ALPHABET[0:size]:
                    print(
                        "Please enter one of the letters displayed on the grid"
                    )
                row_response_location = int(row_response_location) - 1
                column_response_location = ALPHABET.index(
                    column_response_location)
                return row_response_location, column_response_location

            except ValueError and KeyError:
                print("Invalid coordinates.")
                return self.tries_made(
                    [row_response_location, column_response_location])

    def verify_outcome_coordinates(self, size, answer, ships, display):
        if answer in self.tries_made:
            if self.name != "Computer":
                print("You have already uncovered this location," +
                      " please select new coordinate.")
            return True

        return False


def display_outcome(self, ships, display):
    for x, y in ships:
        if self.tries_made[-1] == [x, y]:
            print(f"\n{self.name} guessed: ({self.tries_made[0][0]}" +
                  f",{self.tries_made[-1][1]})")
            print(f"{self.username} scores a direct hit!!!")
            display[x][y] = " X "
            return True

    display[self.tries_made[-1][0]][self.tries_made[-1][1]] = " O "
    print(f"{self.name} guessed: ({self.tries_made[-1][0]}," +
          f"{self.tries_made[-1][1]})")
    print(f"{self.name} hits the water...\n")


def execute_game(player, computer, player_board, computer_board):
    player_board.print_grid_with_ships()
    computer_board.print_grid_with_ships()
    player.input_hit_location(player_board.size, computer_board.ships,
                              computer_board.display)
    computer.input_hit_location(computer_board.size, player_board.ships,
                                player_board.display)


def main():
    print(INTRO)
    player = Player("", [])
    computer = Player("Computer", [])
    player_board = Grid(player.name, 0, 0, [], [])
    board_size = player_board.input_difficulty_level_for_board_size()
    player_board.generate_game_board_grid(board_size)
    player_board.generate_ship_location()
    player_board.position_ships_on_board_grid()
    player_board.print_grid_with_ships(board_size)

    computer_board = Grid(computer.name, board_size, 0, [], [])
    computer_board.generate_game_board_grid(board_size)
    computer_board.generate_ship_location()
    computer_board.print_grid_with_ships(board_size)
    execute_game(player, computer, player_board, computer_board)


main()