import ftplib
from turtle import Turtle
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def set_square_piece(board, colour, co_ords, name):
    if not board.reversed:  # if it is a white pawn
        board.squares[board.squares_reversed[f'({co_ords[0]}, {co_ords[1]})']]['piece'] = f'{colour}_{name}'
    elif board.reversed:  # if it is a black pawn it adds the pawn to the square
        board.squares[board.squares_reversed[f'({co_ords[0]}, {co_ords[1]})']]['piece'] = f'{colour}_{name}'


def initialise_piece(self, colour, co_ords, name, has_moved):
    self.penup()
    self.colour = colour

    if colour == 'w':
        self.opposite_colour = 'b'
    elif colour == 'b':
        self.opposite_colour = 'w'

    self.shape(os.path.join(script_directory, f'images/{colour}_{name}_1x_ns.gif'))
    self.setpos(co_ords)
    self.has_moved = has_moved
    self.name = name


def vision_update_loop(self, board, directions, infinity):  # Used for vision_update in rook, bishop and queen class
    self.vision = []
    self.capture_vision = []
    loop = True

    for dx, dy in directions:
        xpos = self.xcor()
        ypos = self.ycor()

        while loop:
            xpos += 75 * dx
            ypos += 75 * dy

            if str((xpos, ypos)) not in board.squares_reversed.keys():
                break

            square_piece = board.squares[board.squares_reversed[str((xpos, ypos))]]['piece']

            if square_piece == 'empty':
                self.vision.append((xpos, ypos))

            elif square_piece in [f'{self.opposite_colour}_{part}' for part in parts]:
                self.capture_vision.append((xpos, ypos))
                break

            else:
                break

            if not infinity:
                break


class Pawn(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):

        super().__init__()
        initialise_piece(self, colour, co_ords, 'pawn', has_moved)

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, "pawn")

    def vision_update(self, board):

        self.vision = []
        blocked = True

        for square in board.squares.values():
            if square['co_ordinates'] == (self.xcor(), self.ycor() + 75) and square['piece'] == 'empty':
                self.vision.append((self.xcor(), self.ycor() + 75))
                blocked = False

        for square in board.squares.values():
            if not self.has_moved and not blocked and square['co_ordinates'] == (self.xcor(), self.ycor() + 150):
                if square['piece'] == 'empty':  # adds second square to vision array if pawn has not moved yet
                    self.vision.append((self.xcor(), self.ycor() + 150))

        self.capture_vision = []

        for square in board.squares.values():
            if square['co_ordinates'] == (self.xcor() - 75, self.ycor() + 75):
                for part in parts:  # adds square to capture_vision array if enemy piece is present on that square
                    if square['piece'] == f'{self.opposite_colour}_{part}':
                        self.capture_vision.append((self.xcor() - 75, self.ycor() + 75))

            elif square['co_ordinates'] == (self.xcor() + 75, self.ycor() + 75):
                for part in parts:  # adds square to capture_vision array if enemy piece is present on that square
                    if square['piece'] == f'{self.opposite_colour}_{part}':
                        self.capture_vision.append((self.xcor() + 75, self.ycor() + 75))
    # def vision_update(self, board):
    #     self.capture_vision = []
    #     self.vision = []
    #     print(self.pos())
    #     square = board.squares_reversed[f'({self.xcor() + 75}, {self.ycor() + 75})']
    #     if board.squares[square]['piece'] in [f'{self.opposite_colour}_{part}' for part in parts]:
    #         self.capture_vision.append(board.squares[square]['co_ordinates'])
    #
    #     square = board.squares_reversed[f'({self.xcor() - 75}, {self.ycor() + 75})']
    #     if board.squares[square]['piece'] in [f'{self.opposite_colour}_{part}' for part in parts]:
    #         self.capture_vision.append(board.squares[square]['co_ordinates'])
    #
    #     square = board.squares_reversed[f'({self.xcor()}, {self.ycor() + 75})']
    #
    #     if board.squares[square]['piece'] == 'empty':
    #         self.vision.append(board.squares[square]['co_ordinates'])


class Rook(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'rook', has_moved)

        self.vision = []
        self.capture_vision = []
        self.has_moved = False

        set_square_piece(board, colour, co_ords, "rook")

    def vision_update(self, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vision_update_loop(self, board, directions, True)


class Bishop(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'bishop', has_moved)

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'bishop')

    def vision_update(self, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        vision_update_loop(self, board, directions, True)


class Queen(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'queen', has_moved)

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'queen')

    def vision_update(self, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        vision_update_loop(self, board, directions, True)


class Knight(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'knight', has_moved)

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'knight')

    def vision_update(self, board):
        directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        vision_update_loop(self, board, directions, False)


class King(Turtle):
    def __init__(self, colour, co_ords, board, has_moved):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'king', has_moved)

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'king')

    def vision_update(self, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        vision_update_loop(self, board, directions, False)


def create_piece_set(board, colour):
    piece_set = []

    if colour == 'w':
        for letter in letters.keys():
            piece_set.append(
                Pawn(colour="w", co_ords=board.squares[letter + "2"]["co_ordinates"], board=board, has_moved=False))

        piece_set.append(Knight(colour='w', co_ords=board.squares['b1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Knight(colour='w', co_ords=board.squares['g1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Bishop(colour='w', co_ords=board.squares['c1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Bishop(colour='w', co_ords=board.squares['f1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Rook(colour='w', co_ords=board.squares['a1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Rook(colour='w', co_ords=board.squares['h1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Queen(colour='w', co_ords=board.squares['d1']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(King(colour='w', co_ords=board.squares['e1']['co_ordinates'], board=board, has_moved=False))

    elif colour == 'b':
        for letter in letters.keys():
            piece_set.append(
                Pawn(colour="b", co_ords=board.squares[letter + "7"]["co_ordinates"], board=board, has_moved=False))

        piece_set.append(Knight(colour='b', co_ords=board.squares['b8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Knight(colour='b', co_ords=board.squares['g8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Bishop(colour='b', co_ords=board.squares['c8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Bishop(colour='b', co_ords=board.squares['f8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Rook(colour='b', co_ords=board.squares['a8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Rook(colour='b', co_ords=board.squares['h8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(Queen(colour='b', co_ords=board.squares['d8']['co_ordinates'], board=board, has_moved=False))
        piece_set.append(King(colour='b', co_ords=board.squares['e8']['co_ordinates'], board=board, has_moved=False))

    return piece_set

