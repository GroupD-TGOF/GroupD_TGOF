import crayons
import os
import time


class Drawer:
    def __init__(self):
        '''
        if os.get_terminal_size().columns != 0 and os.get_terminal_size().lines != 0:
            self.width = os.get_terminal_size().columns
            self.height = os.get_terminal_size().lines

        else:
        '''
        self.width = 40
        self.height = 30
        self.middle = self.height // 2

    def title_screen(self):
        for i in range(self.middle):
            print()
        print(crayons.green("The Game of Frupal!".center(self.width)))
        for i in range(self.middle):
            print()
        time.sleep(3)

    def print_map(self, player, game_map):
        b = player.get_position()
        size = game_map.get_size()
        spacer = self.height - size[0]
        spacer = spacer // 2
        map_size = game_map.get_size()
        for i in range(spacer):
            print()
        for j in range(map_size[0]):
            for k in range(map_size[1]):
                if k == b[0] and j == b[1]:
                    print(crayons.red(u"\u25CF"), end=' ')
                else:

                    if game_map[j][k].seen_status():
                        if game_map[j][k].get_name() == 'tile':
                            print(crayons.green(game_map[j][k].get_icon()), end=' ')
                        if game_map[j][k].get_name() == 'water':
                            print(crayons.blue(game_map[j][k].get_icon()), end=' ')
                        if game_map[j][k].get_name() == 'tree':
                            print(crayons.yellow(game_map[j][k]).get_icon(), end=' ')
                    else:
                        print(' ', end=' ')
            print()
        for i in range(spacer):
            print()

    def print_stats(self, player):
        for i in range(2):
            print()
        print(crayons.yellow("Energy: " + str(player.get_energy()) + "          " + "Money: " + str(player.get_money())))
