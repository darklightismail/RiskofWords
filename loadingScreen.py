import random
import string
import subprocess
import time
import tkinter as tk
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
            self.delay =int( im.info['duration']/3)
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
lbl.load('loading.gif')
root.geometry("800x400")
root.title('Risk of Words')
import time
from tkinter import *
from tkinter import messagebox
f = ("Arial",10)
hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("5")
second.set("00")

hour_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=hour
)

# hour_tf.place(x=0,y=10)

mins_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=minute)

# mins_tf.place(x=50,y=10)

sec_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=second)

# sec_tf.place(x=100,y=10)


def startCountdown():
    try:
        userinput = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while userinput > -1:
        mins, secs = divmod(userinput, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(0.001)

        if (userinput == 0):
            # messagebox.showinfo("Time's Up", "Votre Score est : %d")
            root.destroy()
            subprocess.call(
                ["python", "menuGeneral.py"])

        userinput -= 1
startCountdown()


root.mainloop()
