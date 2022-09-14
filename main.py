import pandas
import turtle


def create_screen_of_us_map():
    screen_turtle = turtle.Screen()
    screen_turtle.title('U.S. States Game')
    image = 'blank_states_img.gif'
    screen_turtle.addshape(image)
    turtle.shape(image)

    return screen_turtle


screen = create_screen_of_us_map()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

# Check if answer_state is a state in the list of all_states.

guessed_states = []
# missed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 Correctly Guessed States',
        prompt="Type the name of a US State. Type 'Exit' to exit and reveal missed states.").title()

    if answer_state == 'Exit':
        missed_states = [state for state in all_states if state not in guessed_states]

        missed_states_df = pandas.DataFrame(missed_states)
        missed_states_df.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()  # If correct guess, create a turtle which appears as text at correctly guessed location.
        t.hideturtle()
        t.penup()
        correct_state_data = data[data.state == answer_state]
        t.goto(int(correct_state_data.x), int(correct_state_data.y))
        t.write(correct_state_data.state.item(), align='center', font=("Calibri", 12, "bold"))  # .item() just turns
        # the panda series item to a string.

endgame_screen = create_screen_of_us_map()
t2 = turtle.Turtle()

for missed_state in missed_states:
    missed_state_data = data[data.state == missed_state]
    t2.penup()
    t2.hideturtle()
    t2.speed(10)
    t2.goto(int(missed_state_data.x), int(missed_state_data.y))
    t2.color('red')
    t2.write(missed_state_data.state.item(), align='center', font=("Calibri", 12, "bold"))

endgame_screen.exitonclick()
