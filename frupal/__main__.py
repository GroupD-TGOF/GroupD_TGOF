from frupal import (
    Map,
    Config,
    Player,
    Drawer
)


def switch_menu(choice: int):
    if choice == 1:
        return True
    if choice == 2:
        return False
    if choice == 3:
        return False


if __name__ == "__main__":
    debug = True;
    # config = Config.load_config()
    # Make the player
    game_map = Map(10, 20, debug)
    player = Player(20, 20, debug)
    drawer = Drawer()
    drawer.title_screen()
    playing = switch_menu(drawer.menu_screen())
    while playing:
        drawer.print_map(player, game_map)
        drawer.print_stats(player)
        playing = drawer.game_menu(player, game_map)
