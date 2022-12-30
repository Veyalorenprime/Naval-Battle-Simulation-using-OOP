from math import sqrt

from exceptions import DestroyedError, OutOfRangeError
from weapon import Weapon


class Vessel:
    def __init__(self, x: float, y: float, z: float, hits: int,
                 weapon: Weapon):
        self.coordinates = x, y, z
        self.hits_to_be_destroyed = hits
        self.weapon = weapon

    def go_to(self, x, y, z):
        if self.hits_to_be_destroyed == 0:
            raise DestroyedError('Vessel destroyed !')

        self.coordinates = x, y, z

    def get_coordinates(self) -> (float, float, float):
        return self.coordinates

    def fire_at(self, x, y, z):
        if self.hits_to_be_destroyed == 0:
            raise DestroyedError('Vessel destroyed !')

        if self.calculate_distance_to(x, y, z) > self.weapon.get_range():
            raise OutOfRangeError('La cible est hors de portée!')

        self.weapon.fire_at(x, y, z)

    def touched(self):
        self.hits_to_be_destroyed = self.hits_to_be_destroyed - 1

    def get_weapon(self) -> Weapon:
        return self.weapon

    def get_hits(self):
        return self.hits_to_be_destroyed

    def calculate_distance_to(self, x, y, z):
        coord = self.coordinates
        return sqrt(
            (coord[0] - x) ** 2 + (coord[1] - y) ** 2 + (coord[2] - z) ** 2)
