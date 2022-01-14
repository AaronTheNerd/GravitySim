# Written by Aaron Barge
# Copyright 2022

import constants
from planet import Planet
import pygame
from pygame.locals import QUIT

def run(planets):
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen.set_alpha(1)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                continue
        screen.fill((0, 0, 0, 100))
        for planet in planets:
            planet.update_vel(planets)
        for planet in planets:
            planet.update_collision()
        for planet in planets:
            planet.update_pos()
        for planet in planets:
            planet.display(screen)
        pygame.display.update()
        clock.tick(constants.FRAME_RATE)
        