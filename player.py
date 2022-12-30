from battlefield import Battlefield


class Player:
    def __init__(self, name: str, battle_field: Battlefield):
        self.id = None
        self.name = name
        self.battle_field = battle_field

    def get_name(self) -> str:
        return self.name

    def get_battlefield(self) -> Battlefield:
        return self.battle_field
