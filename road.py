import numpy as np
import pygame


class Road:
    def __init__(self, window, road_x, road_y, zone_list, tunnel_list):
        self.window = window
        self.road_array = np.zeros((road_x + 2, road_y + 2))
        self.road_x = road_x
        self.road_y = road_y
        self.w = self.window.get_width() / (self.road_x+4)
        self.h = self.window.get_height() / (self.road_y+4)
        self.zone_list = zone_list
        self.tunnel_list = tunnel_list
    
    def getWidth(self):
        return self.w
    def getHeight(self):
        return self.h

    def isValid(self, pos):
        if self.road_array[pos[0]][pos[1]] == 0:
            return True
        return False

    def occupy(self, pos):
        self.road_array[pos[0]][pos[1]] = 1
    def leave(self, pos):
        self.road_array[pos[0]][pos[1]] = 0

    def move(self, pos1, pos2):
        self.road_array[pos1[0]][pos1[1]] = 0
        self.road_array[pos2[0]][pos2[1]] = 1

    def drawRoad(self):
        boarder_color = (0, 0, 0)
        road_color = (128, 128, 128)
        zone_color = (255, 228, 184)
        tunnel_color = (100, 90, 84)
        zone_width = 8
        road_width = 5
        tunnel_width = 10
       
        for zone in self.zone_list:
            x = (zone[0]+2)*self.w
            y = (zone[1]+2)*self.h
            rect = pygame.Rect(x, y, self.w, self.h)
            pygame.draw.rect(self.window, zone_color, rect)   

        for tunnel in self.tunnel_list:
            pos1 = ((tunnel[0][0]+2.5)*self.w, (tunnel[0][1]+2.5)*self.h)
            pos2 = ((tunnel[1][0]+2.5)*self.w, (tunnel[1][1]+2.5)*self.h)
            pygame.draw.line(self.window, tunnel_color, pos1, pos2, tunnel_width)



        for x in range(2, self.road_x+3):
            start_pos = (self.w*x, self.h*2)
            end_pos = (self.w*x, self.h*(self.road_y+2))
            pygame.draw.line(self.window, boarder_color, start_pos, end_pos, zone_width)
            pygame.draw.line(self.window, road_color, (self.w*x, self.h), start_pos, road_width)
            pygame.draw.line(self.window, road_color, end_pos, (self.w*x, self.h*(self.road_y+3)), road_width)

        for y in range(2, self.road_y+3):
            start_pos = (self.w*2, self.h*y)
            end_pos = (self.w*(self.road_x+2), self.h*y)
            pygame.draw.line(self.window, boarder_color, start_pos, end_pos, zone_width)
            pygame.draw.line(self.window, road_color, (self.w, self.h*y), start_pos, road_width)
            pygame.draw.line(self.window, road_color, end_pos, (self.w*(self.road_x+3), self.h*y), road_width)

        
