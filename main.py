import pygame
import sys
import os
from pygame.locals import QUIT
from road import Road
from car import Car
from display import Display
from scheduler import Scheduler
from depot import Depot
from myMap import map4, map16, map24 # import your map
import time

def main(input_file, output_path):
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    window.fill((255, 255, 255))
    
    ### INPUT ###
    fp = open(input_file, 'r')
    map_type = fp.readline().strip('\n')
    
    ### OUTPUT ###
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    if map_type == 'map4':
        now_map = map4.Map()
    elif map_type == 'map16':
        now_map = map16.Map()
    elif map_type == 'map24':
        now_map = map24.Map()

    road = Road(window, now_map.getX(), now_map.getY(), now_map.getZone(), now_map.getTunnel())
    scheduler = Scheduler(window, road)
    depot = Depot(window, road, scheduler, now_map.getPathCount(), now_map.getPath())
    display = Display(window, road, scheduler)
    
    car_count = fp.readline().strip('\n')
    for car_index in range(int(car_count)):
        road_type, depart_time = fp.readline().split()
        depot.addCar(car_index, int(road_type), int(depart_time))
    fp.close()
   

    ### EXEC ###
    now_time = 0
    now_goal = 0
    now_resolution = 0
    RUNNING, PAUSE, END = 0, 1, 2
    index = 0
    state = RUNNING
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if state == RUNNING:
                        state = PAUSE
                    else:
                        state = RUNNING
        if state == PAUSE or state == END:
            continue
        
        goal, resolution = scheduler.schedule(now_time)
        now_goal += goal
        now_resolution += (now_time*goal - resolution)
        
        
        if now_goal == len(depot.car_list): 
            state = END
        else:
            for car in depot.car_list:
                if now_time == car.departTime():
                    car.depart()
        
        display.update(now_time, now_goal, now_resolution, state) 
        pygame.display.update()
        
        # save output as pictures
        output_name = output_path + '/' + '%02d' %index + '.jpg'
        print(output_name)
        pygame.image.save(window, output_name)
        index += 1
        
        # time goes
        time.sleep(1)
        now_time += 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python main.py input_file output_directory')
        sys.exit()
    main(sys.argv[1], sys.argv[2])

