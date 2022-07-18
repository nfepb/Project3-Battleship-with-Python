![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

Everyone knows the game of Battleship and is familiar with the rules. You will find here a representation of the Battleship game run through a Python terminal. This terminal is running on Heroku.

The purpose of the game is for the users to find all the computer ships (5 ships) before the player runs out of tries/bullets/guesses. Each ship occupies one square on the grid.

[View the live version of the programme running on Heroku](https://project3-battleship-project.herokuapp.com/)

## How to play
Battleship is a turn-based naval strategy game. Originally known as a pencil and paper game, the game has evolved in its format and has its own variations. You can find out more about this game and its history on its [Wikipedia page](https://en.wikipedia.org/wiki/Battleship_(game)#:~:text=Battleship%20(also%20known%20as%20Battleships,concealed%20from%20the%20other%20player.).

In this version of the game, the player sees the guess board. This is a one player game where the player has to try and sink all the ennemy ships before he is running out of tries. 

Each turn, the user will be select to select a row and a column that will work as coordinates to target a location on the grid. The outcome of this selection will display a "O" for a missed shot, or water, or a "X" for a hit. Locations that have not been hit yet are marked on the grid by a "_".

## Features

### Implemented features

- Introduction message explaining the programme, the game, and the winning conditions:

![intro message](assets/images/screenshot-intro-message.png)

- The grid with the numbers for the rows and the letters for the columns to guide the player in how to select locations. The 5 ennemy ships are randomly generated on the grid (but of course not displayed):

![opening grid](assets/images/screenshot-opening-grid.png)

- Input message to invite the player to select the next coordinates for the next try:

![input coordinates](assets/images/screenshot-input-row-and-column.png)

- Logic to verify the input for rows and columns.
    - Verifies if the row input is an integer.
    - Converts the row input in coordinates (substracts 1)
    - Verifies if the column is a letter.
    - Converts the letter in a number.

![wrong coordinates]()

- Outcome logic after input has been validated
    - Verifies if the selected coordinates have not been previously hit.
    - Checks on the grid if an ennemy ship is located there.
    - Checks on the grid if it is an empty location. 
    - Reduces the count of tries left by one.




## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

## Fixed bugs:

* Creating a grid in Python [Stackoverflow](https://stackoverflow.com/questions/40566675/how-to-make-a-board-in-python)

* Pylance kept giving an error. Disabled pylance in the except statement thanks to a solved question on [Stackexchange](https://stackoverflow.com/questions/53408630/catching-all-exceptions-without-pylint-error)

* Issues deploying to Heroku with the main module. Random from 