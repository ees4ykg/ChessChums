# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar
import numpy as np
import time
from Board import *
from pieces import *
from turtle import Screen, Turtle
from functools import partial


screen = Screen()

screen.addshape('images/darkseagreen1.gif')
screen.addshape('images/darkslategrey.gif')

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
for part in parts:
    screen.addshape(f'images/b_{part}_1x_ns.gif')
    screen.addshape(f'images/w_{part}_1x_ns.gif')


def display_options(piece):
    spotlight = []
    for space in piece.vision + piece.capture_vision:
        t = Turtle(shape='circle')
        t.penup()
        t.color('white')
        t.shapesize(2.5)
        t.setpos(space)
        spotlight.append(t)


#screen.tracer(0, 0)
chessboard = Board()
w_pawn = Pawn(colour="w", opposite_colour='b', co_ords=chessboard.squares["d2"]["co_ordinates"], board=chessboard)
b_pawn1 = Pawn(colour="b", opposite_colour='w', co_ords=chessboard.squares["e3"]["co_ordinates"], board=chessboard)
b_pawn2 = Pawn(colour="b", opposite_colour='w', co_ords=chessboard.squares["c3"]["co_ordinates"], board=chessboard)

w_pawn.vision_update(board=chessboard)

screen.update()

w_pawn.onclick(lambda x, y: display_options(w_pawn))


screen.update()

screen.mainloop()
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