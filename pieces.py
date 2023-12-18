from turtle import Turtle, Screen

squares_reversed_w = {'(-275, -275)': 'a1', '(-200, -275)': 'b1', '(-125, -275)': 'c1', '(-50, -275)': 'd1',
                      '(25, -275)': 'e1', '(100, -275)': 'f1', '(175, -275)': 'g1', '(250, -275)': 'h1',
                      '(-275, -200)': 'a2', '(-200, -200)': 'b2', '(-125, -200)': 'c2', '(-50, -200)': 'd2',
                      '(25, -200)': 'e2', '(100, -200)': 'f2', '(175, -200)': 'g2', '(250, -200)': 'h2',
                      '(-275, -125)': 'a3', '(-200, -125)': 'b3', '(-125, -125)': 'c3', '(-50, -125)': 'd3',
                      '(25, -125)': 'e3', '(100, -125)': 'f3', '(175, -125)': 'g3', '(250, -125)': 'h3',
                      '(-275, -50)': 'a4', '(-200, -50)': 'b4', '(-125, -50)': 'c4', '(-50, -50)': 'd4',
                      '(25, -50)': 'e4', '(100, -50)': 'f4', '(175, -50)': 'g4', '(250, -50)': 'h4', '(-275, 25)': 'a5',
                      '(-200, 25)': 'b5', '(-125, 25)': 'c5', '(-50, 25)': 'd5', '(25, 25)': 'e5', '(100, 25)': 'f5',
                      '(175, 25)': 'g5', '(250, 25)': 'h5', '(-275, 100)': 'a6', '(-200, 100)': 'b6',
                      '(-125, 100)': 'c6',
                      '(-50, 100)': 'd6', '(25, 100)': 'e6', '(100, 100)': 'f6', '(175, 100)': 'g6', '(250, 100)': 'h6',
                      '(-275, 175)': 'a7', '(-200, 175)': 'b7', '(-125, 175)': 'c7', '(-50, 175)': 'd7',
                      '(25, 175)': 'e7', '(100, 175)': 'f7', '(175, 175)': 'g7', '(250, 175)': 'h7',
                      '(-275, 250)': 'a8',
                      '(-200, 250)': 'b8', '(-125, 250)': 'c8', '(-50, 250)': 'd8', '(25, 250)': 'e8',
                      '(100, 250)': 'f8',
                      '(175, 250)': 'g8', '(250, 250)': 'h8'}

squares_reversed_b = {'(250, 250)': 'a1', '(175, 250)': 'b1', '(100, 250)': 'c1',
                      '(25, 250)': 'd1', '(-50, 250)': 'e1', '(-125, 250)': 'f1', '(-200, 250)': 'g1',
                      '(-275, 250)': 'h1', '(250, 175)': 'a2', '(175, 175)': 'b2', '(100, 175)': 'c2',
                      '(25, 175)': 'd2', '(-50, 175)': 'e2', '(-125, 175)': 'f2', '(-200, 175)': 'g2',
                      '(-275, 175)': 'h2', '(250, 100)': 'a3', '(175, 100)': 'b3', '(100, 100)': 'c3',
                      '(25, 100)': 'd3', '(-50, 100)': 'e3', '(-125, 100)': 'f3', '(-200, 100)': 'g3',
                      '(-275, 100)': 'h3', '(250, 25)': 'a4', '(175, 25)': 'b4', '(100, 25)': 'c4', '(25, 25)': 'd4',
                      '(-50, 25)': 'e4', '(-125, 25)': 'f4', '(-200, 25)': 'g4', '(-275, 25)': 'h4', '(250, -50)': 'a5',
                      '(175, -50)': 'b5', '(100, -50)': 'c5', '(25, -50)': 'd5', '(-50, -50)': 'e5',
                      '(-125, -50)': 'f5', '(-200, -50)': 'g5', '(-275, -50)': 'h5', '(250, -125)': 'a6',
                      '(175, -125)': 'b6', '(100, -125)': 'c6', '(25, -125)': 'd6', '(-50, -125)': 'e6',
                      '(-125, -125)': 'f6', '(-200, -125)': 'g6', '(-275, -125)': 'h6', '(250, -200)': 'a7',
                      '(175, -200)': 'b7', '(100, -200)': 'c7', '(25, -200)': 'd7', '(-50, -200)': 'e7',
                      '(-125, -200)': 'f7', '(-200, -200)': 'g7', '(-275, -200)': 'h7', '(250, -275)': 'a8',
                      '(175, -275)': 'b8', '(100, -275)': 'c8', '(25, -275)': 'd8', '(-50, -275)': 'e8',
                      '(-125, -275)': 'f8', '(-200, -275)': 'g8', '(-275, -275)': 'h8'}

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

def set_square_piece(board,colour,co_ords,piece):
    if not board.reversed:  # if it is a white pawn
            board.squares[squares_reversed_w[str(co_ords)]]['piece'] = f'{colour}_{piece}' #adds the pawn to the square
    elif board.reversed:  # if it is a black pawn
        board.squares[squares_reversed_b[str(co_ords)]['piece']] = f'{colour}_{piece}'


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

        set_square_piece(board,colour,co_ords,"pawn")

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
    def __init__(self, colour,opposite_colour,co_ords, board):
        super().__init__()

        self.penup()
        self.colour = colour
        self.opposite_colour = opposite_colour
        self.shape(f"images/{colour}_rook_1x_ns.gif")
        self.setpos(co_ords)
        self.vision = []
        self.capture_vision = []
        self.has_moved = False

        set_square_piece(board,colour,co_ords,"rook")

    def vision_update(self, board):
        self.vision = []

        for square in board.squares:
            #for every square which leter is the same as the letter that the rook is on
            #print(str(self.pos))
            if square[0] == squares_reversed_w[str(self.pos)][0]:
                if board.square[square]["piece"] != "empty":
                    break
                self.vision.append(board.square[square]["co_ordinates"])

            #for every square which leter is the same as the number that the rook is on
            elif square[1] == squares_reversed_w[str(self.pos)][1]:
                if board.square[square]["piece"] != "empty":
                    break
                self.vision.append(board.square[square]["co_ordinates"])





            



