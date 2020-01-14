import pickle
import os


class Config:

    @staticmethod
    def load_config(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as fin:
                return pickle.load(file=fin)
        return Config()

    def __init__(self):
        self.x = 1
        config = Config.load_config('out.pickle')
        if config:
            self = config

    def __del__(self):
        fout = open('out.pickle', 'wb')
        pickle.dump(self, file=fout)

c = Config.load_config('out.pickle')
print('c.x: ', c.x)
del c
