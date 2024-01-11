from turtle import Turtle


class Write(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        self.color("black")
        self.penup()
        self.goto(self.x, self.y)
        self.pendown()
        self.write(f"{self.state}", move=False, align='center',
                   font=('Arial', 8, 'normal'))
        self.hideturtle()
