import tkinter as tk
import PIL
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from array import array

## Stuff ##
file = ''
start = '<<DATA>>'
end = '<<END>>'
array = []

## Window elements ##
root = Tk()
root.title("Okayeg")
root.geometry('500x500')
iconimage =  ImageTk.PhotoImage(Image.open('4.ico'))
#root.tk.call('wm','iconphoto', root._w, iconimage)
img = ImageTk.PhotoImage(Image.open("4.png")) 
root.iconphoto(False, iconimage)



## Functions ##

def calclick1():
    global array
    root.filename = tk.filedialog.askopenfilename(initialdir = "/home/rooitier/Documents/honoursproj",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    lbl1f = tk.Label(root, text=root.filename).grid(row=1, column=6)
    txt_file = open(root.filename, 'r')
    
    # a = int(e1.get())
    # b = int(e2.get())
    with open(root.filename) as f:

        for line in f:
            array.append(line.strip())
    idx1 = array.index(start)
    idx2 = array.index(end)
    array = array[idx1+1:idx2]
    array = [int(x) for x in array]

def calclick2():
    global array
    a = int(e1.get())
    b = int(e2.get())
    n = len(array)
    x = list(range(n))
    y = array
    aspline = InterpolatedUnivariateSpline(x,y,k=2)
    area = aspline.integral(a,b)
    print(area)  


def tarclick1():
    root.filename = tk.filedialog.askopenfilename(initialdir = "/home/rooitier/Documents/honoursproj",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    lbl1f = tk.Label(root, text=root.filename).grid(row=5, column=6)








## Labels ##

lbl1 = tk.Label(text="Calibration" ).grid(row=1, column=0)
lbl1a = tk.Label(text="a = ").grid(row=1, column = 2)
lbl1b = tk.Label(text="b = ").grid(row=1, column = 4)


lbl2 = tk.Label(text="Target").grid(row=5, column=0)
lbl2a = tk.Label(text="a = ").grid(row=5, column = 2)
lbl2b = tk.Label(text="b = ").grid(row=5, column = 4)


## Buttons ##

btn1 = tk.Button(root, text="Open File", command = calclick1)
btn1.grid(row=1, column=1)
btn12 = tk.Button(root, text="Open File", command = tarclick1)
btn12.grid(row=5, column=1)
btn3 = tk.Button(root, text="print", command = calclick2)
btn3.grid(row=6,column=1)

## Entry Boxes ##

e1 = tk.Entry(root, width = 5)
e1.grid(row=1, column = 3)
e2 = tk.Entry(root, width = 5)
e2.grid(row=1, column = 5)


e11 = tk.Entry(root, width = 5)
e11.grid(row=5, column = 3)
e22 = tk.Entry(root, width = 5)
e22.grid(row=5, column = 5)


root.mainloop()
