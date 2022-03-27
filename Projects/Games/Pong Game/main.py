from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboardd import Scoreboard
import time



screen = Screen()
screen.setup(width= 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

rpaddle = Paddle((360,0))
lpaddle = Paddle((-360,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(lpaddle.go_up,"w")
screen.onkeypress(lpaddle.go_down,"s")
screen.onkeypress(rpaddle.go_up,"Up")
screen.onkeypress(rpaddle.go_down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(rpaddle) < 70 and ball.xcor() > 320 and ball.xcor() < 380) or (ball.distance(lpaddle) < 70 and ball.xcor() < -320 and ball.xcor() > -380):
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 390 :
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -390 :
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()