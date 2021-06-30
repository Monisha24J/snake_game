from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update() #this turns off the animation of how its done step-by-step
    time.sleep(0.1)

    #Detect collision with food:
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()


    #Detect collision with wall:
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    #Detect collision with tail:
    for segment in snake.segment[3:]:
        if snake.segment[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()


    snake.move()








screen.exitonclick()
