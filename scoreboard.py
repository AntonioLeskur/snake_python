from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        with open(r"venv/data_score.txt") as data:
            self.high_score = int(data.read())


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"venv/data_score.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER\nYour Score: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



