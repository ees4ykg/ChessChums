from turtle import Turtle,Screen

num = {"w": 75, "b": -75}
class Pawn(Turtle):
    def __init__(self, colour, co_ords):
        super().__init__()
        self.penup()
        self.colour = colour
        self.shape(f"images/{colour}_pawn_1x_ns.gif")
        self.setpos(co_ords)

    def Movement(self):
        new_x = self.pos()[0]
        new_y = self.pos()[1] + num[self.colour]
        self.setpos(new_x, new_y)




