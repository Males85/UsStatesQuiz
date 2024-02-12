import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

NUM_OF_STATES = 50
FONT = ('Arial', 8, 'bold')
correct_answer = 0
# coor = data[data["state"] == "Alabama"].x[0], data[data["state"] == "Alabama"].y[0]
# print(coor)
# print(data[data["state"] == "Texas"].y[0])
# print("Alabama" in data["state"].to_list())


def write_state(state, coordinates):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(coordinates)
    new_turtle.write(f"{state}", align="center", font=FONT)


correct_guesses = []
correct_answer = 0    # remove if using len(correct_answer)
all_states = data["state"].to_list()
states_to_learn = {}

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{correct_answer}/{NUM_OF_STATES}States Correct",
                                    prompt="What's another state's name?").title()
                                            # instead of correct_answer, you could use len(correct_guesses) and then remove correct_answer variable
    if answer_state == "Exit":
        states_to_learn["not_guessed"] = all_states
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data["state"].values:        # or data["state"].to_list()
        all_states.remove(answer_state)
        state_coordinates = data[data["state"] == answer_state].x.iloc[0], data[data["state"] == answer_state].y.iloc[0]
        write_state(answer_state, state_coordinates)
        correct_guesses.append(answer_state)
        correct_answer += 1  # remove if using len(correct_guesses)

    # if correct_answer == 10:
    #     game_is_on = False



'''
for future projects: to find coordinates use turtle method onscreenclick(fun) where you must create your own funct
which prints the coordinates when you click on a map or a any other picture which is .gif file.

'''

# missing_states = [state for state in all_states if state not in correct_guesses] => List comprehension for creating list of states that are not guessed.