from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        #assign this turtle a shape, make its penup, make it go_to_start() and setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        #move forward by MOVE_DISTANCE
        pass

    def is_at_finish_line(self):
        #if ycor greater than FINISH_LINE_Y return True else False
        pass
    
