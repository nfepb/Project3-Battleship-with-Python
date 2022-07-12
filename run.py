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
# Global variable for the grid size
GRID_SIZE = 10


class Grid:

    def __init__(self, size, difficulty, gameboard):
        self.grid = grid
        self.difficulty = difficulty
        self.size = size
        self.gameboard = gameboard

    def input_difficulty_level_for_board_size(self):
        difficulty_level = {'1': 5, '2': 6, '3': 8}
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

        self.size = difficulty_level[player_difficulty_lvl]

    def validate_input_difficulty_level(self, player_difficulty_lvl):
        if player_difficulty_lvl == "1" or player_difficulty_lvl == "2" or player_difficulty_lvl == "3":
            return int(player_difficulty_lvl) - 1
        else:
            print("Incorrect value. Please try again.")

    def print_game_board_grid(self, GRID, size, player_difficulty_lvl, gameboard):
        grid_letters_to_print = ALPHABET[0:len(size) + 1]
        grid_numbers_to_print = GRID_NUMBERS[0:len(size) + 1]

        for x in range(player_difficulty_lvl):
            gameboard.append([". |"] * difficulty_level) #how to call on previous variable l.40
            print(" ", " ".join(grid_numbers_to_print))
            for number, row in zip(grid_letters_to_print, gameboard):
                print(number, "".join(row))



def main():
    print(INTRO)
    grid_player = Grid([], [])
    grid_player.input_difficulty_level_for_board_size()
    grid_player.print_game_board_grid()


main()