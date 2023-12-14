# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar

from Board import board
from turtle import Screen

chessboard = board()
screen = Screen()
screen.addshape()
print(chessboard.squares)

screen.exitonclick()
