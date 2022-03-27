
import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move,"Up")

level = 1

game_is_on = True
finished = player.finishLine()
currentpos = player.ycor()
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    for _ in range(0,level):
        finished = player.finishLine()

        car_manager.create_car()
        car_manager.move_cars()

        #Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 15:
                game_is_on = False
                scoreboard.game_over()

    #Detect successful crossing
    if finished :
        player.go_to_start()
        #car_manager.level_up()
        level= level * 2
        scoreboard.increase_level()      





    
screen.exitonclick()     

