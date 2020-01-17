from config import Config
from player import Player
from drawer import Drawer
     
def switchmenu(choice: int):
        if(choice == 1):
                return True;
        if(choice == 2):
                return False;
        if(choice == 3):
                return False;

if __name__ == "__main__":
        #config = Config.load_config()
        #Make the player
        #player = Player(energy=config.start_energy, money=config.start_money)
	drawer = Drawer()
	drawer.titlescreen()
	playing = switchmenu(drawer.menuscreen())
	while playing:
                drawer.printmap()
                playing = False
