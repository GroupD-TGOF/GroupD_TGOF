from time import sleep
from platform import system
import crayons


class Drawer:
    def __init__(self, window: tuple, debug: bool):
        if debug:
            print(window[0], window[1])
        self.width = window[0]
        self.height = window[1]
        self.debug = debug

    def __spacer(self, buffer: int):
        for i in range(buffer):
            if self.debug:
                print("+ " + str(i))
            else:
                print()

    def title_screen(self):
        title = list()
        title.append("  █████▒██▀███   █    ██  ██▓███   ▄▄▄       ██▓    ")
        title.append("▓██   ▒▓██ ▒ ██▒ ██  ▓██▒▓██░  ██▒▒████▄    ▓██▒    ")
        title.append("▒████ ░▓██ ░▄█ ▒▓██  ▒██░▓██░ ██▓▒▒██  ▀█▄  ▒██░    ")
        title.append("░▓█▒  ░▒██▀▀█▄  ▓▓█  ░██░▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░    ")
        title.append("░▒█░   ░██▓ ▒██▒▒▒█████▓ ▒██▒ ░  ░ ▓█   ▓██▒░██████▒")
        title.append(" ▒ ░   ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░")
        title.append(" ░       ░▒ ░ ▒░░░▒░ ░ ░ ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░")
        title.append(" ░ ░     ░░   ░  ░░░ ░ ░ ░░         ░   ▒     ░ ░   ")
        title.append("          ░        ░                    ░  ░    ░  ░")
        buffer = (self.height - len(title)) // 2
        self.__spacer(buffer)
        for line in title:
            print(crayons.green(line.center(self.width)))
        for i in range(buffer - 2):
            if i == buffer // 2:
                print(crayons.green("A Text Based Island Adventure Game!").center(self.width))
            elif self.debug:
                print("+ " + str(i))
            else:
                print()
        print(crayons.green("Now Loading!").center(self.width))
        for i in range(0, self.width, 1):
            print(u"\u25A0", end='')
            sleep(0.010)

    def final_screen(self, playing: int):
        lose = list()
        lose.append("▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████  ▐██▌ ")
        lose.append(" ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌ ")
        lose.append("  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███    ▐██▌ ")
        lose.append("  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒ ")
        lose.append("  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄  ")
        lose.append("   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒ ")
        lose.append(" ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░ ")
        lose.append(" ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░       ░ ")
        lose.append(" ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░ ░    ")
        lose.append(" ░ ░                                                                 ")

        win = list()
        win.append("▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █  ▐██▌ ")
        win.append(" ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █  ▐██▌ ")
        win.append("  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒ ▐██▌ ")
        win.append("  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒ ▓██▒ ")
        win.append("  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░ ▒▄▄  ")
        win.append("   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒  ░▀▀▒ ")
        win.append(" ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░  ░ ")
        win.append(" ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░     ░ ")
        win.append(" ░ ░         ░ ░     ░            ░     ░           ░  ░    ")
        win.append(" ░ ░                                                        ")

        buffer = 0
        if playing == 2:
            buffer = (self.height - len(lose)) // 2
        if playing == 3:
            buffer = (self.height - len(win)) // 2
        self.__spacer(buffer)
        if playing == 2:
            for line in lose:
                print(crayons.green(line.center(self.width)))
        if playing == 3:
            for line in win:
                print(crayons.green(line.center(self.width)))
        self.__spacer(buffer - 1)
        sleep(3)

    def print_game(self, player, game_map):
        border = u"\u25A0"
        b = player.get_position()
        map_size = game_map.get_size()
        spacer_lines = (self.height - (map_size[0] + 2)) // 2
        spacer_columns = (self.width - ((map_size[1] + 2) * 2)) // 2

        # Before Spacer
        self.__spacer(spacer_lines)

        # Spacer for centering map border top
        for m in range(spacer_columns):
            print(' ', end='')

        # Border On Line
        for l in range(map_size[1] + 2):
            print(crayons.blue(border), end=' ')
        print()

        for j in range(map_size[0]):

            # Spacer for centering map
            for m in range(spacer_columns):
                print(' ', end='')

            # Start border for each line
            print(crayons.blue(border), end=' ')

            # Display Map
            for k in range(map_size[1]):
                if k == b[0] and j == b[1]:
                    print(crayons.red("P"), end=' ')
                else:
                    if game_map[j][k].seen_status():
                        if not game_map[j][k].has_item('jewels'):
                            if game_map[j][k].get_color() == 'red':
                                print(crayons.red(game_map[j][k].get_icon()), end=' ')
                            elif game_map[j][k].get_color() == 'green':
                                print(crayons.green(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'yellow':
                                print(crayons.yellow(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'blue':
                                print(crayons.blue(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'black':
                                print(crayons.black(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'magenta':
                                print(crayons.magenta(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'cyan':
                                print(crayons.cyan(game_map[j][k]).get_icon(), end=' ')
                            elif game_map[j][k].get_color() == 'white':
                                print(crayons.white(game_map[j][k]).get_icon(), end=' ')
                            else:
                                print(crayons.green(game_map[j][k]).get_icon(), end=' ')
                        else:
                            print(crayons.cyan("J"), end=' ')
                    else:
                        if system() == "Windows":
                            print('X', end=' ')
                        else:
                            print(u"\u25A0", end=' ')

            # End border for each line
            print(crayons.blue(border))

        # Spacer for centering map border bottom
        for m in range(spacer_columns):
            print(' ', end='')

        # Border After End Line of Map
        for l in range(map_size[1] + 2):
            print(crayons.blue(border), end=' ')
        print()
        print()
        print("(Press K) Keybindings!".center(self.width - 1))
        self.__spacer(spacer_lines - 2)
        print(game_map[b[1]][b[0]].print_tile(player.inventory).center(self.width))
        self.print_stats(player)

    def print_stats(self, player):
        s_str = "Energy: "
        s_str += str(player.get_energy())
        s_str += "     Money: "
        s_str += str(player.get_money())
        s_str += "     Inventory: "
        s_str += ' '.join([str(elem).replace('_', ' ').capitalize() for elem in player.inventory])
        print(crayons.yellow(s_str.center(self.width)))
