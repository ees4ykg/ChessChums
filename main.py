# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar
import numpy as np
import time
from Board import Board
from pieces import *
from turtle import Screen

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
screen = Screen()
screen.addshape('images/darkseagreen1.gif')
screen.addshape('images/darkslategrey.gif')

for part in parts:
    screen.addshape(f'images/b_{part}_1x_ns.gif')
    screen.addshape(f'images/w_{part}_1x_ns.gif')

screen.tracer(0, 0)
chessboard = Board()
w_pawn = Pawn(colour="w", co_ords=chessboard.squares["a2"]["co_ordinates"])


screen.update()

time.sleep(1)
w_pawn.movement()

screen.update()

time.sleep(1)
w_pawn.capture("right")

screen.update()
print(chessboard.squares)
chessboard.flip()
print(chessboard.squares)

screen.mainloop()
