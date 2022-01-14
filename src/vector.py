# Written by Aaron Barge
# Copyright 2022

import math

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"

    def __abs__(self) -> 'float':
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, v: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + v.x, self.y + v.y)

    def __iadd__(self, v: 'Vector2D') -> 'Vector2D':
        self.x += v.x
        self.y += v.y
        return self

    def __sub__(self, v: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - v.x, self.y - v.y)

    def __isub__(self, v: 'Vector2D') -> 'Vector2D':
        self.x -= v.x
        self.y -= v.y
        return self

    def cross(self, v: 'Vector2D') -> float:
        return self.x * v.y - self.y * v.x 

    def dot(self, v: 'Vector2D') -> float:
        return self.x * v.x + self.y * v.y

    def __mul__(self, n: float) -> 'Vector2D':
        return Vector2D(self.x * n, self.y * n)

    def __imul__(self, n: float) -> 'Vector2D':
        self.x *= n
        self.y *= n
        return self

    def __rmul__(self, n: float) -> 'Vector2D':
        return self * n

    def __truediv__(self, n: float) -> 'Vector2D':
        return Vector2D(self.x / n, self.y / n)

    def __itruediv__(self, n: float) -> 'Vector2D':
        self.x /= n
        self.y /= n
        return self

    def square(self) -> 'Vector2D':
        return Vector2D(self.x ** 2, self.y ** 2)

    def i_square(self) -> 'Vector2D':
        self.x **= 2
        self.y **= 2
        return self

    def normalize(self) -> 'Vector2D':
        return self / abs(self)

    def i_normalize(self) -> 'Vector2D':
        self /= abs(self)
        return self

    def invert(self) -> 'Vector2D':
        return Vector2D(1.0 / self.x, 1.0 / self.y)

    def i_invert(self) -> 'Vector2D':
        if self.x != 0:
            self.x = 1 / self.x
        if self.y != 0:
            self.y = 1 / self.y
        return self
    