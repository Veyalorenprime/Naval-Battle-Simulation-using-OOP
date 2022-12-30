

from exceptions import GameFullError
from player import Player

class Game:
    def __init__(self, id=None):
        self.id = id
        self.players = []

    def get_id(self) -> int:
        return self.id

    def get_players(self) -> list[Player]:
        return self.players

    def add_player(self, player: Player):
        if len(self.players) >= 2:
            raise GameFullError(
                "Seulement 2 joueurs sont admis dans la partie !")
        self.players.append(player)
