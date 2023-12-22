import ftplib
from turtle import Turtle

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def set_square_piece(board, colour, co_ords, name):
    if not board.reversed:  # if it is a white pawn
        board.squares[board.squares_reversed[str(co_ords)]]['piece'] = f'{colour}_{name}'
    elif board.reversed:  # if it is a black pawn it adds the pawn to the square
        board.squares[board.squares_reversed[str(co_ords)]]['piece'] = f'{colour}_{name}'


def initialise_piece(self, colour, co_ords, name):
    self.penup()
    self.colour = colour
    if self.colour == 'w':
        self.opposite_colour = 'b'
    elif self.colour == 'b':
        self.opposite_colour = 'w'
    self.shape(f"images/{colour}_{name}_1x_ns.gif")
    self.setpos(co_ords)


def vision_update_loop(self, board, directions, infinity): # Used for vision_update in rook, bishop and queen class
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
    def __init__(self, colour, co_ords, board):

        super().__init__()
        initialise_piece(self, colour, co_ords, 'pawn')

        self.vision = []
        self.capture_vision = []
        self.has_moved = False

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


class Rook(Turtle):
    def __init__(self, colour, co_ords, board):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'rook')

        self.vision = []
        self.capture_vision = []
        self.has_moved = False

        set_square_piece(board, colour, co_ords, "rook")

    def vision_update(self, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vision_update_loop(self, board, directions, True)


class Bishop(Turtle):
    def __init__(self, colour, co_ords, board):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'bishop')

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'bishop')

    def vision_update(self, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        vision_update_loop(self, board, directions, True)


class Queen(Turtle):
    def __init__(self, colour, co_ords, board):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'queen')

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'queen')

    def vision_update(self, board):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
        vision_update_loop(self, board, directions, True)


class Knight(Turtle):
    def __init__(self, colour, co_ords, board):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'knight')

        self.vision = []
        self.capture_vision = []

        set_square_piece(board, colour, co_ords, 'knight')

    def vision_update(self, board):
        directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        vision_update_loop(self, board, directions, False)


class King(Turtle):
    def __init__(self, colour, co_ords, board):
        super().__init__()
        initialise_piece(self, colour, co_ords, 'king')

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
            piece_set.append(Pawn(colour="w", co_ords=board.squares[letter + "2"]["co_ordinates"], board=board))

        piece_set.append(Knight(colour='w', co_ords=board.squares['b1']['co_ordinates'], board=board))
        piece_set.append(Knight(colour='w', co_ords=board.squares['g1']['co_ordinates'], board=board))
        piece_set.append(Bishop(colour='w', co_ords=board.squares['c1']['co_ordinates'], board=board))
        piece_set.append(Bishop(colour='w', co_ords=board.squares['f1']['co_ordinates'], board=board))
        piece_set.append(Rook(colour='w', co_ords=board.squares['a1']['co_ordinates'], board=board))
        piece_set.append(Rook(colour='w', co_ords=board.squares['h1']['co_ordinates'], board=board))
        piece_set.append(Queen(colour='w', co_ords=board.squares['d1']['co_ordinates'], board=board))
        piece_set.append(King(colour='w', co_ords=board.squares['e1']['co_ordinates'], board=board))

    elif colour == 'b':
        for letter in letters.keys():
            piece_set.append(Pawn(colour="b", co_ords=board.squares[letter + "7"]["co_ordinates"], board=board))

        piece_set.append(Knight(colour='b', co_ords=board.squares['b8']['co_ordinates'], board=board))
        piece_set.append(Knight(colour='b', co_ords=board.squares['g8']['co_ordinates'], board=board))
        piece_set.append(Bishop(colour='b', co_ords=board.squares['c8']['co_ordinates'], board=board))
        piece_set.append(Bishop(colour='b', co_ords=board.squares['f8']['co_ordinates'], board=board))
        piece_set.append(Rook(colour='b', co_ords=board.squares['a8']['co_ordinates'], board=board))
        piece_set.append(Rook(colour='b', co_ords=board.squares['h8']['co_ordinates'], board=board))
        piece_set.append(Queen(colour='b', co_ords=board.squares['d8']['co_ordinates'], board=board))
        piece_set.append(King(colour='b', co_ords=board.squares['e8']['co_ordinates'], board=board))

    return piece_set