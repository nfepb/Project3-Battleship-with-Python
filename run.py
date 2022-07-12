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
# Global variable for the alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Global variable for the grid size
GRID_SIZE = 10

class Grid:
    def __init__(self, size, grid):
        self.grid = grid 
        self.size = size

    def input_difficulty_level_for_board_size(self):
        difficulty_level = {'Easy': 5, 'Medium': 6, 'Hard': 8}
        while True:
            print("[1]. Easy")
            print("[2]. Medium")
            print("[3]. Hard")
            player_difficulty_lvl = input("Please select the board size by selecting a difficulty 1-3:\n")
            if self.validate_input_difficulty_level(player_difficulty_lvl):
                print(f"You have chosen {player_difficulty_lvl}\n")
                break
        
        self.size = difficulty_level[player_difficulty_lvl]
    
    def validate_input_difficulty_level(self, player_difficulty_lvl):
        if player_difficulty_lvl == "1" or player_difficulty_lvl == "2" or player_difficulty_lvl == "3":
            return int(player_difficulty_lvl) - 1
        else:
            print("Incorrect value. Please enter a difficulty level 1-3.")

        
    def print_game_board_grid(self, size):
        grid_letters_to_print = ALPHABET[0:len(GRID) + 1]
        grid_separators = [[" |" for x in range(self.size)] for y in range(self.size)]
        print(grid_letters_to_print)
        print(grid_separators)

def main():
    print(INTRO)
    input_difficulty_level_for_board_size()
    print_game_board_grid()

main()
