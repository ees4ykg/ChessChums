from turtle import Turtle
import numpy as np
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
sqrs = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3',
        'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5',
        'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7',
        'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

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

board_colours = [os.path.join(script_directory, 'images/darkseagreen1.gif'),
                 os.path.join(script_directory, 'images/darkslategrey.gif')]
colours = ['darkseagreen1', 'darkslategrey']

translate_matrix = np.array([[1, 0, 12.5], [0, 1, 12.5], [0, 0, 1]])
rotate_matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
translate_inverse_matrix = np.array([[1, 0, -12.5], [0, 1, -12.5], [0, 0, 1]])
matrix_transformation = translate_inverse_matrix.dot(rotate_matrix.dot(translate_matrix))


class Board:
    def __init__(self, draw):
        p = 1
        n = 0
        self.squares = {}
        for square in sqrs:
            x_ord = letters[square[0]] * 75 - 350
            y_ord = int(square[1]) * 75 - 350
            self.squares.update({square: {'piece': 'empty', 'co_ordinates': (x_ord, y_ord)}})
            if draw:
                t = Turtle(shape=board_colours[(p + n) % 2])
                t.penup()
                t.setpos(x_ord, y_ord)
                p += 1
                if (p % 8) - 1 == 0:
                    n += 1
        self.reversed = False
        self.squares_reversed = squares_reversed_w
        if draw:
            pen = Turtle()
            pen.pensize(3)
            pen.penup()
            pen.setpos(self.squares['a8']['co_ordinates'])
            pen.left(90)
            pen.forward(37.5)
            pen.left(90)
            pen.forward(37.5)
            pen.pendown()
            for x in range(4):
                pen.left(90)
                pen.forward(600)
            n = 0
            for x in range(8):
                pen.fillcolor(colours[n % 2])
                pen.begin_fill()
                pen.left(45)
                pen.forward(30)
                pen.left(45)
                pen.forward(75)
                pen.left(135)
                pen.forward(30)
                pen.left(135)
                pen.end_fill()
                n += 1
            n = 1
            for x in range(8):
                pen.fillcolor(colours[n % 2])
                pen.begin_fill()
                pen.left(45)
                pen.forward(30)
                pen.left(135)
                pen.forward(75)
                pen.left(45)
                pen.forward(30)
                pen.left(135)
                pen.end_fill()
                n += 1
            pen.hideturtle()

    def flip(self, white_set, black_set, highlighter):

        for square in self.squares.values():
            co_ordinates_matrix = np.matrix([[square['co_ordinates'][0]], [square['co_ordinates'][1]], [1]])
            new_co_ordinates_matrix = matrix_transformation.dot(co_ordinates_matrix)
            square['co_ordinates'] = (int(new_co_ordinates_matrix[0][0]), int(new_co_ordinates_matrix[1][0]))

        if self.squares_reversed == squares_reversed_w:
            self.squares_reversed = squares_reversed_b

        elif self.squares_reversed == squares_reversed_b:
            self.squares_reversed = squares_reversed_w

        for piece in white_set + black_set + highlighter:
            co_ordinates_matrix = np.matrix([[piece.xcor()], [piece.ycor()], [1]])
            new_co_ordinates_matrix = matrix_transformation.dot(co_ordinates_matrix)
            new_co_ordinates = (int(new_co_ordinates_matrix[0][0]), int(new_co_ordinates_matrix[1][0]))
            piece.setpos(new_co_ordinates)

        self.reversed = not self.reversed

    def update(self, white_set, black_set):

        for square in self.squares.values():
            square['piece'] = 'empty'

        for piece in white_set + black_set:
            square = self.squares_reversed[f'({piece.xcor()}, {piece.ycor()})']
            self.squares[square]['piece'] = f'{piece.colour}_{piece.name}'
