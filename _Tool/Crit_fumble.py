#Import everything from tkinter
from tkinter import *
import random
import ctypes

#Create Windows object
window=Tk()
window.title('Crit & Fumble')
window.geometry("200x80")
window.attributes('-toolwindow', True)

import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

def CritMessage(i):
    message = ""
    if i < 32:
        message = "Standard Critical"
    elif i < 63:
        message = "+2 Damage, pre-multiplier"
    elif i < 65:
        message = "Critical multiplier +1"
    elif i < 68:
        message = "Apply critical dmg to shield"
    elif i < 70:
        message = "-4 AC"
    elif i == 70:
        message = "-10 AC"
    elif i < 73:
        message = "Stun 1D4-1 rnds"
    elif i == 73:
        message = "Stun 2 rnds"
    elif i == 74:
        message = "Silenced 1D4 Hours"
    elif i == 75:
        message = "15% Miss chance"
    elif i == 76:
        message = "50% Miss chance"
    elif i == 77:
        message = "Blindness 1D4 rounds"
    elif i == 78:
        message = "-10 Move"
    elif i == 79:
        message = "-20 MOve"
    elif i == 80:
        message = "-1D4 next (min 2)"
    elif i == 81:
        message = "-10 Move, -4 Dex"
    elif i == 82:
        message = "-2 AB, No shield"
    elif i < 86:
        message = "Bleed 3+HD damage per turn"
    elif i == 87:
        message = "-6 AB"
    elif i == 88:
        message = "No action 1D4 rounds"
    elif i == 89:
        message = "Loose all dex to AC"
    elif i == 90:
        message = "Drop a random item"
    elif i == 91:
        message = "-10 All Roll for 2 turn"
    elif i == 92:
        message = "+4 Critical Modifier"
    elif i == 93:
        message = "Fall unconscious"
    elif i == 94:
        message = "No spell for 1D4 turn"
    elif i == 95:
        message = "Half action"
    elif i == 96:
        message = "Sever leg"
    elif i == 97:
        message = "Throat cut, DC 20 or so"
    elif i == 98:
        message = "Throat cut, DC 25 or die"
    elif i == 99:
        message = "Decapitation DC 30, 25% hp if fail"
    elif i == 100:
        message = "Decapitation DC 35, 50% hp if fail"
    else:
        message = "ERROR"
        
    return message

def FumMessage(i):
    message = ""
    if i < 32:
        message = "Standard Fumble"
    elif i < 63:
        message = "Deal yourself 2D8 damages"
    elif i < 65:
        message = "Shaken for 4 turns"
    elif i < 68:
        message = "Fall last in the initiative"
    elif i < 70:
        message = "Fall into fear for 1 round"
    elif i == 70:
        message = "Attack another adjacent friendly"
    elif i < 73:
        message = "Weapon fall on the groundss"
    elif i == 73:
        message = "Weapon fall D4 square away"
    elif i == 74:
        message = "Weapon stuck on ground DC 22 Strength"
    elif i == 75:
        message = "Ignore your next critical hit this fight"
    elif i == 76:
        message = "50% Miss chance"
    elif i == 77:
        message = "All enemy gain +3 Dmg"
    elif i == 78:
        message = "All enemy gain +2 AC"
    elif i == 79:
        message = "All enemy gain +2 AB"
    elif i == 80:
        message = "-1D4 next (min 2)"
    elif i == 81:
        message = "Next attack receive this turn is a critical"
    elif i == 82:
        message = "Self damage"
    elif i < 86:
        message = "Loose 50% move speed, 4 turns"
    elif i == 87:
        message = "Self stun for 1D4 – 1 rnds (Min 1)"
    elif i == 88:
        message = "Blind for 4 turns"
    elif i == 89:
        message = "50% attack miss for 4 turns"
    elif i == 90:
        message = "Self damage x2"
    elif i == 91:
        message = "-5 AB for the 6 turns"
    elif i == 92:
        message = "Inflict only 50% dmg for 4 turns"
    elif i == 93:
        message = "Weapon break -1 enhancement"
    elif i == 94:
        message = "Crit yourself"
    elif i == 95:
        message = "Muted"
    elif i == 96:
        message = "Can’t inflict critical for 10 turns"
    elif i == 97:
        message = "Consider flat footed for 4 turns"
    elif i == 98:
        message = "Self-confused for 2 turns"
    elif i == 99:
        message = "Reroll twice"
    elif i == 100:
        message = "Limited to a standard action for the fight"
    else:
        message = "ERROR"
        
    return message
  
def rollCrit():
    #Variable
    Result = ""
    rollnum = random.randrange(1, 100)
    
    result = CritMessage(rollnum)
    ctypes.windll.user32.MessageBoxW(0, result, "Critical, rolled a " + str(rollnum) + ".", 0)
        
    #Clear shit
    CriticalRoll.set("")
    FumbleRoll.set("")

def rollFum():
    #Variable
    Result = ""
    rollnum = random.randrange(1, 100)
    
    result = FumMessage(rollnum)
    ctypes.windll.user32.MessageBoxW(0, result, "Fumble, rolled a " + str(rollnum) + ".", 0)
        
    #Clear shit
    CriticalRoll.set("")
    FumbleRoll.set("")
    
def roll():
    #Variable
    crit = e1.get()
    fum = e2.get()
    Result = ""
    
    if crit != "":
        result = CritMessage(int(crit))
        ctypes.windll.user32.MessageBoxW(0, result, "Critical", 0)
    if fum != "":
        result = FumMessage(int(fum))
        ctypes.windll.user32.MessageBoxW(0, result, "Fumble", 0)
       
    #Test
    #print()
        
    #Clear shit
    CriticalRoll.set("")
    FumbleRoll.set("")
    
    #Debug
    #print("End")

#define Entries
CriticalRoll=StringVar()
e1=Entry(window,textvariable=CriticalRoll, width=12, justify="center")
e1.grid(row=0,column=1)

FumbleRoll=StringVar()
e2=Entry(window,textvariable=FumbleRoll, width=12, justify="center")
e2.grid(row=1,column=1)

#define buttons
b1=Button(window, text="Critical", width=12,  command=lambda: rollCrit())
b1.grid(row=0,column=0)

b2=Button(window, text="Fumble", width=12, command=lambda: rollFum())
b2.grid(row=1,column=0)

b3=Button(window, text="Roll", width=12, command=lambda: roll())
b3.grid(row=3,column=1)

window.mainloop()
