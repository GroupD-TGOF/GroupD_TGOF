from .config import Config
from .player import Player


if __name__ == "__main__":
    config = Config.load_config()
    # Make the player
    player = Player(energy=config.start_energy, money=config.start_money)
    playing = True
    while playing:
        # TODO: do loop
        playing = False
