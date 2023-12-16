from turtle import Turtle, Screen
import numpy as np

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
sqrs = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a3', 'b3',
        'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'a5', 'b5', 'c5', 'd5',
        'e5', 'f5', 'g5', 'h5', 'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7',
        'g7', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
board_colours = ['images/darkseagreen1.gif', 'images/darkslategrey.gif']


translate_matrix = np.array([[1, 0, 12.5], [0, 1, 12.5], [0, 0, 1]])
rotate_matrix = np.array([[-1, 0, 0 ], [0, -1, 0], [0, 0, 1]])
translate_inverse_matrix = np.array([[1, 0, -12.5], [0, 1, -12.5], [0, 0, 1]])


class Board:
    def __init__(self):
        p = 1
        n = 0
        self.squares = {}
        for square in sqrs:
            x_ord = letters[square[0]] * 75 - 350
            y_ord = int(square[1]) * 75 - 350
            self.squares.update({square: {'piece': 'empty', 'co_ordinates': (x_ord, y_ord)}})
            t = Turtle(shape=board_colours[(p + n) % 2])
            t.penup()
            t.setpos(x_ord, y_ord)
            p += 1
            if (p % 8) - 1 == 0:
                n += 1

    def flip(self):
        for square in self.squares.values():
            co_ordinates_matrix = np.matrix([[square['co_ordinates'][0]], [square['co_ordinates'][1]], [1]])
            new_co_ordinates_matrix = translate_inverse_matrix.dot(rotate_matrix.dot(translate_matrix.dot(co_ordinates_matrix)))
            square['co_ordinates'] = (int(new_co_ordinates_matrix[0][0]), int(new_co_ordinates_matrix[1][0]))
