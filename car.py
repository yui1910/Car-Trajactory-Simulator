import pygame
from direction import Direct

class Car:
    def __init__(self, car_id, window, road, scheduler, start_pos, end_pos, path, color, time):
        self.car_id = car_id 
        self.window = window
        self.road = road
        self.scheduler = scheduler
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.path = path
        self.color = color
        self.now_pos = None
        self.index = -1
        self.time = time
    
    def getID(self):
        return self.car_id

    def departTime(self):
        return self.time

    def depart(self):
        self.index = 0
        self.now_pos = self.start_pos
        self.next_pos = self.path[self.index+1]
        self.road.occupy(self.now_pos)
        self.scheduler.addCar(self)
        
    def canMove(self):
        return self.road.isValid(self.path[self.index+1])
           
    def move(self):
        self.road.move(self.now_pos, self.path[self.index+1])
        self.index += 1
        self.now_pos = self.path[self.index]

    def leave(self):
        self.road.leave(self.now_pos)

    def isEnd(self):
        return (self.now_pos == self.end_pos)

    def draw(self):
        w = self.road.getWidth()
        h = self.road.getHeight()
        x = w * (self.now_pos[0] + 1.5)
        y = h * (self.now_pos[1] + 1.5)
        pygame.draw.circle(self.window, self.color, (x, y), 25, 0)
        direct = Direct.getDirect(self.now_pos, self.path[self.index+1])
        arrow = Direct.getArrow(x, y, 20, direct)
        pygame.draw.polygon(self.window, (0, 0, 0), arrow)
        my_font = pygame.font.SysFont(None, 25)
        text = my_font.render(str(self.getID()), True, (255, 255, 255), (5, 5, 5))
        textRect = text.get_rect(center=(x, y))
        self.window.blit(text, textRect)
