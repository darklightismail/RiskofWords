import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

def conf():
    return varage


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


def to_main():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/menuGeneral.py"])



def to_play():
    root.destroy()
    if(varage<=12):
        subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/easy.py"])
    if (13 < varage < 18):
        subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/medium.py"])
    if (varage > 18):
        subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/hard.py"])
varage=0
varname=""
leaderboardlist=[]
leaderstring=""
def confirm():
    global varage,leaderstring
    varage =  int(age.get())
    varname=name.get()
    print(varage,varname)
    if (os.path.isfile('C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt') == True):
        fout = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt", 'r')
        for line in fout:
            currentline = line.split(",")
            if(varname!=currentline[0]):
                leaderboardlist.append(currentline)
                leaderstring = leaderstring + str(currentline)
        print(varname)

        fil = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt", 'w')
        fil.write(varname + "," + str(varage)+",0"+'\n')
        for r in leaderboardlist:
             fil.write(str(r[0])+","+str(r[1])+",0")

    else:
        fil = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt", 'w')
        fil.write(varname + "," + str(varage) +","+'0'+'\n')



root = tk.Tk()
root.title('Risk of Words')
lbl = ImageLabel(root)
lbl.pack()
lbl.load('C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/fallingstars.gif')
root.configure(background="#262626")
root.geometry("720x360")

btn1 = tk.Button(root, text="Enter Your Name :", font="riskofrainsquare", width=20, height=1, bg="white",
                 activebackground="#a0fa4c", )
btn1.place(x=30, y=20)
name = tk.Entry(root, text="Enter Your Name :", font="riskofrainsquare", width=20, bd=5)
name.place(x=300, y=20)
btn2 = tk.Button(root, text="Age :", font="riskofrainsquare", width=20, height=1, bg="White",
                 activebackground="#f4ca60")
btn2.place(x=30, y=80)
age = tk.Entry(root, text="Age :", font="riskofrainsquare", width=20, bd=5)
age.place(x=300, y=80)
btn0 = tk.Button(root, text="Confirm", font="riskofrainsquare", width=20, height=1, bg="White", activebackground="#37d3ff",command=confirm)
btn0.place(x=230, y=120)

btn3 = tk.Button(root, text="PLAY", font="riskofrainsquare", width=20, height=1, bg="White", activebackground="#37d3ff",command=to_play)
btn3.place(x=230, y=200)
btn4 = tk.Button(root, text="Back to MAIN", font="riskofrainsquare", width=20, height=1, bg="White", activebackground="#fa7731", command=to_main)
btn4.place(x=230, y=280)
btn5 = tk.Button(root, text="Exit", font="riskofrainsquare", width=20, height=1, bg="White", activebackground="#FF0000",command=root.destroy)
btn5.place(x=230, y=320)


root.mainloop()
