import subprocess
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
            self.delay = im.info['duration']
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
root.title('Risk of Words')
lbl = ImageLabel(root)
lbl.pack()
lbl.load('test.gif')
root.configure(background="#262626")
root.geometry("600x600")


def to_inputscreen():
    root.destroy()
    subprocess.call(["python", "InputScreen.py"])
def to_customgame():
    root.destroy()
    subprocess.call(["python", "CustomGame.py"])
def to_leaderboard():
    root.destroy()
    subprocess.call(["python", "LeaderBoard.py"])
btn1=tk.Button(root, text="New Player",font="riskofrainsquare", width=20, height=2, bg="white",	activebackground="#a0fa4c",command=to_inputscreen)
btn1.pack()
btn2=tk.Button(root, text="CUSTOM GAME",font="riskofrainsquare", width=20, height=2, bg="White", activebackground="#f4ca60",command=to_customgame)
btn2.pack()
btn3=tk.Button(root, text="LEADERSHIP BOARD",font="riskofrainsquare", width=20, height=2, bg="White", activebackground="#37d3ff",command=to_leaderboard)
btn3.pack()
btn4=tk.Button(root, text="Exit",font="riskofrainsquare", width=20, height=2, bg="White",activebackground="#FF0000",command=root.destroy)
btn4.pack()
root.mainloop()
