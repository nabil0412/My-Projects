from turtle import Turtle , Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


startpos = [(0,0),(-20,0),(-40,0)]
segments = []


snake1 = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey (snake1.up,"Up")
screen.onkey(snake1.down, "Down")
screen.onkey (snake1.left, "Left")
screen.onkey (snake1.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    #Detect collision with food.
    if snake1.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake1.extend()

    #Detect collision with wall.
    if snake1.head.xcor () > 295 or snake1.head.xcor () < -295 or snake1.head.ycor () > 295 or snake1.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake1.segments[1:]:
        if snake1.head.distance (segment) < 10:
            game_is_on = False
            scoreboard.game_over()



  


        
        





















screen.exitonclick()


