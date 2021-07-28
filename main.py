import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")

screen.tracer(0) # tracer....is coolllll

snake = Snake()
food = Food()
score = ScoreBoard()


# to input key to move
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move_fd()

    # Detect collisions
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        score.update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for part in snake.segment[1:]:
        if snake.head.distance(part) < 15:
            score.reset()
            snake.reset()


screen.exitonclick()