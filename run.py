# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
Battleship game written in python. First iteration will be
basic version, drawing a board and allowing a user to guess
the location of randomly placed ships. Building on that to
allow for the user the place their own ships. Then adding
an computer player to create a 2 player game.
"""

from random import randint
# used to create the random co ordinates
from time import sleep
# used to create pauses in the game

# start by defining a 10 x 10 game board
board = []

for num in range(0,10):
    board.append(["O"] * 10)
    # the "O" represents a space on the board multiplied
    # by a predetermined board size, in this case 10.


def print_board(board):
    """
    create a function that generates the game board
    """

    for row in board:
        print(" ".join(row))


print_board(board)


def random_row(board):
    """
    create a function that randomly selects a row location
    and returns the x co-ordinate
    """

    return randint(0, len(board) - 1)


def random_col(board):
    """
    create a function that randomly selects a row location
    and returns the y co-ordinate
    """

    return randint(0, len(board[0]) - 1)

# assign the random x,y values to the ship row and column
# to generate a random 1x1 ship.
ship_row = random_row(board)
ship_col = random_col(board)
# print out the ship for debugging.
print(f"x is {ship_col}, and y is {ship_row}")

# ask the user choose which row(x) and column(y)
# to fire a missle at.
guess_row = int(input("Which row would you like to fire on: "))
sleep(1)    # create a pause before asking for next co-ordinate
guess_col = int(input("Which column would you like to fire on: "))

# test to see whether the guess was a hit or miss.
if guess_row == ship_row and guess_col == ship_col:
    guess_row = "H"
    guess_col = "H"
    print("You sank my Battleship!")
elif guess_row == ship_row or guess_col == ship_col:
    print("You hit my Battleship!")
else:
    guess_col = "X"
    guess_row = "X"
    print("You missed my Battleship!")
    print_board(board)
