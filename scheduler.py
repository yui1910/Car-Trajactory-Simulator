import random

class Scheduler:
    def __init__(self, window, road):
        self.schedule_list = []
    def addCar(self, car):
        self.schedule_list.append(car)
    def removeCar(self, car):
        self.schedule_list.remove(car)
    
    def schedule(self, now_time):
        count = 0
        resolution = 0
        for car in self.schedule_list:
            if car.canMove(): 
                car.move()
            if car.isEnd():
                count += 1
                resolution += car.departTime()
                car.leave()
                self.removeCar(car)
        return count, resolution
    
    def drawCar(self):
        for car in self.schedule_list:
            car.draw()
