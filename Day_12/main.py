import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()



game_is_on = True


while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()    
    car_manager.move_car()
    
    # To detect the collision of turtle with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    
    # To see if turtle reaches finish line

    if player.is_reach_finish_line():
        player.back_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
   

screen.exitonclick()


