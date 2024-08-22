from turtle import Turtle



FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        #give it a variable level = 1, hideturtle(), penup(), goto(-280, 250), then update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        #increase the level by 1 and update_scoreboard
        pass

    def game_over(self):
        #goto(0,0)

        #and write GAME OVER , align center, font=FONT

        pass
