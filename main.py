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

screen.addshape('images/darkseagreen1.gif')
screen.addshape('images/darkslategrey.gif')

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
for part in parts:
    screen.addshape(f'images/b_{part}_1x_ns.gif')
    screen.addshape(f'images/w_{part}_1x_ns.gif')

spotlight = []


def reset_spotlight():
    for t in spotlight:
        t.hideturtle()
    spotlight.clear()


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
    screen.update()



    screen.update()

    global next_turn
    next_turn = True


def player_turn(piece):

    global selected_piece_index

    if current_player == 'white':
        selected_piece_index = (white_set.index(piece))

    elif current_player == 'black':
        selected_piece_index = (black_set.index(piece))

    reset_spotlight()

    piece.vision_update(board=chessboard)

    for space in piece.vision + piece.capture_vision:
        t = Turtle(shape='circle')
        t.penup()
        t.color('black')
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
        piece.onclick(lambda x, y, p=piece: player_turn(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set)
    chessboard.update(white_set, black_set)

    # black's turn:

    next_turn = False
    current_player = 'black'

    for piece in black_set:
        piece.onclick(lambda x, y, p=piece: player_turn(p))

    while not next_turn:
        screen.update()

    chessboard.flip(white_set, black_set)
    chessboard.update(white_set, black_set)

screen.mainloop()
