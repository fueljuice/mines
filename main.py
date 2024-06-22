import tkinter as tk
import configuration
from unit import Board
import random

root = tk.Tk()
root.geometry(f'{configuration.WIDTH}x{configuration.HEIGHT}')
root.title("Mine game")         #מגדיר הגדרות ראשוניות 
root.resizable(False,False)



exit = tk.Button(root,text="Exit",command=lambda: root.destroy())
exit.place(x=1370,y=695)
gameframe = tk.Frame(root,width=200, height=150) # כפתור יציאה
gameframe.pack()

board = Board(configuration.MINES)

for x in range(configuration.ROWS): # לולאה שיוצרת כפתורים
   for y in range(configuration.COLUMNS):
        board.create_button(gameframe,x, y) # יוצר את הכפתור ומכניס אותם לאזור מסויים ומקבל ערכים של מיקום
        if x==7 and y==7:
            board.create_mines()

for x in range(configuration.ROWS): # לולאה שיוצרת כפתורים
   for y in range(configuration.COLUMNS):
        board.create_button2(x,y)


root.mainloop()

