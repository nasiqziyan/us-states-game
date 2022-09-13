import pandas
import turtle

screen = turtle.Screen()

screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title='Guess a State',
    prompt='Type the name of a US State.').title()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

# Check if answer_state is a state in the list of all_states

if answer_state in all_states:
    t = turtle.Turtle()  # If correct guess, create a turtle which appears as text at the correctly guessed location.
    t.hideturtle()
    t.penup()
    correct_state_data = data[data.state == answer_state]
    t.goto(int(correct_state_data.x), int(correct_state_data.y))
    t.write(correct_state_data.state.item())  # .item() just turns the panda series item to a string.

screen.exitonclick()
