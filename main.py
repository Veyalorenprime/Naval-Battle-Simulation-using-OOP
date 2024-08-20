import Vaisseaux
from Battlefield import battlefield
from Space import space
from Weapon import Torpille
from Weapon import Missile_anti_air
from Weapon import Missile_anti_surface
from Vaisseaux import Vessel

Lance_missile_antisurface = Missile_anti_surface()
Lance_missile_anti_air = Missile_anti_air()
Lance_torpilles = Torpille()

battle = battlefield()
firstPlayer = space()
SecondPlayer = space()

firstPlayer.addVaisseaux(Vessel((10, 20, 0), 21, Lance_missile_anti_air), battle)

SecondPlayer.addVaisseaux(Vessel((4, 40, -1), 6, Lance_torpilles), battle)
SecondPlayer.addVaisseaux(Vessel((11, 21, 1), 4, Lance_missile_antisurface), battle)

vais = battle.getVaisseaux()
Vessel.set_vaisseaux(vais)

vesFirst1 = firstPlayer.getVaisseaux()[0]
vesFirst1.fire_at(11, 21, 1)

vesSec = SecondPlayer.getVaisseaux()[1]

print(vesSec.get_MaxHits())

# Cruiser = Vessel([x,y,0],6,Lance_missile_anti_air)
# Submarine = Vessel([x,y,z],2,Lance_torpilles)
# Fregate = Vessel([x,y,0],5,Lance_missile_antisurface)
# Destroyer = Vessel([x,y,0],4,Lance_torpilles)
# Aircraft = Vessel([x,y,0],1,Lance_missile_antisurface)
