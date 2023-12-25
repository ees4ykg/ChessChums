# python -m nuitka --standalone --follow-imports --windows-icon-from-ico=icon.ico --disable-console --enable-plugin=tk-inter main.py
from board import Board
from pieces import *
import copy


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


# find method so player cant leave themselves in check


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

