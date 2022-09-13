import pandas
import turtle

screen = turtle.Screen()

screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

# Check if answer_state is a state in the list of all_states.

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 Correctly Guessed States',
        prompt="Type the name of a US State. Type 'Exit' to exit.").title()

    if answer_state == 'Exit':
        missed_states = []

        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)

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





