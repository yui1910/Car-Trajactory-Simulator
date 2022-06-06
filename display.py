import pygame
import numpy as np

class Display:
    def __init__(self, window, road, scheduler):
        self.window = window
        self.road = road
        self.scheduler = scheduler
    def update(self, time, goal, resolution, state):
        self.window.fill((255, 255, 255))
        self.road.drawRoad()
        self.scheduler.drawCar()
        my_font = pygame.font.SysFont(None, 50)
        text = my_font.render('Press SPACE to pause', True, (0, 0, 0))
        self.window.blit(text, (400, 10))
        text = my_font.render('Time: ' + str(time), True, (0, 0, 0))
        self.window.blit(text, (10, 10))
        text = my_font.render('Goal: ' + str(goal), True, (0, 0, 0))
        self.window.blit(text, (10, 65))
        if goal == 0:
            p = "-"
        else:
            p = np.round(resolution / goal, 2)
        text = my_font.render('Average Resolution Time: ' + str(p), True, (0, 0, 0))
        self.window.blit(text, (10, 550))
        if state == 2: #END
            text = my_font.render('Complete!', True, (0, 0, 0))
            self.window.blit(text, (600, 550))
