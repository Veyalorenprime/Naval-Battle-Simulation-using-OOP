from exceptions import NoAmmunitionError


class Weapon:
    def __init__(self, ammunitions: int, range: int):
        self.ammunitions = ammunitions
        self.range = range

    def fire_at(self, x, y, z):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Vous n'avez plus de munitions !")

        self.check_target_position(x, y, z)

        self.ammunitions = self.ammunitions - 1

    def get_ammunitions(self):
        return self.ammunitions

    def get_range(self):
        return self.range

    def check_target_position(self, x, y, z):
        raise NotImplementedError()
