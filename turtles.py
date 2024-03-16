from turtle import Turtle



class States(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()





    def create_state(self,x,y,name):
        self.goto(x,y)
        self.write(arg=name)
