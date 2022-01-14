# Written by Aaron Barge
# Copyright 2022

import pygame
import random

import constants
import simulation
from planet import Planet
from vector import Vector2D

PRESETS = {
    0: [
        Planet(
            20000, 20,
            Vector2D(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, 0),
            pygame.Color(255, 255, 255)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH * 3 // 4, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, 10),
            pygame.Color(255, 0, 0)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH // 4, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, -10),
            pygame.Color(0, 255, 0))
    ],
    1: [
        Planet(
            1000, 5,
            Vector2D(5, constants.SCREEN_HEIGHT - 5),
            Vector2D(1, -1),
            pygame.Color(255, 255, 255)),
        Planet(
            5, 2,
            Vector2D(20, constants.SCREEN_HEIGHT - 5),
            Vector2D(9, -10),
            pygame.Color(255, 0, 0)),
        Planet(
            5, 2,
            Vector2D(0, constants.SCREEN_HEIGHT - 40),
            Vector2D(-2, 3),
            pygame.Color(0, 255, 0))
    ],
    2: [
        Planet(
            10000, 20,
            Vector2D(constants.SCREEN_WIDTH // 2 - 40, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, 8),
            pygame.Color(255, 255, 255)),
        Planet(
            10000, 20,
            Vector2D(constants.SCREEN_WIDTH // 2 + 40, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, -8),
            pygame.Color(255, 255, 255)),
        Planet(
            5, 5,
            Vector2D(10, constants.SCREEN_HEIGHT - 10),
            Vector2D(3, 3),
            pygame.Color(0, 255, 0)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH - 10, 10),
            Vector2D(0, 6),
            pygame.Color(255, 0, 0)),
        Planet(
            5, 5,
            Vector2D(10, 10),
            Vector2D(4, -1),
            pygame.Color(0, 0, 255)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH - 10, constants.SCREEN_HEIGHT - 10),
            Vector2D(6, -1),
            pygame.Color(255, 0, 255)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH // 2, 10),
            Vector2D(5, -4),
            pygame.Color(0, 255, 255)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT - 10),
            Vector2D(-6, -1),
            pygame.Color(255, 255, 0)),
        Planet(
            0.005, 2,
            Vector2D(constants.SCREEN_WIDTH // 2 + 10, constants.SCREEN_HEIGHT - 10),
            Vector2D(-6, 2),
            pygame.Color(128, 128, 0))
        ],
    3: [
        Planet(
            50000, 25,
            Vector2D(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, 0),
            pygame.Color(255, 255, 255)),
        Planet(
            5, 5,
            Vector2D(constants.SCREEN_WIDTH // 2 + 250, constants.SCREEN_HEIGHT // 2),
            Vector2D(0, 8),
            pygame.Color(255, 0, 0)),
        ],
}

def main():
    planets: list[Planet] = PRESETS[3]
    simulation.run(planets)

if __name__ == "__main__":
    main()
