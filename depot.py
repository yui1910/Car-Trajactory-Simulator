from car import Car
import random

class Depot:
    def __init__(self, window, road, scheduler, path_count, path):
        self.window = window
        self.road = road
        self.scheduler = scheduler
        self.car_list = []
        self.path_count = path_count
        self.path = path

    def addCar(self, index, path_type, time):
        path = self.path[path_type]
        color = (random.randint(2, 10)*25, random.randint(2, 10)*25, random.randint(2, 10)*25)
        car = Car(index, self.window, self.road, self.scheduler, path[0], path[-1], path, color, time)
        self.car_list.append(car)

