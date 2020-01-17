from config import Config
from player import Player
from drawer import Drawer


if __name__ == "__main__":
        #config = Config.load_config()
        #Make the player
        #player = Player(energy=config.start_energy, money=config.start_money)
	playing = True
	drawer = Drawer()
	drawer.titlescreen()
	drawer.menuscreen()
	drawer.printmap()
	while playing:
        # TODO: do loop
		playing = False
