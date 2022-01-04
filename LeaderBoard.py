import os
import random
import string
import subprocess
import time
import tkinter as tk
from tkinter import ttk

import numpy as np
# photo_path = "RISK OF  WORDS/loading.gif"
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay =int( im.info['duration'])
        except:
            self.delay = 10

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('RISK OF  WORDS/sit.gif')
root.geometry("600x600")
root.configure(background="#262626")
root.title('Risk of Words')
btn0 = tk.Label(root, text="", font="riskofrainsquare", width=20, height=1, bg="#262626", activebackground="#262626")
btn0.pack()
from tkinter import *
game_frame = Frame(root, width=800, height=800)
game_frame.place(x=40,y=10)

# scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set, )

my_game.place(x=0,y=0)

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('Id', 'Name', 'Age', 'higestScore')

# format our column
my_game.column("#0", width=0, stretch=NO)
my_game.column("Id", anchor=CENTER, width=100)
my_game.column("Name", anchor=CENTER, width=100)
my_game.column("Age", anchor=CENTER, width=100)
my_game.column("higestScore", anchor=CENTER, width=200)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("Id", text="Id", anchor=CENTER)
my_game.heading("Name", text="Name", anchor=CENTER)
my_game.heading("Age", text="Age", anchor=CENTER)
my_game.heading("higestScore", text="higestScore", anchor=CENTER)

scores = []
if (os.path.isfile('RISK OF  WORDS/leaderboard.txt') == True):
    fout = open("RISK OF  WORDS/leaderboard.txt", 'r')
    for line in fout:
        currentline = line.split(",")

        scores.append(currentline)


else:
    scores.append(0)

print(scores)
print(scores[0][0])
print(scores[0][1])
print(scores[0][2])

for i in range(len(scores)):
    my_game.insert(parent='', index='end', iid=i, text='',
                   values=(i, scores[i][0], scores[i][1], scores[i][2]))

# # add data
# my_game.insert(parent='', index='end', iid=0, text='',
#                values=('4', 'Ninja','18', '101'))
# my_game.insert(parent='', index='end', iid=1, text='',
#                values=('5', 'Ranger','18', '102'))
# my_game.insert(parent='', index='end', iid=2, text='',
#                values=('6', 'Deamon','18', '103'))
# my_game.insert(parent='', index='end', iid=3, text='',
#                values=('7', 'Dragon','18', '104'))


style = ttk.Style()


def to_main():
    root.destroy()
    subprocess.call(["python", "RISK OF  WORDS/menuGeneral.py"])


style.configure("Treeview", font=("riskofrainsquare", 11), bg="White")
style.configure("Treeview.Heading", font=("riskofrainsquare", 13), bg="White")
my_game.pack()
btn4 = tk.Button(root, text="Back to MAIN", font="riskofrainsquare", width=20, height=1, bg="White",
                 activebackground="#fa7731", command=to_main)
btn4.place(x=180, y=500)
btn5 = tk.Button(root, text="Exit", font="riskofrainsquare", width=20, height=1, bg="White", activebackground="#FF0000",
                 command=root.destroy)
btn5.place(x=180, y=550)

root.mainloop()
