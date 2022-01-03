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
lbl.load('C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/blackhole.gif')
root.configure(background="#262626")
root.geometry("600x350")
def to_main():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/menuGeneral.py"])


def to_inputscreen():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/InputScreen.py"])

def to_easy():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/easy.py"])
def to_medium():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/medium.py"])

def to_hard():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/hard.py"])






btn0=tk.Button(root, text="CHOOSE THE DIFFICULTY YOU WANT : ",font="riskofrainsquare", width=40, height=2, bg="white",	activebackground="Orange")
btn0.place(x=50,y=10)
btn1=tk.Button(root, text="EASY",font="riskofrainsquare", width=12, height=2, bg="white",	activebackground="#a0fa4c",command=to_easy)
btn1.place(x=20,y=100)
btn2=tk.Button(root, text="MEDIUM",font="riskofrainsquare", width=12, height=2, bg="White", activebackground="#f4ca60",command=to_medium)
btn2.place(x=220,y=100)
btn3=tk.Button(root, text="HARD",font="riskofrainsquare", width=12, height=2, bg="White", activebackground="#37d3ff",command=to_hard)
btn3.place(x=420,y=100)
btn4 = tk.Button(root, text="Back to MAIN", font="riskofrainsquare", width=15, height=1, bg="White",
                 activebackground="#fa7731", command=to_main)
btn4.place(x=200, y=260)
btn5 = tk.Button(root, text="Exit", font="riskofrainsquare", width=15, height=1, bg="White", activebackground="#FF0000",
                 command=root.destroy)
btn5.place(x=200, y=300)
root.mainloop()