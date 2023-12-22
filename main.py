# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar
import time
from Board import *
from pieces import *
from turtle import Screen, Turtle


screen = Screen()

screen.addshape('images/darkseagreen1.gif')
screen.addshape('images/darkslategrey.gif')

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
for part in parts:
    screen.addshape(f'images/b_{part}_1x_ns.gif')
    screen.addshape(f'images/w_{part}_1x_ns.gif')


spotlight = []


def display_options(piece):

    for t in spotlight:
        t.hideturtle()
    spotlight.clear()

    piece.vision_update(board=chessboard)

    for space in piece.vision + piece.capture_vision:
        t = Turtle(shape='circle')
        t.penup()
        t.color('black')
        t.shapesize(2.5)
        t.setpos(space)
        spotlight.append(t)

    screen.update()


screen.tracer(0, 0)
chessboard = Board()
w_pawn1 = Pawn(colour="w", opposite_colour='b', co_ords=chessboard.squares["d2"]["co_ordinates"], board=chessboard)
w_pawn2 = Pawn(colour="w", opposite_colour='b', co_ords=chessboard.squares["d7"]["co_ordinates"], board=chessboard)
b_pawn1 = Pawn(colour="b", opposite_colour='w', co_ords=chessboard.squares["a2"]["co_ordinates"], board=chessboard)
b_pawn2 = Pawn(colour="b", opposite_colour='w', co_ords=chessboard.squares["c3"]["co_ordinates"], board=chessboard)
b_pawn3 = Pawn(colour="b", opposite_colour='w', co_ords=chessboard.squares["f4"]["co_ordinates"], board=chessboard)
w_rook1 = Rook(colour="w", opposite_colour="b", co_ords=chessboard.squares["d4"]["co_ordinates"], board=chessboard)

screen.update()

w_rook1.onclick(lambda x, y: display_options(w_rook1))
w_pawn1.onclick(lambda x, y: display_options(w_pawn1))

screen.update()
screen.mainloop()
