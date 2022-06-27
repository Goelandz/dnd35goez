#Import everything from tkinter
from tkinter import *
from tkinter import Menu
import random
import ctypes
import math

#Create Windows object
window=Tk()
window.title('Falling Damage')
window.geometry("218x254")
window.resizable(False, False)

#pop up
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

#Menu with information
menubar = Menu(window)
window.config(menu=menubar)

# create a menu
file_menu = Menu(menubar, tearoff=False)

# add a menu item to the menu
file_menu.add_command(label='How it work?', command=lambda: Help())
file_menu.add_command(label='Falling Rule PC', command=lambda: HelpRule())
file_menu.add_command(label='Falling Rule Object', command=lambda: HelpRuleObject())
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.destroy)

# add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

#Help menu
def Help():
    ctypes.windll.user32.MessageBoxW(0, "Simply enter either the 'Player distance' or enter the 'Object Weight & Object Distance', then click 'Calculate'", "How does it work?", 0)
#Help menu
def HelpRule():
    ctypes.windll.user32.MessageBoxW(0, "A character that fall take 1D6 damage per 10ft up to 20D6."+"\n"+"\n"+
                                     "A character that jump on purpose can attemps to do a DC 15 Jump or Tumble to ignore the fist 10ft and turn the second 10ft into nonlethal damage."+"\n"+"\n"
                                     "Soft ground will modify the first 1D6 damage receive unto nonlethal. (Cumulative with Jump/Tumble)"+"\n"+"\n"
                                     
                                     "A character that fall on water receive no damage for the first 20ft."+"\n"+
                                     "Then receive 1D3 nonlethal damage per 10ft for the next 20ft."+"\n"+"\n"+
                                     
                                     "A character that dive can do a DC 15 Swim or Tumble as long the water is at least 10ft deep for each 30ft fallen."+"\n"
                                     "That DC is increased by 5 for each 50ft"+"\n"
                                     , "Falling Rule PC"
                                     , 0)
def HelpRuleObject():
    ctypes.windll.user32.MessageBoxW(0, "An Object inflict 1D6 point of damage for each 200 lbs for each 10ft fallen. Up to a maximum of 20D6 damage"+"\n"+"\n"+
                                     "Object that has less then 200lbs must fall farther to deal the same damage"+"\n"
                                     , "Falling Object Rule"
                                     , 0)

#We calculate the damage, 
#Object damage won't have the priority, only the PC if both entry are enter.
#GOnna specify it on the pop up
def roll():
    iDistObject = e2.get()
    iDistObject = int(iDistObject)
    iWeightObject = e1.get()
    iWeightObject= int(iWeightObject)
    iObjectReqHeight = 10
    
    if (iDistObject != "") & (iWeightObject != ""):
        #Lets see how we calculate the damage
        if iWeightObject < 5:
            iObjectReqHeight = 70
        elif iWeightObject < 10:
            iObjectReqHeight = 60
        elif iWeightObject < 30:
            iObjectReqHeight = 50
        elif iWeightObject < 50:
            iObjectReqHeight = 40
        elif iWeightObject < 100:
            iObjectReqHeight = 30
        elif iWeightObject < 200:
            iObjectReqHeight = 20
        
        #Lets not forget >200, anything else should be 10 by default
        iObjectDie = math.floor(iDistObject / iObjectReqHeight)
        iObjectDieDmg = 0
        print("Dice amount: "+ str(iObjectDie))
        
        #Max 20d6
        if iObjectDie > 20:
            iObjectDie = 20
        
        v = iObjectDie
        while v > 0:
            v = v - 1
            iObjectDieDmg = iObjectDieDmg + random.randrange(1, 6)

        ctypes.windll.user32.MessageBoxW(0, "The Object target receive: "+str(iObjectDieDmg)+" damage.", "Result", 0)

        
        #We know the weight Dist required
        print("Weight class: "+ str(iObjectReqHeight))
        print("Dice amount: "+ str(iObjectDie))
        print("DMG: "+ str(iObjectDieDmg))
        print("=======================================")
            
        
    iHeight = e3.get()
    if iHeight != "":
        iDieLethal = 0
        iDmgLethal = 0
        iDieNonlethal = 0
        iDmgD6NonLethal = 0
        iDie3NonLethal = 0
        iDmgD3NonLethal = 0

        #3 controller, suceed roll, soft ground and water
        iWater = vWater.get() #0 = FALSE
        iDC = vDC.get() #0 = FALSE
        iSoft = vSoft.get() #0 = FALSE
        x = 0

        print("===========================New Debug=================================")
        print("Height: " + str(iHeight))
        print("D6Lethal: " + str(iDieLethal))
        print("D6NonLethal: " + str(iDieNonlethal))
        print("D3NonLethal: " + str(iDie3NonLethal))
        print("HasWater: " + str(iWater))
        print("SuceedDC: " + str(iDC))
        print("SoftGrnd: " + str(iSoft))

        #Nonwater jump
        if iWater == 0:
            print("No Water")
            #We are on water, 2 modifier soft ground and jump on soft
            iDieLethal = int(iHeight) / 10
            print("iDieLethal = "+str(iDieLethal))
            if iDieLethal > 20: #Max 20d6
                iDieLethal = 20

            print("iDieLethal2 = "+str(iDieLethal))
            if iDC == 1:
                if iDieLethal >= 1:
                    iDieLethal = iDieLethal - 1 #We reduce the Die by 1.
                    print("reduce die by 1 DC suceed")
                if iDieLethal >= 1:
                    iDieLethal = iDieLethal -1 #We switch a lethal die into a nonlethal
                    print("we reduce lethal die again by 1 and increase nonlethal by 1")
                    iDieNonlethal = iDieNonlethal + 1
            if iSoft == 1: #soft? We reduce
                if iDieLethal >= 1:
                    iDieLethal = iDieLethal -1 #We switch a lethal die into a nonlethal
                    print("we reduce lethal die again by 1 and increase nonlethal by 1")
                    iDieNonlethal = iDieNonlethal + 1
         #Water jump
            print("iDieLethal3 = "+str(iDieLethal))
            print("iDieNonLethal3 = "+str(iDieNonlethal))
        else:
            iDieLethal = int(iHeight) / 10
            iDieLethal = iDieLethal - 2 #We always ignore the first 20ft
            print("water time1")

            if iDC == 0: #well...
                print("water time2")
                if iDieLethal >= 1: #Okay that a jump of 30+ft we continue
                    if iDieLethal <= 2: #1d3 nonlethal for those.
                        iDie3NonLethal = iDieLethal
                        iDieLethal = 0
                        print("nonlethal water added")
                    else:
                        #we have more then 2, so the first are 1d3 nonlethal
                        iDieLethal = iDieLethal - 2
                        iDie3NonLethal = 2
                        print("lethal water added")
            else:
                print("water time3")
                iDieLethal = 0
                iDie3NonLethal = 0
                iDieNonlethal = 0

        print("Height: " + str(iHeight))
        print("D6Lethal: " + str(iDieLethal))
        print("D6NonLethal: " + str(iDieNonlethal))
        print("D3NonLethal: " + str(iDie3NonLethal))
        print("HasWater: " + str(iWater))
        print("SuceedDC: " + str(iDC))
        print("SoftGrnd: " + str(iSoft))           

        #Calculation of damage!
        z = iDie3NonLethal
        while z > 0:
            #print("Loop: D3NonLethal: " + str(iDie3NonLethal))
            z = z - 1
            iDmgD3NonLethal = iDmgD3NonLethal + random.randrange(1, 3)  
              
        x = iDieLethal
        while x > 0:
            x = x - 1
            iDmgLethal = iDmgLethal + random.randrange(1, 6)
            
        y = iDieNonlethal
        while y > 0:
            y = y - 1
            iDmgD6NonLethal = iDmgD6NonLethal + random.randrange(1, 6)

            
        print("Dmg:" + str(iDmgLethal))                
        print("DmgNonlethal:" + str(iDmgD6NonLethal))               
        print("DmgD3:" + str(iDmgD3NonLethal))   
        
        ctypes.windll.user32.MessageBoxW(0, "The character receive: "+str(iDmgLethal)+" regular damage and: "+str(iDmgD3NonLethal+iDmgD6NonLethal)+" non-lethal damage", "Result", 0)
        #vAlignClassTest = secrets.choice(iAlignClass)

#Lets automatically update the DC
def key_pressed(event):
    #print('Tim')
    iValueDC = e3.get()
    if iValueDC != "":
        iValueDC = int(iValueDC)
        iDC = 15
        iInc = 0
    
    #We update the DC only if its more than 49 ft
        if iValueDC >= 50:
            iInc = iValueDC / 50
            iInc = round(iInc) * 5
            print("Rounded value "+str(iInc))
            iDC = iInc + iDC
        else:
            iDC = 15
    
        vb5.set("DC "+str(iDC)+" Swim/Tumble")

            
#define Entries
ObjectWeight=StringVar()
e1=Entry(window,textvariable=ObjectWeight, width=12, justify="center")
e1.grid(row=0,column=1)

ObjectDist=StringVar()
e2=Entry(window,textvariable=ObjectDist, width=12, justify="center")
e2.grid(row=1,column=1)

PCDist=StringVar()
e3=Entry(window,textvariable=PCDist, width=12, justify="center")
e3.grid(row=2,column=1)
e3.bind('<KeyRelease>', key_pressed)

#define buttons
b1=Button(window, text="Object Weight", width=12, state = DISABLED)
b1.grid(row=0,column=0)

b2=Button(window, text="Object Distance", width=12, state = DISABLED)
b2.grid(row=1,column=0)

b1=Button(window, text="Player Distance", width=12, state = DISABLED)
b1.grid(row=2,column=0)

b3=Button(window, text="Calculate", width=12, command=lambda: roll())
b3.grid(row=3,column=0, columnspan=2)

b4=Button(window, text="On Water", width=12, state = DISABLED)
b4.grid(row=6,column=0)

vb5=StringVar()
b5=Label(window, textvariable=vb5, text="DC 15 Swim/Tumble", width=16, relief=GROOVE)
b5.grid(row=6,column=1)

b6=Button(window, text="On ground", width=12, state = DISABLED)
b6.grid(row=5,column=0)

b7=Button(window, text="DC 15 Jump/Tumble", width=16, state = DISABLED)
b7.grid(row=5,column=1)

#Spacer
s1=Label(window, text=" ", width=16)
s1.grid(row=4,column=1, columnspan=2)

#CheckBox
vDC=IntVar()
x1=Checkbutton(window,text="Succeed Check?", variable=vDC)
x1.grid(row=7,column=0, columnspan=2)

vSoft=IntVar()
x2=Checkbutton(window,text="Soft Ground?", variable=vSoft)
x2.grid(row=8,column=0, columnspan=2)

vWater=IntVar()
x3=Checkbutton(window,text="Fall on water?", variable=vWater)
x3.grid(row=9,column=0, columnspan=2)

window.mainloop()
