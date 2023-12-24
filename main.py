# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar
import time
from Board import *
from pieces import *
from turtle import Screen, Turtle, setup
import turtle
import tkinter
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

turtle.title('ChessChums')
img = tkinter.Image("photo", file=os.path.join(script_directory, "images/b_knight_1x_ns.gif"))
turtle._Screen._root.iconphoto(True, img)


setup(700, 700)
screen = Screen()

screen.screensize(675, 675)

# Set the custom center coordinates
custom_center_x = (-12.5 + 300) - (35 / 2 ** 0.5 + 600) / 2
custom_center_y = (-12.5 + 300) - (35 / 2 ** 0.5 + 600) / 2

# Calculate the range for setworldcoordinates
left_bound = custom_center_x - screen.window_width() // 2
right_bound = custom_center_x + screen.window_width() // 2
bottom_bound = custom_center_y - screen.window_height() // 2
top_bound = custom_center_y + screen.window_height() // 2

# Set the world coordinates with the custom center
screen.setworldcoordinates(left_bound, bottom_bound, right_bound, top_bound)


screen.bgcolor('grey')

screen.addshape(os.path.join(script_directory, 'images/darkseagreen1.gif'))
screen.addshape(os.path.join(script_directory, 'images/darkslategrey.gif'))
screen.addshape(os.path.join(script_directory, "images/cross.gif"))
screen.addshape(os.path.join(script_directory, "images/greycross.gif"))
screen.addshape(os.path.join(script_directory, 'images/greycircle.gif'))
screen.addshape(os.path.join(script_directory, 'images/highlighter.gif'))

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
for part in parts:
    screen.addshape(os.path.join(script_directory, f'images/b_{part}_1x_ns.gif'))
    screen.addshape(os.path.join(script_directory, f'images/w_{part}_1x_ns.gif'))

spotlight = []
highlighter = []


def reset_spotlight():
    for t in spotlight:
        t.hideturtle()
    spotlight.clear()


def reset_highlighter():
    for t in highlighter:
        t.hideturtle()
    highlighter.clear()


def reset_lights(x, y):
    reset_highlighter()
    reset_spotlight()
    screen.update()

selected_piece_index = None


def spot_clicked(spot, player):
    if player == 'white':
        white_set[selected_piece_index].setpos(spot.xcor(), spot.ycor())
        white_set[selected_piece_index].has_moved = True

        for piece in black_set:
            piece.onclick(None)
            if spot.pos() == piece.pos():
                piece.hideturtle()
                black_set.remove(piece)
                break

    elif player == 'black':
        black_set[selected_piece_index].setpos(spot.xcor(), spot.ycor())
        black_set[selected_piece_index].has_moved = True

        for piece in white_set:
            piece.onclick(None)
            if spot.pos() == piece.pos():
                piece.hideturtle()
                white_set.remove(piece)
                break

    reset_spotlight()

    h = Turtle(shape=os.path.join(script_directory, 'images/highlighter.gif'))
    h.penup()
    h.setpos(spot.xcor(), spot.ycor())
    highlighter.append(h)

    screen.update()



    screen.update()

    global next_turn
    next_turn = True


def piece_clicked(piece):
    global selected_piece_index

    if current_player == 'white':
        selected_piece_index = (white_set.index(piece))

    elif current_player == 'black':
        selected_piece_index = (black_set.index(piece))

    reset_spotlight()
    reset_highlighter()

    h = Turtle(shape=os.path.join(script_directory, 'images/highlighter.gif'))
    h.penup()
    h.setpos(piece.xcor(), piece.ycor())
    highlighter.append(h)
    for h in highlighter:
        h.onclick(fun=reset_lights)

    piece.vision_update(board=chessboard)

    for space in piece.vision + piece.capture_vision:
        t = Turtle(shape=os.path.join(script_directory, 'images/greycircle.gif'))
        t.penup()
        t.shapesize(2.5)
        t.setpos(space)
        spotlight.append(t)

    screen.update()
    for spot in spotlight:
        spot.onclick(lambda x, y, s=spot, p=current_player: spot_clicked(s, p))


screen.tracer(0, 0)

chessboard = Board()


white_set = create_piece_set(chessboard, 'w')
black_set = create_piece_set(chessboard, 'b')

screen.update()

while True:
    # white's turn:
    next_turn = False
    current_player = 'white'

    for piece in white_set:
        piece.onclick(lambda x, y, p=piece: piece_clicked(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set, highlighter)
    chessboard.update(white_set, black_set)

    # black's turn:

    next_turn = False
    current_player = 'black'

    for piece in black_set:
        piece.onclick(lambda x, y, p=piece: piece_clicked(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set, highlighter)
    chessboard.update(white_set, black_set)

screen.mainloop()
