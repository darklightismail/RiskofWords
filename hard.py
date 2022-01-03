import os
import random
import string
import subprocess
import tkinter as tk
import numpy as np

w=[]
score=[]


def to_main():
    root.destroy()
    subprocess.call(["python", "C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/menuGeneral.py"])

def anwser_verification(answer_dict):
    global word_find
    global w
    global score
    is_done = True
    for i in range(len(word_find)):
        if (answer_dict[i].cget("text") != ""):
            pass
        else:
            is_done = False
    if (is_done):
        for i in range(len(word_find)):
            listletter.append(answer_dict[i].cget("text"))
            madeword = "".join(listletter)
            answer_dict[i].grid_forget()

        print("cest bon", madeword)



        if (len(w)==len(wordlist)-2):
            w.clear()

        else:
            w.append(1)

        text.delete(0, tk.END)
        text.insert(0, wordlist[len(w)][0])

        word_find=wordlist[len(w)][0]
        print('word to FIND : ',word_find,'LENGTH OF W :',len(w),'LENGTH OF WORDLIST:',len(wordlist)-1)
        button_name(btn_dict)
        case_rep(len(word_find))
        score.append(1)
        scoretext.config(text=str(len(score)*10))







wordlist = [] #import word list
file = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/medium.txt").readlines()
print(file)
for line in file:
    currentline = line.split(",")
    wordlist.append(currentline)
print(wordlist)
print('length of the word list : ',len(wordlist))

def text_update(letter):  # niveau facile auto fill words.

    text.delete(0, tk.END)
    text.insert(0, wordlist[0][0])



    print("NEW -------------------------------------")
    print(letter)
    for i in range(len(word_find)):
        if (letter == word_find[i]):
            # answer_dict[i].delete(0, tk.END)
            # answer_dict[i].insert(0, letter)
            answer_dict[i].config(text=letter)
            anwser_verification(answer_dict)
            # if(answer_dict[i].cget("text")!="" ):
            #     print("cest bon",answer_dict[i].cget("text"))

    # listletter.append(letter)
    # madeword = "".join(listletter)

    # if(madeword==word_find):
    #          print("well done")
    # else:
    #     print("NOT YET"+str(len(listletter)))
    # print(listletter)
    # print(answer_dict)


root = tk.Tk()
root.title('Risk of Words')
root.geometry("800x550")


import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/rain.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0,y=0)

# root.resizable(False, False)

text = tk.Entry(root, width=15,font="riskofrainsquare", bg='lightgreen')
text.grid(row=0, column=0, columnspan=6, sticky='')
scoretext = tk.Label(root,text="",font="riskofrainsquare",bg="yellow", height=1, width=5)
scoretext.grid(row=0, column=5, pady=10, padx=10, sticky='')
scoretext.config(text=0)
userlist=[]
######BRING NAME OF USER
fout = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt", 'r')
for line in fout:
    currentline = line.split(",")
    userlist.append(currentline)
btna=tk.Button(root, text=userlist[0][0],font="riskofrainsquare", width=5, height=1, bg="White",activebackground="#FF0000")
btna.grid(row=0, column=4)
btna=tk.Button(root, text="HARD",font="riskofrainsquare", width=7, height=1, bg="#37d3ff",activebackground="#FF0000")
btna.grid(row=0, column=10)



listletter = []
madeword = ""
btn_dict = {}
btn_dict0 = {}
btn_dict1 = {}
btn_dict2 = {}
btn_dict3 = {}
btn_dict4 = {}
answer_dict = {}
row0 = 1
cpt = 0
# alphabet_string = string.ascii_lowercase
# letters = list(alphabet_string)
# newletters = random.sample(letters, len(letters))
# word_find="dad" #the word u wanna find !
newletters = ()
# letters = list(word_find)
alphabet_string = string.ascii_lowercase
letters = list(alphabet_string) + list("aeouiy")

word_find = wordlist[len(w)][0]   # FIND WORD OF LIST !!!


print(len(word_find))
# root.columnconfigure(0, weight=10)
# root.columnconfigure(1, weight=10)
randletters = random.sample(letters, 30 - len(word_find))
new = randletters + list(word_find)
random.shuffle(new)
print(new)
listalpha = new


# def button_name(btn_dict0,col): #placing buttons in the screen
#  row0=1
#  newletters = random.sample(letters, len(letters))
#  for letter in newletters  :
#     # pass each button's text to a function
#     action = lambda x = letter: text_update(x)
#     # create the buttons and assign to animal:button-object dict pair
#     btn_dict0[letter] = tk.Button(root, text=letter, width=2, command=action)
#     btn_dict0[letter].grid(row=row0, column=col,pady=20,padx=20)
#     row0 += 1
#     if( row0==6):
#         break
def button_name(btn_dict):  # placing buttons in the screen
    randletters = random.sample(letters, 30 - len(word_find))
    new = randletters + list(word_find)
    random.shuffle(new)
    col = 0
    row0 = 1
    # for letter in new:
    #     # pass each button's text to a function
    #     action = lambda x=letter: text_update(x)
    #     if (row0 < 6):
    #         # create the buttons and assign to animal:button-object dict pair
    #         btn_dict[letter] = tk.Button(root, text=letter, width=2, command=action)
    #         btn_dict[letter].grid(row=row0, column=col, pady=20, padx=20)
    #         row0 += 1
    #         if (row0 == 6):
    #             row0 = 1
    #             col += 1
    #         if (col == 6):
    #             break
    for letter in new:
        # pass each button's text to a function
        action = lambda x=letter: text_update(x)

        # create the buttons and assign to animal:button-object dict pair
        btn_dict[letter] = tk.Button(root, text=letter,font=("riskofrainsquare",9), width=2, command=action)
        btn_dict[letter].grid(row=row0, column=col, pady=20, padx=20)
        row0 += 1
        if (row0 > 5):
            row0 = 1
            col += 1


def case_rep(n):  # case des reponses of the user
    col = 0
    for i in range(n):
        # answer_dict[i] = tk.Entry(root, width=10, bg='yellow')
        answer_dict[i] = tk.Label(root,
                                  text="",font=("riskofrainsquare",9),
                                  bg="yellow", height=1, width=10)
        answer_dict[i].grid(row=10, column=col, pady=100, padx=10, sticky='')

        col += 1


button_name(btn_dict)
# button_name(btn_dict0,0)
# button_name(btn_dict1,1)
# button_name(btn_dict2,2)
# button_name(btn_dict0,3)
# button_name(btn_dict0,4)
# button_name(btn_dict0,5)
# case_rep(len(word_find))


# def move(i):
#    root.update()
#
#    if i<=350:
#             btn_dict[btn_list0[0]].place(y=i,x=36)
#             btn_dict[btn_list0[0]].after(10, lambda: move(i)) #after every 100ms
#             i = i+1
#
cpt = 0
btn_list = new
print(btn_list)


def disapear_animation(z, i, y):
    # root.update()
    btn_dict[btn_list[z]].grid_forget()

    if i <= 8:
        btn_dict[btn_list[z]].grid(row=i, column=y)
        btn_dict[btn_list[z]].after(1000, lambda: disapear_animation(z, i, y))  # after every 100ms
        i = i + 1
def hori_animation(z, i, y):
    # root.update()
    btn_dict[btn_list[z]].grid_forget()

    if y <= 8:
        btn_dict[btn_list[z]].grid(row=i, column=y)
        btn_dict[btn_list[z]].after(1000, lambda: hori_animation(z, i, y))  # after every 100ms
        y = y + 1

disapear_animation(29, 1, 8)
disapear_animation(20, 2, 9)
hori_animation(5, 7, 1)
hori_animation(2, 8, 0)
# print("this is alphabets words of alpha", btn_dict[listalpha[5]])
# disapear_animation(21,1,8)
print(btn_dict)
# btn_list=list(btn_dict)
# print(btn_list[5])
# print(btn_list[10])
case_rep(len(word_find))
# print(btn_dict0[btn_list0[0]].winfo_rootx())
# print("list answers from les cases : ")
# listanswer=list(answer_dict)
# print(listanswer[0])
# print("the label is", answer_dict[0]['text'])
import time
from tkinter import *
from tkinter import messagebox
f = ("Arial",10)
hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("01")
second.set("00")

hour_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=hour
)

hour_tf.place(x=0,y=10)

mins_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=minute)

mins_tf.place(x=50,y=10)

sec_tf = Entry(
    root,
    width=3,
    font=f,
    textvariable=second)

sec_tf.place(x=100,y=10)
leaderstring=""
leaderboardlist=[]
def startCountdown():
    global score,leaderboardlist,leaderstring
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
        time.sleep(1/100000)

        if (userinput == 0): #time is up
            messagebox.showinfo("Time's Up", "Votre Score est : %d" % int(scoretext.cget('text')))
            print("your score is : ",int(len(score)*10))
            fout = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt", 'r')
            for line in fout:
                    currentline = line.split(",")
                    leaderboardlist.append(currentline)
                    leaderstring = leaderstring + str(currentline)



            fil = open("C:/Users/dark/Desktop/WORK/MASTER SIM TAZA/S1/PYTHON/RISK OF  WORDS/leaderboard.txt",
                               'w')
            leaderboardlist[0][2]=max(eval(leaderboardlist[0][2]),int(len(score)*10))
            for r in leaderboardlist:
                        fil.write(str(r[0]) + "," + str(r[1])+ "," + str(r[2])+'\n')
            fil.close()
            to_main()


        userinput -= 1
        root.after(2000, text.delete(0, tk.END))#to make text disapear
startCountdown()














# run the GUI event loop
root.mainloop()
