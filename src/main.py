import sys
import time
import os

from frupal import (
    Map,
    Config,
    Player,
    Drawer,
    User
)

if __name__ == "__main__":
    try:
        window = (os.get_terminal_size().columns, os.get_terminal_size().lines)
    except OSError:
        window = (60, 50)

    # Initializations
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            debug = True
    config = Config()
    user = User(window, config, debug)

    # Draw Game Title Screen
    drawer = Drawer(window, debug)
    drawer.title_screen()

    # Take user input
    running = user.main_menu(config)
    playing = 0

    # Main Loop
    while running:
        # Initialize Map When Player Selects Start
        game_map = Map(config, debug)
        player = Player(config, debug)
        user.update_store(config)
        playing = 1
        player.player_view(2, game_map)
        while playing != 0:
            # Print Game Screen
            drawer.print_game(player, game_map)
            drawer.print_stats(player)

            # Conditions for continuing
            playing = user.control(player, game_map)
            if playing == 2 or playing == 3:
                drawer.print_game(player, game_map)
                time.sleep(3)
                drawer.final_screen(playing)
                playing = 0
        running = user.main_menu(config)
