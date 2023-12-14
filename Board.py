from turtle import Turtle, Screen

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
sqrs = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3',
        'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5',
        'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7',
        'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
board_colours = ['DarkSeaGreen1', 'DarkGrey']

class board:
    def __init__(self):
        self.squares = {}
        for square in sqrs:
            x_ord = letters[square[0]] * 75 - 350
            y_ord = int(square[1]) * 75 - 350
            self.squares.update({square: {'piece': 'empty', 'co_ordinates': (x_ord, y_ord)}})

        # creates a dictionary with all the squares containing a piece value and coordinate value
        self.pen = Turtle(shape='square')
        self.pen.penup()
        self.pen.pensize(37.5)

        t = 1
        n = 0
        for square in self.squares.values():
            self.pen.color(board_colours[(t+n) % 2])
            self.pen.setpos(square['co_ordinates'])
            self.pen.dot()
            t += 1
            if (t % 8) - 1 == 0:
                n += 1



chessboard = board()
screen = Screen()
print(chessboard.squares)

chessboard.squares['a1']['piece'] = 'bishop'
print(chessboard.squares)

screen.exitonclick()