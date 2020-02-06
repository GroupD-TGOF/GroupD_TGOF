from frupal import (
    Map,
    Config,
    Player,
    Drawer,
    User
)

if __name__ == "__main__":
    # Draw Game Title Screen
    drawer = Drawer()
    user = User()
    drawer.title_screen()

    # Initializations
    debug = False
    config = Config()
    game_map = Map(config, debug)
    player = Player(config, debug)

    # Take user input
    playing = user.main_menu(config)

    # Main Game Loop
    while playing:
        # Print Game Screen
        drawer.print_map(player, game_map)
        drawer.print_stats(player)

        # Conditions for continuing
        playing = user.game_menu(player, game_map) and (player.get_energy() != 0)
