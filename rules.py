# python -m nuitka --standalone --follow-imports --windows-icon-from-ico=icon.ico --disable-console --enable-plugin=tk-inter main.py
from board import Board
from pieces import *
from turtle import Turtle
import os


script_directory = os.path.dirname(os.path.abspath(__file__))


def in_check(board, current_player, opponent):
    # loop through every piece of the previous players turn and check if opponents king is in the capture vision
    # must  run at the start of the current players turn
    board.flip(current_player, opponent, [])
    board.update(current_player, opponent)

    checked = False
    for piece in opponent:
        piece.vision_update(board)
        for square in piece.capture_vision:
            square_piece = board.squares[board.squares_reversed[f'{square}']]['piece']
            if square_piece == f'{piece.opposite_colour}_king':
                # Then current player is in check
                checked = True

    board.flip(current_player, opponent, [])
    board.update(current_player, opponent)

    return checked


def create_virtual_set(set):
    virtual_set = []
    for piece in set:
        if piece.name == 'pawn':
            virtual_set.append(Pawn(piece.colour, piece.pos(), virtual_board, piece.has_moved))
        elif piece.name == 'rook':
            virtual_set.append(Rook(piece.colour, piece.pos(), virtual_board, piece.has_moved))
        elif piece.name == 'bishop':
            virtual_set.append(Bishop(piece.colour, piece.pos(), virtual_board, piece.has_moved))
        elif piece.name == 'knight':
            virtual_set.append(Knight(piece.colour, piece.pos(), virtual_board, piece.has_moved))
        elif piece.name == 'king':
            virtual_set.append(King(piece.colour, piece.pos(), virtual_board, piece.has_moved))
        elif piece.name == 'queen':
            virtual_set.append(Queen(piece.colour, piece.pos(), virtual_board, piece.has_moved))
    for t in virtual_set:
        t.shape('circle')
        t.hideturtle()
    return virtual_set


virtual_board = Board(draw=False)


def find_illegal_moves(current_player, opponent, board):
    illegal_moves = []

    if current_player[0].colour == 'b' and not virtual_board.reversed:
        virtual_board.flip([], [], [])
    virtual_board.update(current_player, opponent)

    virtual_player = create_virtual_set(current_player)
    virtual_opponent = create_virtual_set(opponent)
    virtual_board.update(virtual_player, virtual_opponent)

    piece_index = 0
    while piece_index <= len(current_player) - 1:

        virtual_player[piece_index].vision_update(board)

        for spot in virtual_player[piece_index].capture_vision + virtual_player[piece_index].vision:
            piece_position = tuple(virtual_player[piece_index].pos())

            virtual_player[piece_index].setpos(spot[0], spot[1])

            for virtual_piece in virtual_opponent[:]:
                if virtual_piece.pos() == (spot[0], spot[1]):
                    virtual_opponent.remove(virtual_piece)

            if in_check(virtual_board, virtual_player, virtual_opponent):
                illegal_moves.append({'piece': piece_position, 'spot': spot})

            for virtual_piece in virtual_opponent + virtual_player:
                virtual_piece.hideturtle()
            virtual_player.clear()
            virtual_opponent.clear()
            virtual_opponent = create_virtual_set(opponent)
            virtual_player = create_virtual_set(current_player)
            for virtual_piece in virtual_opponent + virtual_player:
                virtual_piece.hideturtle()

        piece_index += 1

    for virtual_piece in virtual_player + virtual_opponent:
        virtual_piece.hideturtle()

    return illegal_moves


selected = False


def promotion_piece(piece, player_set, board, selection):
    if selection == 'rook':
        player_set.append(Rook(piece.colour, tuple((piece.xcor(), 250)), board, True))
    elif selection == 'queen':
        player_set.append(Queen(piece.colour, tuple((piece.xcor(), 250)), board, True))
    elif selection == 'knight':
        player_set.append(Knight(piece.colour, tuple((piece.xcor(), 250)), board, True))
    elif selection == 'bishop':
        player_set.append(Bishop(piece.colour, tuple((piece.xcor(), 250)), board, True))
    global selected
    selected = True


def promotion(piece, player_set, board, screen):
    if piece.name == 'pawn' and piece.ycor() == 250:
        global selected
        selected = False
        q = Turtle(os.path.join(script_directory, f'images/{piece.colour}_queen_1x_ns.gif'))
        q.penup()
        q.setpos(piece.xcor() - 37.5, piece.ycor() + 150)
        q.onclick(lambda x, y, p=piece, sel='queen', ps=player_set: promotion_piece(p, ps, board, sel))
        r = Turtle(os.path.join(script_directory, f'images/{piece.colour}_rook_1x_ns.gif'))
        r.penup()
        r.setpos(piece.xcor() + 37.5, piece.ycor() + 150)
        r.onclick(lambda x, y, p=piece, sel='rook', ps=player_set: promotion_piece(p, ps, board, sel))
        k = Turtle(os.path.join(script_directory, f'images/{piece.colour}_knight_1x_ns.gif'))
        k.penup()
        k.setpos(piece.xcor() - 37.5, piece.ycor() + 75)
        k.onclick(lambda x, y, p=piece, sel='knight', ps=player_set: promotion_piece(p, ps, board, sel))
        b = Turtle(os.path.join(script_directory, f'images/{piece.colour}_bishop_1x_ns.gif'))
        b.penup()
        b.setpos(piece.xcor() + 37.5, piece.ycor() + 75)
        b.onclick(lambda x, y, p=piece, sel='bishop', ps=player_set: promotion_piece(p, ps, board, sel))
        selections = [q, r, k, b]
        while not selected:
            screen.update()
        for s in selections:
            s.hideturtle()
        piece.hideturtle()
        player_set.remove(piece)


def all_moves(player, board):
    moves = []
    for piece in player:
        piece.vision_update(board)
        for space in piece.vision + piece.capture_vision:
            moves.append(space)

    return moves


def show_castling(king, player, board):
    special_spaces = []

    if player[0].colour == 'b':

        if not king.has_moved and board.squares['h8']['piece'] == 'b_rook':
            for piece in player:
                if tuple(piece.pos()) == (-275, -275) and not piece.has_moved:
                    gap_squares = ['f8', 'g8']
                    gap_pieces = [board.squares[s]['piece'] for s in gap_squares]
                    if gap_pieces == ['empty', 'empty']:
                        special_spaces.append((-200, -275))

        if not king.has_moved and board.squares['a8']['piece'] == 'b_rook':
            for piece in player:
                if tuple(piece.pos()) == (250, -275) and not piece.has_moved:
                    gap_squares = ['b8', 'c8', 'd8']
                    gap_pieces = [board.squares[s]['piece'] for s in gap_squares]
                    if gap_pieces == ['empty', 'empty', 'empty']:
                        special_spaces.append((100, -275))

    elif player[0].colour == 'w':

        if not king.has_moved and board.squares['a1']['piece'] == 'w_rook':
            for piece in player:
                if tuple(piece.pos()) == (-275, -275) and not piece.has_moved:
                    gap_squares = ['b1', 'c1', 'd1']
                    gap_pieces = [board.squares[s]['piece'] for s in gap_squares]
                    if gap_pieces == ['empty', 'empty', 'empty']:
                        special_spaces.append((-125, -275))

        if not king.has_moved and board.squares['h1']['piece'] == 'w_rook':
            for piece in player:
                if tuple(piece.pos()) == (250, -275) and not piece.has_moved:
                    gap_squares = ['f1', 'g1']
                    gap_pieces = [board.squares[s]['piece'] for s in gap_squares]
                    if gap_pieces == ['empty', 'empty']:
                        special_spaces.append((175, -275))

    return special_spaces


def reset_castling_spotlight(castling_spotlight):
    for spot in castling_spotlight:
        spot.hideturtle()
    castling_spotlight.clear()


def castling_spot_clicked(spot, player, white_set, black_set, reset_spotlight, castling_spotlight, next_turn, screen, highlighter):
    reset_spotlight()
    reset_castling_spotlight(castling_spotlight)

    if player == 'white':
        pieces = white_set
    elif player == 'black':
        pieces = black_set

    for piece in pieces:
        if spot.xcor() <= -125 and piece.name == 'king':
            piece.setpos(spot.pos())
            king_new_x = piece.xcor()
        elif spot.xcor() >= 100 and piece.name == 'king':
            piece.setpos(spot.pos())
            king_new_x = piece.xcor()

    for piece in pieces:
        if spot.xcor() <= -125 and tuple(piece.pos()) == (-275, -275):
            piece.setpos(king_new_x + 75, -275)
        elif spot.xcor() >= 100 and tuple(piece.pos()) == (250, -275):
            piece.setpos(king_new_x - 75, -275)

    h = Turtle(shape=os.path.join(script_directory, 'images/highlighter.gif'))
    h.penup()
    h.setpos(spot.xcor(), spot.ycor())
    highlighter.append(h)

    screen.update()
    next_turn[0] = True
