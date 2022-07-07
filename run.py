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


ship_row = random_row(board)
ship_col = random_col(board)
print(f"x is {ship_col}, and y is {ship_row}")
