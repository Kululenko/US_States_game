from turtle import Turtle, Screen
import pandas
from turtles import States


state_obj = States()
turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "C:\\Users\\pcmai\\Desktop\\python\\100days\\US_states_game\\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pandas.read_csv("C:\\Users\\pcmai\\Desktop\\python\\100days\\US_states_game\\50_states.csv")


guessed_states = []
states_to_learn = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states",prompt="Tell me a state").title()
    print(answer_state)

    
    if answer_state in df["state"].values:
        state_data = df[df["state"] == answer_state]
        name = state_data["state"].values[0]  
        x_corr = int(state_data["x"].iloc[0])  
        y_corr = int(state_data["y"].iloc[0])
        state_obj.create_state(x=x_corr,y=y_corr,name=name)  
        if name not in guessed_states:
            guessed_states.append(name)

    elif answer_state == "Exit":
        states_to_learn.extend(state for state in df["state"].values if state not in guessed_states)
        df2 = pandas.DataFrame(states_to_learn)
        df2.to_csv("states_to_learn.csv")
        break
        
        

            



