#Import everything from tkinter
from tkinter import *
import random
import ctypes
import secrets

#Create Windows object
window=Tk()
window.title('Fall damage')
window.geometry("200x80")
window.attributes('-toolwindow', True)
    
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    
def roll():
    #Variable
    wgt = e1.get()
    dist = e2.get()
    Multipler = 1    
           
    #Calculate damage    
    if wgt == "":
        Multipler = 1
    else:
        Multipler = int(wgt)/200
    print(Multipler)
    Multipler = round(Multipler)
    print(Multipler)
    
    
    D6 = round(int(dist)/10)
    if D6 > 20:
        D6 = 20
    
    D6Result = 0
    D6PosResult = ['1', '2', '3', '4', '5', '6']
    i = 1
    while i != D6:
        D6Result = D6Result + int(secrets.choice(D6PosResult))
        i += 1
    
    result = D6Result * Multipler
    
    #Test
    #print(str(Multipler))
    #print(str(D6))
    #print(str(D6Result))
    ctypes.windll.user32.MessageBoxW(0, str(result) + " damage.", "Result", 0) 
        
    #Clear shit
    wgtValue.set("")
    distValue.set("")
    
def Note():
    ctypes.windll.user32.MessageBoxW(0, "Padded 10lb" + "\n" + 
                                     "Leather 15lb" + "\n" +
                                     "Studded leather 20lb" + "\n" +
                                     "Chain shirt 25lb" + "\n" +
                                     "Hide 25lb" + "\n" +
                                     "Scale mail 30lb" + "\n" +
                                     "Chainmail 40lb" + "\n" +
                                     "Breastplate 30lb" + "\n" +
                                     "Splint mail 35lb" + "\n" +
                                     "Banded mail 35lb" + "\n" +
                                     "Half-plate 50lb" + "\n" +
                                     "Full plate 50lb" + "\n" +
                                     "Buckler 5lb" + "\n" +
                                     "Medium shield 6-15lb" + "\n" +
                                     "Tower shield 45lb" + "\n" , "Weight note",0) 
    
#define Entries
wgtValue=StringVar()
e1=Entry(window,textvariable=wgtValue, width=12, justify="center")
e1.grid(row=0,column=1)

distValue=StringVar()
e2=Entry(window,textvariable=distValue, width=12, justify="center")
e2.grid(row=1,column=1)

#define buttons
b1=Button(window, text="Weight", width=12, state=DISABLED)
b1.grid(row=0,column=0)

b2=Button(window, text="Distance", width=12, state=DISABLED)
b2.grid(row=1,column=0)

b3=Button(window, text="Calculate", width=12, command=lambda: roll())
b3.grid(row=3,column=1)

b4=Button(window, text="Note", width=12, command=lambda: Note())
b4.grid(row=3,column=0)

window.mainloop()
