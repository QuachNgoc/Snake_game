from turtle import Turtle

MOVE_DISTANCE = 20
POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> object:
        self.segment = []  # in class we have to use self to list, function,etc
        self.create_snake()
        self.head = self.segment[0]

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_part(pos)

    def add_part(self, position):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.segment.append(new_part)

    def extend(self):
        self.add_part(self.segment[-1].position()) # thêm vào đuôi

    # auto moving forward
    def move_fd(self):
        # vị trí cuối thành vị trí kế, vị trí trước vị trí kế sẽ có thể di chuyển trái hoặc phải
        for part in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[part - 1].xcor()
            new_y = self.segment[part - 1].ycor()
            self.segment[part].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
