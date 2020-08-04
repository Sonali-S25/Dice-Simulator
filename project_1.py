import tkinter as tk
import random
from tkinter import *
from PIL import Image,ImageTk
def roll():
    img = PhotoImage(file = "dice1.png")
    img1 = PhotoImage(file = "dice2.png")
    img2 = PhotoImage(file = "dice3.png")
    img3 = PhotoImage(file = "dice4.png")
    img4 = PhotoImage(file = "dice5.png")
    img5 = PhotoImage(file = "dice6.png")
    no = random.randint(1,6)
    if no == 1:
        n=img1
    if no == 2:
        n=img1
    if no == 3:
        n=img2
    if no == 4:
        n=img3
    if no == 5:
        n=img4
    if no == 6:
        n=img5
    imglabel = Label(root, image=n)
    imglabel.image=n
    imglabel.place(x=20, y=20)        
root=tk.Tk()
root.title("Dice Roll")
button1 = tk.Button(root,text="Roll", command=roll)
button1.pack()
button2 = tk.Button(root,text="Quit", command=root.destroy)
button2.pack()
root.mainloop()
