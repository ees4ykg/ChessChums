from turtle import Turtle,Screen

class Pawn(Turtle):
    def __init__(self, colour, co_ords):
        super().__init__()
        self.penup()
        self.colour = colour
        self.shape(f"images/{colour}_pawn_1x_ns.gif")
        self.setpos(co_ords)

    def movement(self):
        new_x = self.pos()[0]
        new_y = self.pos()[1] + 75
        self.setpos(new_x, new_y)

    def capture(self, direction):
        #check if pieces are diagional
        #if they are, delete that piece and move to its location
        if direction == "left":
            new_x = self.pos() - 75
            new_y = self.pos() + 75
            self.setpos(new_x, new_y)

        elif direction == "right":
            new_x = self.pos()[0] + 75
            new_y = self.pos()[1] + 75
            self.setpos(new_x, new_y)





