import turtle
import pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

state_writer = StateWriter()
correct_guesses = []

while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if guess not in correct_guesses and guess in states_list:
        # extract the state's data
        row = data[data["state"] == guess]
        x = int(row["x"].iloc[0])
        y = int(row["y"].iloc[0])
        # guess = row.state.item()
        state_writer.write_state_name(guess, x, y)
        correct_guesses.append(guess)

screen.exitonclick()
