# make a board: 8 x 8. Key name for all the squares.


# make functions for each piece:
# object oriented program:
# detect if a piece can be taken:
# other micelanous rules such as queening and castling and en passent:

# bismillah allahu akbar

from Board import board
from turtle import Screen

parts = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
screen = Screen()
screen.addshape('images/darkseagreen1.gif')
screen.addshape('images/darkslategrey.gif')

for part in parts:
    screen.addshape(f'images/b_{part}_1x_ns.gif')
    screen.addshape(f'images/w_{part}_1x_ns.gif')

screen.tracer(0, 0)

chessboard = board()

print(chessboard.squares)
print(chessboard.squares['a1']['co_ordinates'])
print(chessboard.squares['a2']['co_ordinates'])
screen.update()
screen.mainloop()
