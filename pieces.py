from turtle import Turtle, Screen


parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']


def set_square_piece(board, colour, co_ords, piece):
    if not board.reversed:  # if it is a white pawn
        board.squares[board.squares_reversed[str(co_ords)]]['piece'] = f'{colour}_{piece}'  # adds the pawn to the square
    elif board.reversed:  # if it is a black pawn
        board.squares[board.squares_reversed[str(co_ords)]]['piece'] = f'{colour}_{piece}'


class Pawn(Turtle):
    def __init__(self, colour, opposite_colour, co_ords, board):
        super().__init__()

        self.penup()
        self.colour = colour
        self.opposite_colour = opposite_colour
        self.shape(f"images/{colour}_pawn_1x_ns.gif")
        self.setpos(co_ords)
        self.vision = [(self.xcor(), self.ycor() + 75), (self.xcor(), self.ycor() + 150)]
        self.capture_vision = []
        self.has_moved = False

        set_square_piece(board, colour, co_ords, "pawn")

    def movement(self):
        new_x = self.pos()[0]
        new_y = self.pos()[1] + 75
        self.setpos(new_x, new_y)

    def capture(self, direction):
        # check if pieces are diagional
        # if they are, delete that piece and move to its location
        if direction == "left":
            new_x = self.xcor() - 75
            new_y = self.ycor() + 75
            self.setpos(new_x, new_y)

        elif direction == "right":
            new_x = self.xcor() + 75
            new_y = self.ycor() + 75
            self.setpos(new_x, new_y)

    def vision_update(self, board):

        self.vision = []

        for square in board.squares.values():
            if square['co_ordinates'] == (self.xcor(), self.ycor() + 75):
                if square['piece'] == 'empty':  # adds first square pawn can move to
                    self.vision.append((self.xcor(), self.ycor() + 75))

            elif not self.has_moved and square['co_ordinates'] == (self.xcor(), self.ycor() + 150):
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
    def __init__(self, colour, opposite_colour, co_ords, board):
        super().__init__()

        self.penup()
        self.colour = colour
        self.opposite_colour = opposite_colour
        self.shape(f"images/{colour}_rook_1x_ns.gif")
        self.setpos(co_ords)
        self.vision = []
        self.capture_vision = []
        self.has_moved = False

        set_square_piece(board, colour, co_ords, "rook")

    def vision_update(self, board):
        self.vision = []

        for square in board.squares:
            # for every square which letter is the same as the letter that the rook is on
            if board.squares[square]['co_ordinates'] == self.pos():
                pass

            elif square[0] == board.squares_reversed[str((int(self.xcor()), int(self.ycor())))][0]:
                if board.squares[square]["piece"] != "empty":
                    break
                self.vision.append(board.squares[square]["co_ordinates"])

            # for every square which letter is the same as the number that the rook is on
            elif square[1] == board.squares_reversed[str((int(self.xcor()), int(self.ycor())))][1]:
                if board.squares[square]["piece"] != "empty":
                    break
                self.vision.append(board.squares[square]["co_ordinates"])

        self.capture_vision = []