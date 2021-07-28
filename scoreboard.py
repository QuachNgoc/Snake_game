from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self) -> object:
        super().__init__()
        self.point = 0

        with open(".\data\data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"SCORE: {self.point} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.point += 1

    def update(self):
        self.clear()
        self.write(f"SCORE: {self.point} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
            with open("data.txt", mode="w") as data_1:
                data_1.write(str(self.high_score))
        self.point = 0
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over.", True, align=ALIGNMENT, font=FONT)


