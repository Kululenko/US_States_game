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
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states",prompt="Tell me a state").capitalize()
    print(answer_state)

    for state in df["state"].values:
        if answer_state in df["state"].values:
            state_data = df[df["state"] == answer_state]
            name = state_data["state"].values[0]  
            x_corr = int(state_data["x"])  
            y_corr = int(state_data["y"])
            state_obj.create_state(x=x_corr,y=y_corr,name=name)  
            
            if name not in guessed_states:
                guessed_states.append(name)



            





screen.exitonclick()