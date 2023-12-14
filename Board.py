import turtle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
sqrs = []
for n in range(1,9):
    for letter in letters:
        sqrs.append(letter+str(n))
print(sqrs)
class board:
    def __init__(self):
        self.squares = {}
