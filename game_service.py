from dao.game_dao import GameDao
from model.frigate import Frigate
from model.game import Game
from model.battlefield import Battlefield
from model.cruiser import Cruiser
from model.destroyer import Destroyer
from model.player import Player
from model.aircraft import Aircraft
from model.submarine import Submarine

class GameService:
    def __init__(self):
        self.game_dao = GameDao()

    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int,max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)

    def join_game(self, game_id: int, player_name: str) -> bool:
        game=self.game_dao.find_game(game_id)
        player=Player(name=player_name)
        return game.add_player(player)

    def get_game(self, game_id: int) -> Game:
        return self.game_dao.find_game(game_id)

    def add_vessel(self, game_id: int, player_name: str, vessel_type: str, x: int, y: int, z: int) -> bool:
        game = self.get_game(game_id)
        player = [i for i in game.get_players() if i.name == player_name][0]
        battle_field = player.get_battlefield()
        vessel = GameDao.find_vessel(type)
        battle_field.add_vessel(vessel)

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int, y: int, z: int) -> bool:
        game = self.game_dao.find_game(game_id)
        player = Player(name=shooter_name)
        vessel = self.game_dao.find_vessel(vessel_id)
        return player.fire_at(vessel,x,y,z)

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        game = self.get_game(game_id)
        player = Player(shooter_name)
        if player.battle_field.get_power()==0:
            return "Perdu"
        else:
            return "Gagne"
