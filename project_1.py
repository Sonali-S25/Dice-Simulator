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
        imglabel = Label(root, image=img)
        imglabel.image=img
        imglabel.pack() 
    if no == 2:
        imglabel1 = Label(root, image=img1)
        imglabel1.image=img1
        imglabel1.pack()
    if no == 3:
        imglabel2 = Label(root, image=img2)
        imglabel2.image=img2
        imglabel2.pack()
    if no == 4:
        imglabel3 = Label(root, image=img3)
        imglabel3.image=img3
        imglabel3.pack()
    if no == 5:
        imglabel4 = Label(root, image=img4)
        imglabel4.image=img4
        imglabel4.pack()
    if no == 6:
        imglabel5 = Label(root, image=img5)
        imglabel5.image=img5
        imglabel5.pack() 
        
root=tk.Tk()
root.title("Dice Roll")
button1 = tk.Button(root,text="Roll", command=roll)
button1.pack()
button2 = tk.Button(root,text="Quit", command=root.destroy)
button2.pack()
root.mainloop()
  


        
          
