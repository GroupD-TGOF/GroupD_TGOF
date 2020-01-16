from .map import Direction


class Player:
    def __init__(self, energy: float, money: float):
        """
        Create a new player class
        :param energy: the starting energy
        :param money:  the starting money
        """
        self.energy = energy
        self.money = money
        self.position = (0, 0)

    def move(self, direction: Direction):
        """
        Move the player in a specific direction
        :param direction: Direction enum
        :return:
        """
        if direction == Direction.NORTH:
            self.position[0] += 1
        #TODO implement other directions
        pass

