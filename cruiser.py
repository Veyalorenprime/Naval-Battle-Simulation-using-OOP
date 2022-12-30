from air_missile_launcher import AirMissileLauncher
from vessel import Vessel


class Cruiser(Vessel):

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 6, AirMissileLauncher())

    def go_to(self, x, y, z):
        if z != 0:
            raise ValueError("Coordonnées de déplacement invalides !")
        self.coordinates = (x, y, z)
