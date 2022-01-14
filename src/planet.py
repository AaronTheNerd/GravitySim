# Written by Aaron Barge
# Copyright 2022

import constants
from vector import Vector2D

import pygame

class Planet:
    def __init__(self, mass: int, radius: int, pos: Vector2D, vel: Vector2D, color: pygame.Color):
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.vel = vel
        self.collision = None
        self.color = color
        self.tail_color = pygame.Color(color.r, color.g, color.b, 10)
        self.tail = [(pos.x, pos.y), (pos.x, pos.y)]

    def __repr__(self) -> str:
        return f"Planet(mass={self.mass}, radius={self.radius}, pos={self.pos}, vel={self.vel}, color={self.color})"

    def update_vel(self, planets = None):
        if constants.DEBUG:
            print("\n\n" + "*" * 79)
            print(f"self: {self}")
            print("*" * 79)
        for planet in planets:
            if planet is self:
                continue
            if constants.DEBUG:
                print(f"planet: {planet}")
            r = planet.pos - self.pos
            r_mag = abs(r)
            if constants.DEBUG:
                print(f"Vector: {r}, Magnitude: {r_mag}")
            if r_mag < (planet.radius + self.radius):
                self.collision = planet
                planet.collision = self
            a = r * ((constants.G * planet.mass) / (r_mag ** 3))
            if constants.DEBUG:
                print(f"Acceleration: {a}")
                print("*" * 79)
            self.vel += a
        if constants.DEBUG:
            print("*" * 79)
        
    def update_collision(self):
        """
        Assuming inelastic collision.

        Source: https://en.wikipedia.org/wiki/Momentum#Application_to_collisions
        """
        if self.collision is not None:
            planet = self.collision
            inverted_mass_sum = 1 / (self.mass + planet.mass)
            temp_vel_1 = ((self.mass - planet.mass) * inverted_mass_sum * self.vel
                    + 2 * planet.mass * inverted_mass_sum * planet.vel)
            temp_vel_2 = ((planet.mass - self.mass) * inverted_mass_sum * planet.vel
                    + 2 * self.mass * inverted_mass_sum * self.vel)
            self.vel = temp_vel_1
            planet.vel = temp_vel_2
            self.collision = None
            planet.collision = None

    def update_pos(self):
        self.pos += self.vel
        if constants.DRAW_TAILS:
            self.tail.append((self.pos.x, self.pos.y))

    def display(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius, 0)
        if constants.DRAW_TAILS:
            pygame.draw.lines(screen, self.tail_color, False, self.tail)
