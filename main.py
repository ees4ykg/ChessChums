# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar
import time
from board import *
from pieces import *
from rules import *
from turtle import Screen, Turtle, setup
import turtle
import tkinter
import os
import winsound

script_directory = os.path.dirname(os.path.abspath(__file__))

turtle.title('ChessChums')
img = tkinter.Image("photo", file=os.path.join(script_directory, "images/icon.gif"))
turtle._Screen._root.iconphoto(True, img)

setup(700, 900)
screen = Screen()

screen.screensize(700, 800)

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
screen.addshape(os.path.join(script_directory, 'images/checkmate.gif'))

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
    reset_spotlight()
    
    if player == 'white':
        white_set[selected_piece_index].setpos(spot.xcor(), spot.ycor())
        white_set[selected_piece_index].has_moved = True

        for piece in black_set:
            piece.onclick(None)
            if spot.pos() == piece.pos():
                piece.hideturtle()
                black_set.remove(piece)
                winsound.PlaySound("thud", winsound.SND_FILENAME)
                break

        promotion(white_set[selected_piece_index], white_set, chessboard, screen)

    elif player == 'black':
        black_set[selected_piece_index].setpos(spot.xcor(), spot.ycor())
        black_set[selected_piece_index].has_moved = True

        for piece in white_set:
            piece.onclick(None)
            if spot.pos() == piece.pos():
                piece.hideturtle()
                white_set.remove(piece)
                winsound.PlaySound("thud", winsound.SND_FILENAME)
                break

        promotion(black_set[selected_piece_index], black_set, chessboard, screen)

    h = Turtle(shape=os.path.join(script_directory, 'images/highlighter.gif'))
    h.penup()
    h.setpos(spot.xcor(), spot.ycor())
    highlighter.append(h)

    
    screen.update()
    winsound.PlaySound("click", winsound.SND_FILENAME)
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

        if {'piece': tuple(piece.pos()), 'spot': tuple(space)} in illegal_moves:
            pass

        else:

            t = Turtle(os.path.join(script_directory, 'images/greycircle.gif'))
            t.penup()
            t.shapesize(2.5)
            t.setpos(space)
            spotlight.append(t)

    screen.update()
    for spot in spotlight:
        spot.onclick(lambda x, y, s=spot, p=current_player: spot_clicked(s, p))


screen.tracer(0, 0)

chessboard = Board(draw=True)

white_set = create_piece_set(chessboard, 'w')
black_set = create_piece_set(chessboard, 'b')

screen.update()

while True:
    # white's turn:

    next_turn = False
    current_player = 'white'
    illegal_moves = find_illegal_moves(white_set, black_set, chessboard)

    if len(all_moves(white_set, chessboard)) == len(illegal_moves):
        winner = 'black'
        break

    if in_check(chessboard, white_set, black_set):
        print('CHECK')

    for piece in white_set:
        piece.onclick(lambda x, y, p=piece: piece_clicked(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set, highlighter)
    chessboard.update(white_set, black_set)

    # black's turn:

    next_turn = False
    current_player = 'black'
    illegal_moves = find_illegal_moves(black_set, white_set, chessboard)

    if len(all_moves(black_set, chessboard)) == len(illegal_moves):
        winner = 'white'
        break

    if in_check(chessboard, white_set, black_set):
        print('CHECK')
    screen.update()

    for piece in black_set:
        piece.onclick(lambda x, y, p=piece: piece_clicked(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set, highlighter)
    chessboard.update(white_set, black_set)

print(f'CHECKMATE by {winner}')
image = Turtle(shape=os.path.join(script_directory, 'images/checkmate.gif'))
image.penup()
image.setpos(-327.5, 300 - 5)
image.write('CHECKMATE', font=('Arial', 45, 'bold'))
image.setpos(-322.5, 300)
image.write('CHECKMATE', font=('Arial', 45, 'bold'))
image.setpos(160, 350)
# image2 = Turtle(shape=os.path.join(script_directory, 'images/checkmate.gif'))
# image2.penup()
# image2.setpos(170 - 5, 350)
chessboard.flip(white_set, black_set, highlighter)
screen.update()
screen.mainloop()
