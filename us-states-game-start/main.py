import turtle
import pandas as pd
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
states = data.state.to_list()

guess = []

while len(guess) < 50:
    answer_state = screen.textinput(title=f"{len(guess)}/50 Correct Guess.",prompt="What's another state name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guess]
        df = pd.DataFrame(states_to_learn)
        df.to_csv("Missing_states.csv")
        break

    if answer_state in  states:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(x=int(state_data.x),y=int(state_data.y))
        tim.write(answer_state)
        guess.append(answer_state)


