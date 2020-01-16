import pickle
import os


class Config:
    config_filename = 'config.pickle'
    static = None

    @staticmethod
    def load_config():
        if not Config.static:
            if os.path.exists(Config.config_filename):
                with open(Config.config_filename, 'rb') as fin:
                    Config.static = pickle.load(file=fin)
            else:
                Config.static = Config()
        return Config.static

    def __init__(self):
        config = Config.load_config()
        self._start_money = getattr(config, '_start_money', 100.0)
        self._start_energy = getattr(config, '_start_energy', 100.0)

    def __del__(self):
        with open(Config.config_filename, 'wb') as fout:
            pickle.dump(self, file=fout)

    @property
    def start_money(self):
        return Config.static._start_money

    @start_money.setter
    def start_money(self, new_value: float):
        Config.static._start_money = new_value

    @property
    def start_energy(self):
        return Config.static._start_energy

    @start_energy.setter
    def start_energy(self, new_value: float):
        Config.static._start_energy = new_value
