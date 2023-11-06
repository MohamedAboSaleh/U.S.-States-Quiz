import turtle
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = list(data.to_dict()["state"].values())

state_writer = StateWriter()
correct_guesses = []
score = 0
while score < 50:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if guess not in correct_guesses and guess in states_list:
        pass

screen.exitonclick()
