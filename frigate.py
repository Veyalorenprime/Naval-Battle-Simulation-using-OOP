from surface_missile_launcher import SurfaceMissileLauncher
from vessel import Vessel


class Frigate(Vessel):

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 5, SurfaceMissileLauncher())

    def go_to(self, x, y, z):
        if z != 0:
            raise ValueError("Coordonnées de déplacement invalides !")
        self.coordinates = (x, y, z)
