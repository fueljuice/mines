import tkinter as tk
import random
import time
import configuration

random.seed(time.time())


class Board:

    def __init__(self, mine_count):
        self.buttons = [[0 for _ in range(8)] for _ in range(8)]
        self.mine_objects = [[None for _ in range(8)] for _ in range(8)]
        self.mine_count = mine_count

    def create_button(self, root, x, y):
        button = tk.Button(root, width=9, height=3)  # ,command = self.OnClick
        button.grid(row=x, column=y)
        self.buttons[x][y] = button

    def create_mines(self):
        for unit in range(0, self.mine_count):
            row = random.randint(0, configuration.ROWS - 1)
            column = random.randint(0, configuration.COLUMNS - 1)

            self.mine_objects[row][column] = self.buttons[row][column]
            self.mine_objects[row][column].config(bg="blue")
            print(f'{row}, {column}, {self.mine_objects[row][column]}, {self.buttons[row][column]}')

        #  self.buttons[x][y] = None

    def create_button2(self, x, y):

        print(f'nir: {x}, {y}')
        if self.mine_objects[x][y]:
            self.mine_objects[x][y].config(
                command=lambda: self.buttons[x][y].config(state="disabled", text="You exploded!"))

        elif self.buttons[x][y]:
            self.buttons[x][y].config(command=lambda: self.buttons[x][y].config(state="disabled", bg="yellow", text=" "))

    def FindNum(self):
        pass
