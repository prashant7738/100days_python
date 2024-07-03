from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        
    def create_car(self):
        random_value = random.randint(1,6)
        if random_value == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-240, 240))
            
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def move_car(self):

        for car in self.all_cars:
            # x_cor = car.xcor() - STARTING_MOVE_DISTANCE
            # car.setx(x_cor)
            car.backward(self.car_speed)

    


