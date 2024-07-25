from turtle import Turtle , Screen
import pandas as pd
screen = Screen()
screen.setup(width = 800 , height = 600)


map = Turtle()
mb = Turtle()
screen.title("US state game")
screen.addshape("Day_14/US GAME/blank_states_img.gif")
map.shape("Day_14/US GAME/blank_states_img.gif")

data = pd.read_csv("Day_14/US GAME/50_states.csv")
# print(data.state)

state_list = data.state.to_list()

guessed_state = []
while(len(guessed_state) < 50):
    answer_txt = screen.textinput(title = f"{len(guessed_state)} / 50" , prompt="Enter the state name")

    if(answer_txt == "exit"):
            print(state_list)
            not_answered_list = [state for state in state_list if state.lower() not in guessed_state]
            print(guessed_state)
            new_dataframe = pd.DataFrame(not_answered_list)
            new_dataframe.to_csv("not_answered.csv")

            print(not_answered_list)
            break

    for _ in range(len(data)):
        if(answer_txt.lower() == data.state.values[_].lower() and answer_txt.lower() not in guessed_state):
            guessed_state.append(answer_txt)
            mb.penup()
            mb.hideturtle()
            mb.goto(data.x.values[_] , data.y.values[_])
            mb.write(f"{answer_txt}" , align="left")
            
    
            




