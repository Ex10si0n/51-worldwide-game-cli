# Hit-and-Blow
import random
import os
from helper import *

class Game:
    def __init__(self):
        # Colorset: Red Green Blue Yellow White Cyan
        self.color_set = ['r', 'g', 'b', 'y', 'w', 'c']
        self.answer = ['r', 'g', 'b', 'y', 'w', 'c']
        random.shuffle(self.answer)
        self.answer = self.answer[:4]
        self.display_answer = ['x', 'x', 'x', 'x']
        self.guess_slot = [['_', '_', '_', '_'] for i in range(8)]
        self.guess_result = [[0, 0] for i in range(8)]
        self.gametable = """
        +----------------------------------------------------------------------+
        | F H     F H     F H     F H     F H     F H      F H      F H  |     |
        | {self.guess_result[0][0]} {self.guess_result[0][1]}     {self.guess_result[1][0]} {self.guess_result[1][1]}     {self.guess_result[2][0]} {self.guess_result[2][1]}     {self.guess_result[3][0]} {self.guess_result[3][1]}     {self.guess_result[4][0]} {self.guess_result[4][1]}     {self.guess_result[5][0]} {self.guess_result[5][1]}      {self.guess_result[6][0]} {self.guess_result[6][1]}      {self.guess_result[7][0]} {self.guess_result[7][1]}  |     |
        |  {self.guess_slot[0][0]}       {self.guess_slot[1][0]}       {self.guess_slot[2][0]}       {self.guess_slot[3][0]}       {self.guess_slot[4][0]}       {self.guess_slot[5][0]}        {self.guess_slot[6][0]}        {self.guess_slot[7][0]}   |  {self.display_answer[0]}  |
        |  {self.guess_slot[0][1]}       {self.guess_slot[1][1]}       {self.guess_slot[2][1]}       {self.guess_slot[3][1]}       {self.guess_slot[4][1]}       {self.guess_slot[5][1]}        {self.guess_slot[6][1]}        {self.guess_slot[7][1]}   |  {self.display_answer[1]}  |
        |  {self.guess_slot[0][2]}       {self.guess_slot[1][2]}       {self.guess_slot[2][2]}       {self.guess_slot[3][2]}       {self.guess_slot[4][2]}       {self.guess_slot[5][2]}        {self.guess_slot[6][2]}        {self.guess_slot[7][2]}   |  {self.display_answer[2]}  |
        |  {self.guess_slot[0][3]}       {self.guess_slot[1][3]}       {self.guess_slot[2][3]}       {self.guess_slot[3][3]}       {self.guess_slot[4][3]}       {self.guess_slot[5][3]}        {self.guess_slot[6][3]}        {self.guess_slot[7][3]}   |  {self.display_answer[3]}  |
        +----------------------------------------------------------------------+
        """
        self.start()

    def print_table(self):
        table = self.gametable.format(self=self)
        table = table.replace('r', '\033[41;m \033[0m').replace('g', '\033[42;m \033[0m').replace('b', '\033[44;m \033[0m').replace('y', '\033[43;m \033[0m').replace('w', '\033[47;m \033[0m').replace('c', '\033[46;m \033[0m')
        print(table)


    def check_guess(self, i):
        full = []
        rest = []
        for j in range(4):
            if self.guess_slot[i][j] == self.answer[j]:
                self.guess_result[i][0] += 1
                full.append(self.guess_slot[i][j])
        for j in range(4):
            if self.guess_slot[i][j] not in rest and self.guess_slot[i][j] not in full:
                rest.append(self.guess_slot[i][j])
        for j in rest:
            if j in self.answer:
                self.guess_result[i][1] += 1



    def start(self):
        for i in range(8):
            cls()
            self.print_table()
            guess = input("[r:\033[41;m \033[0m g:\033[42;m \033[0m b:\033[44;m \033[0m y:\033[43;m \033[0m w:\033[47m \033[0m c:\033[46;m \033[0m]  > ")
            guess = guess.lower()
            if guess == 'q':
                return
            guess = guess.split(' ')
            self.guess_slot[i] = guess
            self.check_guess(i)
            if guess == self.answer:
                self.display_answer = self.answer
                break
        cls()
        self.display_answer = self.answer
        self.print_table()
        cmd = input("[q: quit]  > ")
        if cmd == 'q':
            return



if __name__ == '__main__':
    game = Game()
