from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state_name(self, state, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(state)

