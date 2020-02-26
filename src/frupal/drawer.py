import crayons
import os
import time
import platform


class Drawer:
    def __init__(self, window: tuple, debug: bool):
        self.width = window[0]
        self.height = window[1]
        self.middle = self.height // 2
        self.debug = debug

    def title_screen(self):
        for i in range(self.middle - 1):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        print(crayons.green("The Game of Frupal!".center(self.width)), end='')
        for i in range(self.middle):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        time.sleep(3)

    def final_screen(self, playing: int):
        for i in range(self.middle):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        if playing == 3:
            print(crayons.green("You Win!".center(self.width)))
        if playing == 2:
            print(crayons.green("You Lose!".center(self.width)))
        for i in range(self.middle):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        time.sleep(3)

    def print_game(self, player, game_map):
        border = u"\u25A0"
        b = player.get_position()
        map_size = game_map.get_size()
        spacer_lines = (self.height - map_size[0]) // 2
        spacer_columns = (self.width - ((map_size[1]) * 2)) // 2

        # Before Spacer
        for a in range(spacer_lines):
            if self.debug:
                print("+ " + str(a))
            else:
                print()

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
                            print(crayons.cyan("J"), end=' ')
                    else:
                        if platform.system() == "Windows":
                            print('X', end=' ')
                        else:
                            print(u"\u25A0", end=' ')

            # End border for each line
            print(crayons.blue(border), end='\n')

        # Spacer for centering map border bottom
        for m in range(spacer_columns):
            print(' ', end='')

        # Border After End Line of Map
        for l in range(map_size[1] + 2):
            print(crayons.blue(border), end=' ')
        print()

        # After Spacer
        for a in range(spacer_lines - 1):
            if self.debug:
                print("+ " + str(a))
            else:
                print()
            if a == 2:
                print(game_map[b[1]][b[0]].print_tile(player.inventory).center(self.width))

    def print_stats(self, player):
        s_str = "Energy: "
        s_str += str(player.get_energy())
        s_str += "     Money: "
        s_str += str(player.get_money())
        s_str += "     Inventory: "
        s_str += ' '.join([str(elem).capitalize() for elem in player.inventory])
        print(crayons.yellow(s_str.center(self.width)))
