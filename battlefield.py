from functools import reduce
from typing import Optional

from exceptions import OutOfRangeError
from vessel import Vessel


class Battlefield:
    def __init__(self, min_x: int, max_x: int, min_y: int, max_y: int,
                 min_z: int, max_z: int, max_power: int = 22):
        self.vessels: list[Vessel] = []
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.max_power = max_power

    def add_vessel(self, vessel: Vessel):
        x, y, z = vessel.get_coordinates()
        if x not in range(self.min_x, self.max_x) \
                or y not in range(self.min_y, self.max_y) \
                or z not in range(self.min_z, self.max_z):
            raise OutOfRangeError("Les coordonnées du vaisseau sont "
                                  "en dehors de l'espace réservé !")
        if self.get_vessel_by_coordinates(x, y, z) is not None:
            raise ValueError("Il y a déjà un vaisseau positionné ici !")
        if self.get_power() + vessel.get_hits() > self.max_power:
            raise ValueError(f"La puissance dépasse la maximum autorisé "
                             f"{self.max_power} !")

        self.vessels.append(vessel)

    def fired_at(self, x, y, z) -> bool:
        vessel = self.get_vessel_by_coordinates(x, y, z)
        if vessel is None:
            return False
        vessel.touched()
        return True

    def get_vessels(self) -> list[Vessel]:
        return self.vessels

    def get_vessel_by_coordinates(self, x, y, z) -> Optional[Vessel]:
        vessels_found = list(
            filter(lambda vessel: vessel.get_coordinates() == (x, y, z),
                   self.vessels))
        if len(vessels_found) != 0:
            return vessels_found[0]
        else:
            return None

    def get_power(self) -> int:
        return reduce(
            lambda vessel_n, vessel_n_plus_1:
            vessel_n + vessel_n_plus_1.get_hits(),
            self.vessels, 0)
