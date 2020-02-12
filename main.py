from frupal import (
    Map,
    Config,
    Player,
    Drawer,
    User
)

import sys

if __name__ == "__main__":

    # Draw Game Title Screen
    drawer = Drawer()
    user = User()
    drawer.title_screen()

    # Initializations
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            debug = True
    config = Config()

    # Take user input
    playing = user.main_menu(config)

    # Initialize Map When Player Selects Start or Changes Config
    game_map = Map(config, debug)
    player = Player(config, debug)

    # Main Game Loop
    while playing != 0:
        # Print Game Screen
        drawer.print_map(player, game_map)
        drawer.print_stats(player)

        # Conditions for continuing
        playing = user.control(player, game_map)
        if playing == 2 or playing == 3:
            drawer.final_screen(playing)
            playing = 0
