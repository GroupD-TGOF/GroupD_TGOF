from . import (
	Map,
	Config,
	Player,
	Drawer
)


def switchmenu(choice: int):
	if(choice == 1):
		return True
	if(choice == 2):
		return False
	if(choice == 3):
		return False

if __name__ == "__main__":
	#config = Config.load_config()
	#Make the player
	map = Map(10, 20)
	player = Player(20, 20)
	drawer = Drawer()
	drawer.titlescreen()
	playing = switchmenu(drawer.menuscreen())
	while playing:
		drawer.printmap(player, map)
		drawer.printstats(player)
		playing = drawer.gamemenu(player, map)
