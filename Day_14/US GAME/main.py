from turtle import Turtle , Screen
import pandas as pd
screen = Screen()
screen.setup(width = 800 , height = 600)


map = Turtle()
mb = Turtle()
screen.title("US state game")
screen.addshape("blank_states_img.gif")
map.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
# print(data.state)

state_list = data.state.to_list()

guessed_state = []
while(len(guessed_state) < 50):
    answer_txt = screen.textinput(title = f"{len(guessed_state)} / 50" , prompt="Enter the state name")

    

    for _ in range(len(data)):
        if(answer_txt.lower() == data.state.values[_].lower() and answer_txt.lower() not in guessed_state):
            guessed_state.append(answer_txt)
            mb.penup()
            mb.hideturtle()
            mb.goto(data.x.values[_] , data.y.values[_])
            mb.write(f"{answer_txt}" , align="left")
            
    if(answer_txt == "exit"):
            not_answered_list = []
            # not_answered_list = list(set(state_list) - set(guessed_state))
            for state in state_list:
                if (state not in guessed_state):
                    not_answered_list.append(state)
            break


new_dataframe = pd.DataFrame(not_answered_list)
new_dataframe.to_csv("not_answered.csv")



