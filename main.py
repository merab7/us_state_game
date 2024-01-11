import turtle
import pandas
from write import Write

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
turtle.penup()
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()
score = 0
guessed_list = []
game_on = True

while game_on:
    user_input = turtle.textinput(title=f"{score}""/"f"{len(states_list)}", prompt="Write a state: ")

    if user_input.lower() == "exit":
        break
    else:
        for r in states_list:
            if user_input.lower() == r.lower():
                score += 1
                guessed_list.append(r.lower())
                indexes = states_list.index(r)
                Write(x=x_list[indexes], y=y_list[indexes], state=r)

learn = []

for x in states_list:
    if x.lower() not in guessed_list:
        learn.append(x)

you_must_learn = {
    "states": learn
}

pandas.DataFrame(you_must_learn).to_csv("learn_this")
