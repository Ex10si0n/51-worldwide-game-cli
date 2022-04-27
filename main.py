from hit_and_blow import Game
from helper import *

class Lobby():
    def __init__(self):
        self.game_list = ['hit_and_blow', 'mancala']
        self.banner = '''\
        +----------------------------------------------------+
        |                                                    |
        |                51 World Game CLI                   |
        |                                                    |
        |               Created by Ex10si0n                  |
        |                                                    |
        +----------------------------------------------------+
        '''

if __name__ == "__main__":
    lobby = Lobby()
    while True:
        cls()
        print(lobby.banner)
        for i in range(len(lobby.game_list)):
            print('[', i, ']', lobby.game_list[i])
        print('[ q ] quit')
        select = input('play: ')
        if select.lower() == 'q':
            break
        __import__(lobby.game_list[int(select)])
        Game()



