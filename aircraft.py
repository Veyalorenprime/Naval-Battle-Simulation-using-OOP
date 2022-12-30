from air_missile_launcher import AirMissileLauncher

from surface_missile_launcher import SurfaceMissileLauncher
from vessel import Vessel


class Aircraft(Vessel):

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1, SurfaceMissileLauncher())

    def go_to(self, x, y, z):
        if z != 1:
            raise ValueError("Coordonnées de déplacement invalides !")
        self.coordinates = (x, y, z)
