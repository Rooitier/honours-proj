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
import math as mth


## Window elements ##

root = Tk()
root.title("Okayeg")
root.geometry('1000x300')
# iconimage =  ImageTk.PhotoImage(Image.open('4.ico'))
# root.tk.call('wm','iconphoto', root._w, iconimage)
# img = ImageTk.PhotoImage(Image.open("4.png")) 
# root.iconphoto(False, iconimage)

## Stuff ##

start = '<<DATA>>'
end = '<<END>>'
array = []
array1 = []
xdataarray = []
ydataarray = []
lamb = 0
lbl = tk.Label(root)
lblc = tk.Label(root)
lblt = tk.Label(root)
## Functions ##

def clear():
    global xdataarray, ydataarray, lbl, lamb
    xdataarray = []
    ydataarray =[]
    plt.clf()
    lbl.destroy()
    lamb = 0

def calclick1():
    clear()
    global array, lbl, lblc
    lblc.destroy()
    root.filename = tk.filedialog.askopenfilename(initialdir = "/home/rooitier/Documents/honoursproj",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    lblc = tk.Label(root, text=root.filename)
    lblc.grid(row=1, column=6)
    #txt_file = open(root.filename, 'r')
    
    # a = int(e1.get())
    # b = int(e2.get())
    with open(root.filename) as f:

        for line in f:
            array.append(line.strip())
    idx1 = array.index(start)
    idx2 = array.index(end)
    array = array[idx1+1:idx2]
    array = [int(x) for x in array]
    
    plt.plot(array)
    plt.xlabel('Energy [keV $ x 10^2$]')
    plt.ylabel('Counts [arb.]')
    plt.show()

def tarclick1():
    clear()
    global array1, lbl, lblt
    lblt.destroy()
    root.filename = tk.filedialog.askopenfilename(initialdir = "/home/rooitier/Documents/honoursproj",title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    lblt = tk.Label(root, text=root.filename)
    lblt.grid(row=2, column=6)
    #txt_file = open(root.filename, 'r')
    
    # a = int(e1.get())
    # b = int(e2.get())
    with open(root.filename) as f:

        for line in f:
            array1.append(line.strip())
    idx1 = array1.index(start)
    idx2 = array1.index(end)
    array1 = array1[idx1+1:idx2]
    array1 = [int(x) for x in array1]
    
    plt.plot(array1)
    plt.xlabel('Energy [keV $ x 10^2$]')
    plt.ylabel('Counts [arb.]')
    plt.show()
## Attenuation buttons ##

def attenclickli():
    clear()
    global xdataarray, ydataarray, lamb, lbl


    f = open('li','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickmg():
    clear()
    global xdataarray, ydataarray, lamb, lbl


    f = open('mg','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)       

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()
 
def attenclickal():
    clear()
    global xdataarray, ydataarray, lamb, lbl
    lbl.destroy()


    f = open('al','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclicksc():
    clear()
    global xdataarray, ydataarray, lamb, lbl
    lbl.destroy()

    
    f = open('sc','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickti():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('ti','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickcr():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('cr','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickmn():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('mn','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickfe():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('fe','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickco():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('co','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickni():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('ni','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickcu():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('cu','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickzn():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('zn','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickrh():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('rh','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickpd():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('pd','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickag():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('ag','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclicksn():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('sn','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickw():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('w','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickir():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('ir','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickpt():
    clear()
    global xdataarray, ydataarray, lamb, lbl

    
    f = open('pt','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()

def attenclickau():
    clear()
    global xdataarray, ydataarray, lamb, lbl


    f = open('au','r')
    a = float(atten.get())

    for line in f:
        line = line.strip()
        column = line.split()
        xdataarray.append(mth.log(float(column[0])))
        ydataarray.append(mth.log(float(column[1])))

    fit = np.polyfit(xdataarray,ydataarray,6)
    plotfit = np.poly1d(fit)
    lamb = mth.exp(plotfit(mth.log(a)))
    lbl = tk.Label(text = u'\u03BC / \u03C1'+' '+'='+' '+str(lamb))
    lbl.grid(row=3, column=6)   

    x_new = np.linspace(xdataarray[0],xdataarray[-1])
    y_new = plotfit(x_new)
    
    plt.plot(xdataarray,ydataarray,'o',x_new,y_new)
    plt.xlabel('log(Energy [MeV])')
    plt.ylabel(u'ln(\u03Bc [$cm^2/g$])')
    plt.show()


## Calculate thickness ##

def calclick2():
    global array, array1, lamb
    a = float(e1.get())
    b = float(e2.get())
    n = len(array)
    x = list(range(n))
    y = array
    aspline = InterpolatedUnivariateSpline(x,y,k=2)
    area = aspline.integral(a,b)
    
    a = float(e11.get())
    b = float(e22.get())
    n = len(array1)
    x = list(range(n))
    y = array1
    aspline = InterpolatedUnivariateSpline(x,y,k=2)
    area1 = aspline.integral(a,b)

    thick = -(mth.log(area1/area)/lamb)*10000
    lblth = tk.Label(root, text = str(thick)+' '+u'\u03BCm').grid(row=11, column=6)

## Labels ##

lbl1 = tk.Label(text="Calibration" ).grid(row=1, column=0)
lbl1a = tk.Label(text="a = ").grid(row=1, column = 2)
lbl1b = tk.Label(text="b = ").grid(row=1, column = 4)


lbl2 = tk.Label(text="Target").grid(row=2, column=0)
lbl2a = tk.Label(text="a = ").grid(row=2, column = 2)
lbl2b = tk.Label(text="b = ").grid(row=2, column = 4)

lbl3 = tk.Label(text="Energy (MeV) = ").grid(row=3,column=0)
## Buttons ##

btn1 = tk.Button(root, text="Open File", command = calclick1)
btn1.grid(row=1, column=1)
btn12 = tk.Button(root, text="Open File", command = tarclick1)
btn12.grid(row=2, column=1)
btn3 = tk.Button(root, text="Calculate", command = calclick2, width = 7)
btn3.grid(row=11,column=5)

## Atten buttons ##

btn4 = tk.Button(root, text="Li - 3", command = attenclickli, width = 7)
btn4.grid(row=7,column=1)
btn5 = tk.Button(root, text="Mg - 12", command = attenclickmg, width = 7)
btn5.grid(row=7,column=2)
btn6 = tk.Button(root, text="Al - 13", command = attenclickal, width = 7)
btn6.grid(row=7,column=3)
btn7 = tk.Button(root, text="Sc - 21", command = attenclicksc, width = 7)
btn7.grid(row=7,column=4)
btn8 = tk.Button(root, text="Ti - 22", command = attenclickti, width = 7)
btn8.grid(row=7,column=5)

btn9 = tk.Button(root, text="Cr - 24", command = attenclickcr, width = 7)
btn9.grid(row=8,column=1)
btn10 = tk.Button(root, text="Mn - 25", command = attenclickmn, width = 7)
btn10.grid(row=8,column=2)
btn11 = tk.Button(root, text="Fe - 26", command = attenclickfe, width = 7)
btn11.grid(row=8,column=3)
btn12 = tk.Button(root, text="Co - 27", command = attenclickco, width = 7)
btn12.grid(row=8,column=4)
btn13 = tk.Button(root, text="Ni - 28", command = attenclickni, width = 7)
btn13.grid(row=8,column=5)

btn14 = tk.Button(root, text="Cu - 29", command = attenclickcu, width = 7)
btn14.grid(row=9,column=1)
btn15 = tk.Button(root, text="Zn - 30", command = attenclickzn, width = 7)
btn15.grid(row=9,column=2)
btn16 = tk.Button(root, text="Rh - 45", command = attenclickrh, width = 7)
btn16.grid(row=9,column=3)
btn17 = tk.Button(root, text="Pd - 46", command = attenclickpd, width = 7)
btn17.grid(row=9,column=4)
btn18 = tk.Button(root, text="Ag - 47", command = attenclickag, width = 7)
btn18.grid(row=9,column=5)

btn19 = tk.Button(root, text="Sn - 50", command = attenclicksn, width = 7)
btn19.grid(row=10,column=1)
btn20 = tk.Button(root, text="W - 74", command = attenclickw, width = 7)
btn20.grid(row=10,column=2)
btn21 = tk.Button(root, text="Ir - 77", command = attenclickir, width = 7)
btn21.grid(row=10,column=3)
btn22 = tk.Button(root, text="Pt - 78", command = attenclickpt, width = 7)
btn22.grid(row=10,column=4)
btn23 = tk.Button(root, text="Au - 79", command = attenclickau, width = 7)
btn23.grid(row=10,column=5)
## Entry Boxes ##

e1 = tk.Entry(root, width = 7)
e1.grid(row=1, column = 3)
e2 = tk.Entry(root, width = 7)
e2.grid(row=1, column = 5)


e11 = tk.Entry(root, width = 7)
e11.grid(row=2, column = 3)
e22 = tk.Entry(root, width = 7)
e22.grid(row=2, column = 5)

atten = tk.Entry(root, width =7)
atten.grid(row =3, column=1)

root.mainloop()
