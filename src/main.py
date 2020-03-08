from platform import system
from time import sleep
from frupal import (
    Map,
    Config,
    Player,
    Drawer,
    User
)
import sys
import os

if __name__ == "__main__":
    # Try to get size of window if OS error then set default size.
    try:
        if system() == "Windows":
            window = (os.get_terminal_size().columns - 1, os.get_terminal_size().lines)
        else:
            window = (os.get_terminal_size().columns, os.get_terminal_size().lines)
    except OSError:
        window = (60, 50)

    # Initializations
    # See if debug option is enabled from command line
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            debug = True

    # Load Config and Pass Values
    config = Config()
    user = User(window, config, debug)

    # Draw Game Title Screen
    drawer = Drawer(window, debug)
    drawer.title_screen()

    # Take user input
    running = user.main_menu(config)

    # Initialize Game Map and Player
    game_map = Map(config, debug)
    player = Player(config, debug)

    # Main Loop
    while running:
        # Update the map, player, and user for new game
        game_map.update_map(config, debug)
        player.update_player(config, debug)
        user.update_store(config, debug)

        # set playing to yes
        playing = 1

        # Starts of Map Reveal
        player.player_view(1, game_map)
        while playing != 0:
            # Print Game Screen
            drawer.print_game(player, game_map)

            # Finds Whether to Continue or not
            playing = user.control(player, game_map)

            # If playing is 2 or 3 the game will return to main menu and before it does will display win or lose
            if playing == 2 or playing == 3:
                # Print Map one more time and Print Final Screen
                drawer.print_game(player, game_map)
                sleep(3)
                drawer.final_screen(playing)
                playing = 0
        running = user.main_menu(config)
