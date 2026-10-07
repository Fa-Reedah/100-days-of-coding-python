import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []


while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct.",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        not_guessed_states = [state for state in all_states if state not in guessed_states]

        df = pandas.DataFrame(not_guessed_states)
        df.to_csv("States_to_Learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        txt = turtle.Turtle()
        txt.hideturtle()
        txt.penup()
        state_data = data[data.state == answer_state]
        txt.goto(int(state_data.x.item()), int(state_data.y.item()))
        txt.write(answer_state)






