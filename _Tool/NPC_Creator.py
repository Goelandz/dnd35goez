#Import everything from tkinter
from tkinter import *
from tkinter import ttk
import secrets
import random
import math

window=Tk()
#window.geometry("550x820")
window.title('NPC Creator')



#Define empty label
l1=Label(window, text="Race")
l1.grid(row=2,column=1)
l1=Label(window, text="Class")
l1.grid(row=3,column=1)
l1=Label(window, text="-----------------------------------------------------------------------------------")
l1.grid(row=4,columnspan=6,column=1)
l1=Label(window, text="First Name", width=12)
l1.grid(row=5,column=1)
l1=Label(window, text="Last Name", width=12)
l1.grid(row=6,column=1)
l1=Label(window, text="Clan", width=12)
l1.grid(row=7,column=1)
l1=Label(window, text="Traits")
l1.grid(row=7,column=3)
l1=Label(window, text="Equipment", relief=RIDGE, width=40, bg="#00ffff")
l1.grid(row=9,column=1, columnspan=4)
l1=Label(window, text="Gold")
l1.grid(row=10,column=3)
l1=Label(window, text="Armor")
l1.grid(row=10,column=1)
l1=Label(window, text="Weapon")
l1.grid(row=21,column=5)
l1=Label(window, text="Save", relief=RIDGE, width=20, bg="#00ffff")
l1.grid(row=12,column=1, columnspan=2)
l1=Label(window, text="Statistic", relief=RIDGE, width=20, bg="#00ffff")
l1.grid(row=11,column=3, columnspan=2)
l1=Label(window, text="Will")
l1.grid(row=15,column=1)
l1=Label(window, text="Fort")
l1.grid(row=13,column=1)
l1=Label(window, text="Ref")
l1.grid(row=14,column=1)
l1=Label(window, text="Level")
l1.grid(row=2,column=4)
l1=Label(window, text="STR")
l1.grid(row=12,column=3)
l1=Label(window, text="DEX")
l1.grid(row=13,column=3)
l1=Label(window, text="CON")
l1.grid(row=14,column=3)
l1=Label(window, text="INT")
l1.grid(row=15,column=3)
l1=Label(window, text="WIS")
l1.grid(row=16,column=3)
l1=Label(window, text="CHA")
l1.grid(row=17,column=3)
l1=Label(window, text="Race")
l1.grid(row=5,column=3)
l1=Label(window, text="Common Race")
l1.grid(row=1,column=1)
l1=Label(window, text="Class")
l1.grid(row=6,column=3)
l1=Label(window, text="Level")
l1.grid(row=5,column=5)
l1=Label(window, text="Secondary")
l1.grid(row=22,column=5)
l1=Label(window, text="Height")
l1.grid(row=6,column=5)
l1=Label(window, text="Weight")
l1.grid(row=7,column=5)
l1=Label(window, text="Age")
l1.grid(row=8,column=5)
l1=Label(window, text="Job")
l1.grid(row=9,column=5)
l1=Label(window, text="Job2")
l1.grid(row=10,column=5)
l1=Label(window, text="Job3")
l1.grid(row=11,column=5)
l1=Label(window, text="Sex")
l1.grid(row=12,column=5)
l1=Label(window, text="Alignment")
l1.grid(row=13,column=5)
l1=Label(window, text="Skill (with Armor Check penalty)", relief=RIDGE, width=40, bg="#00ffff")
l1.grid(row=18,column=1, columnspan=4)
l1=Label(window, text="Appraise")
l1.grid(row=19,column=1)
l1=Label(window, text="Balance")
l1.grid(row=20,column=1)
l1=Label(window, text="Bluff")
l1.grid(row=21,column=1)
l1=Label(window, text="Climb")
l1.grid(row=22,column=1)
l1=Label(window, text="Concentration")
l1.grid(row=23,column=1)
l1=Label(window, text="Craft")
l1.grid(row=24,column=1)
l1=Label(window, text="Decipher Script")
l1.grid(row=25,column=1)
l1=Label(window, text="Diplomacy")
l1.grid(row=26,column=1)
l1=Label(window, text="Disable Device")
l1.grid(row=27,column=1)
l1=Label(window, text="Disguise")
l1.grid(row=28,column=1)
l1=Label(window, text="Escape Artist")
l1.grid(row=29,column=1)
l1=Label(window, text="Forgery")
l1.grid(row=30,column=1)
l1=Label(window, text="Gather Info")
l1.grid(row=31,column=1)
l1=Label(window, text="Handle Animal")
l1.grid(row=32,column=1)
l1=Label(window, text="Heal")
l1.grid(row=33,column=1)
l1=Label(window, text="Hide")
l1.grid(row=34,column=1)
l1=Label(window, text="Intimidate")
l1.grid(row=35,column=1)
l1=Label(window, text="Jump")
l1.grid(row=36,column=1)
l1=Label(window, text="Knowledge")
l1.grid(row=19,column=3)
l1=Label(window, text="Listen")
l1.grid(row=20,column=3)
l1=Label(window, text="Move Silently")
l1.grid(row=21,column=3)
l1=Label(window, text="Open Lock")
l1.grid(row=22,column=3)
l1=Label(window, text="Perform")
l1.grid(row=23,column=3)
l1=Label(window, text="Profession")
l1.grid(row=24,column=3)
l1=Label(window, text="Ride")
l1.grid(row=25,column=3)
l1=Label(window, text="Search")
l1.grid(row=26,column=3)
l1=Label(window, text="Sense Motive")
l1.grid(row=27,column=3)
l1=Label(window, text="Sleight Of Hand")
l1.grid(row=28,column=3)
l1=Label(window, text="Spellcraft")
l1.grid(row=29,column=3)
l1=Label(window, text="Spot")
l1.grid(row=30,column=3)
l1=Label(window, text="Survival")
l1.grid(row=31,column=3)
l1=Label(window, text="Swim")
l1.grid(row=32,column=3)
l1=Label(window, text="Tumble")
l1.grid(row=33,column=3)
l1=Label(window, text="UMD")
l1.grid(row=34,column=3)
l1=Label(window, text="Use Rope")
l1.grid(row=35,column=3)
l71=Label(window, text="Combat Skill", relief=RIDGE, width=24, bg="#00ffff")
l71.grid(row=14,column=5, columnspan=2)
l72=Label(window, text="Max HP")
l72.grid(row=15,column=5)
l74=Label(window, text="Initiative")
l74.grid(row=16,column=5)
l77=Label(window, text="Armor Class")
l77.grid(row=17,column=5)
l81=Label(window, text="BAB")
l81.grid(row=18,column=5)
l82=Label(window, text="APR (DEX)")
l82.grid(row=19,column=5)
l83=Label(window, text="APR (STR)")
l83.grid(row=20,column=5)
l71=Label(window, text="Note", relief=RIDGE, width=24, bg="#00ffff")
l71.grid(row=24,column=5, columnspan=2)
#Entry
ve1=StringVar()
e1=Entry(window,textvariable=ve1, width=12, justify="center")
e1.grid(row=5,column=2)
ve2=StringVar()
e2=Entry(window,textvariable=ve2, width=12, justify="center")
e2.grid(row=6,column=2)
ve3=StringVar()
e3=Entry(window,textvariable=ve3, width=12, justify="center")
e3.grid(row=7,column=2)
#Text
t1 = Text(window, width=36, height=12)
t1.grid(row=25,column=5, columnspan=2, rowspan=12)

#Defined Button
#Sex
vSex=StringVar()
l42=Label(window, textvariable=vSex, text=" ", width=12, relief=GROOVE)
l42.grid(row=12,column=6,sticky=W)
#Race
vRace=StringVar()
l9=Label(window, textvariable=vRace, text=" ", width=12, relief=GROOVE)
l9.grid(row=5,column=4)
#Level
vLvl=StringVar()
l19=Label(window, textvariable=vLvl, text=" ", width=12, relief=GROOVE)
l19.grid(row=5,column=6,sticky=W)
#Class
vClass=StringVar()
l20=Label(window, textvariable=vClass, text=" ", width=12, relief=GROOVE)
l20.grid(row=6,column=4)
#Gold
vGold=StringVar()
l4=Label(window, textvariable=vGold, text=" ", width=12, relief=GROOVE)
l4.grid(row=10,column=4)
#Alignment
vAlign=StringVar()
l42=Label(window, textvariable=vAlign, text=" ", width=12, relief=GROOVE)
l42.grid(row=13,column=6,sticky=W)
#Stats
vStr=StringVar()
l13=Label(window, textvariable=vStr, text=" ", width=12, relief=GROOVE)
l13.grid(row=12,column=4)

vDex=StringVar()
l14=Label(window, textvariable=vDex, text=" ", width=12, relief=GROOVE)
l14.grid(row=13,column=4)

vCon=StringVar()
l15=Label(window, textvariable=vCon, text=" ", width=12, relief=GROOVE)
l15.grid(row=14,column=4)

vInt=StringVar()
l16=Label(window, textvariable=vInt, text=" ", width=12, relief=GROOVE)
l16.grid(row=15,column=4)

vWis=StringVar()
l17=Label(window, textvariable=vWis, text=" ", width=12, relief=GROOVE)
l17.grid(row=16,column=4)

vCha=StringVar()
l18=Label(window, textvariable=vCha, text=" ", width=12, relief=GROOVE)
l18.grid(row=17,column=4)

#Save
vWill=StringVar()
l6=Label(window, textvariable=vWill, text=" ", width=12, relief=GROOVE)
l6.grid(row=15,column=2)
vFort=StringVar()
l7=Label(window, textvariable=vFort, text=" ", width=12, relief=GROOVE)
l7.grid(row=13,column=2)
vRef=StringVar()
l8=Label(window, textvariable=vRef, text=" ", width=12, relief=GROOVE)
l8.grid(row=14,column=2)

#Height & Weight
vHeight=StringVar()
l13=Label(window, textvariable=vHeight, text=" ", width=12, relief=GROOVE)
l13.grid(row=6,column=6,sticky=W)
vWeight=StringVar()
l23=Label(window, textvariable=vWeight, text=" ", width=12, relief=GROOVE)
l23.grid(row=7,column=6,sticky=W)

#SkillVar
vSk19=StringVar()
l27=Label(window, textvariable=vSk19, text=" ", width=12, relief=GROOVE)
l27.grid(row=19,column=2)
vSk20=StringVar()
l28=Label(window, textvariable=vSk20, text=" ", width=12, relief=GROOVE)
l28.grid(row=20,column=2)
vSk21=StringVar()
l29=Label(window, textvariable=vSk21, text=" ", width=12, relief=GROOVE)
l29.grid(row=21,column=2)
vSk22=StringVar()
l30=Label(window, textvariable=vSk22, text=" ", width=12, relief=GROOVE)
l30.grid(row=22,column=2)
vSk23=StringVar()
l31=Label(window, textvariable=vSk23, text=" ", width=12, relief=GROOVE)
l31.grid(row=23,column=2)
vSk24=StringVar()
l32=Label(window, textvariable=vSk24, text=" ", width=12, relief=GROOVE)
l32.grid(row=24,column=2)
vSk25=StringVar()
l33=Label(window, textvariable=vSk25, text=" ", width=12, relief=GROOVE)
l33.grid(row=25,column=2)
vSk26=StringVar()
l34=Label(window, textvariable=vSk26, text=" ", width=12, relief=GROOVE)
l34.grid(row=26,column=2)
vSk27=StringVar()
l42=Label(window, textvariable=vSk27, text=" ", width=12, relief=GROOVE)
l42.grid(row=27,column=2)
vSk28=StringVar()
l43=Label(window, textvariable=vSk28, text=" ", width=12, relief=GROOVE)
l43.grid(row=28,column=2)
vSk29=StringVar()
l44=Label(window, textvariable=vSk29, text=" ", width=12, relief=GROOVE)
l44.grid(row=29,column=2)
vSk30=StringVar()
l45=Label(window, textvariable=vSk30, text=" ", width=12, relief=GROOVE)
l45.grid(row=30,column=2)
vSk31=StringVar()
l46=Label(window, textvariable=vSk31, text=" ", width=12, relief=GROOVE)
l46.grid(row=31,column=2)
vSk32=StringVar()
l47=Label(window, textvariable=vSk32, text=" ", width=12, relief=GROOVE)
l47.grid(row=32,column=2)
vSk33=StringVar()
l48=Label(window, textvariable=vSk33, text=" ", width=12, relief=GROOVE)
l48.grid(row=33,column=2)
vSk34=StringVar()
l49=Label(window, textvariable=vSk34, text=" ", width=12, relief=GROOVE)
l49.grid(row=34,column=2)
vSk35=StringVar()
l50=Label(window, textvariable=vSk35, text=" ", width=12, relief=GROOVE)
l50.grid(row=35,column=2)
vSk36=StringVar()
l51=Label(window, textvariable=vSk36, text=" ", width=12, relief=GROOVE)
l51.grid(row=36,column=2)
#--------------
vSkA19=StringVar()
l35=Label(window, textvariable=vSkA19, text=" ", width=12, relief=GROOVE)
l35.grid(row=19,column=4)
vSkA20=StringVar()
l36=Label(window, textvariable=vSkA20, text=" ", width=12, relief=GROOVE)
l36.grid(row=20,column=4)
vSkA21=StringVar()
l37=Label(window, textvariable=vSkA21, text=" ", width=12, relief=GROOVE)
l37.grid(row=21,column=4)
vSkA22=StringVar()
l38=Label(window, textvariable=vSkA22, text=" ", width=12, relief=GROOVE)
l38.grid(row=22,column=4)
vSkA23=StringVar()
l39=Label(window, textvariable=vSkA23, text=" ", width=12, relief=GROOVE)
l39.grid(row=23,column=4)
vSkA24=StringVar()
l40=Label(window, textvariable=vSkA24, text=" ", width=12, relief=GROOVE)
l40.grid(row=24,column=4)
vSkA25=StringVar()
l41=Label(window, textvariable=vSkA25, text=" ", width=12, relief=GROOVE)
l41.grid(row=25,column=4)
vSkA26=StringVar()
l52=Label(window, textvariable=vSkA26, text=" ", width=12, relief=GROOVE)
l52.grid(row=26,column=4)
vSkA27=StringVar()
l53=Label(window, textvariable=vSkA27, text=" ", width=12, relief=GROOVE)
l53.grid(row=27,column=4)
vSkA28=StringVar()
l54=Label(window, textvariable=vSkA28, text=" ", width=12, relief=GROOVE)
l54.grid(row=28,column=4)
vSkA29=StringVar()
l55=Label(window, textvariable=vSkA29, text=" ", width=12, relief=GROOVE)
l55.grid(row=29,column=4)
vSkA30=StringVar()
l56=Label(window, textvariable=vSkA30, text=" ", width=12, relief=GROOVE)
l56.grid(row=30,column=4)
vSkA31=StringVar()
l57=Label(window, textvariable=vSkA31, text=" ", width=12, relief=GROOVE)
l57.grid(row=31,column=4)
vSkA32=StringVar()
l58=Label(window, textvariable=vSkA32, text=" ", width=12, relief=GROOVE)
l58.grid(row=32,column=4)
vSkA33=StringVar()
l59=Label(window, textvariable=vSkA33, text=" ", width=12, relief=GROOVE)
l59.grid(row=33,column=4)
vSkA34=StringVar()
l60=Label(window, textvariable=vSkA34, text=" ", width=12, relief=GROOVE)
l60.grid(row=34,column=4)
vSkA35=StringVar()
l61=Label(window, textvariable=vSkA35, text=" ", width=12, relief=GROOVE)
l61.grid(row=35,column=4)

#Age
vAge=StringVar()
l24=Label(window, textvariable=vAge, text=" ", width=12, relief=GROOVE)
l24.grid(row=8,column=6,sticky=W)

#Traits
vTraits=StringVar()
l3=Label(window, textvariable=vTraits, text=" ", width=12, relief=GROOVE)
l3.grid(row=7,column=4)

#Jobs
vJob1=StringVar()
l25=Label(window, textvariable=vJob1, text=" ", width=24, relief=GROOVE)
l25.grid(row=9,column=6, columnspan=2)
vJob2=StringVar()
l26=Label(window, textvariable=vJob2, text=" ", width=24, relief=GROOVE)
l26.grid(row=10,column=6, columnspan=2)
vJob3=StringVar()
l70=Label(window, textvariable=vJob3, text=" ", width=24, relief=GROOVE)
l70.grid(row=11,column=6, columnspan=2)

#hp
vHP=StringVar()
l73=Label(window, textvariable=vHP, text=" ", width=12, relief=GROOVE)
l73.grid(row=15,column=6,sticky=W)

#Ini
vIni=StringVar()
l75=Label(window, textvariable=vIni, text=" ", width=12, relief=GROOVE)
l75.grid(row=16,column=6,sticky=W)

#Armor
vArmor=StringVar()
l5=Label(window, textvariable=vArmor, text=" ", width=12, relief=GROOVE)
l5.grid(row=10,column=2)

#AC
vAC=StringVar()
l78=Label(window, textvariable=vAC, text=" ", width=12, relief=GROOVE)
l78.grid(row=17,column=6,sticky=W)

#FuckCommer
vCommoner=IntVar()
ckBox=Checkbutton(window,text="Disable Commoner", variable=vCommoner)
ckBox.grid(row=3,column=4, columnspan=2)

#BAB
vBAB=StringVar()
l80=Label(window, textvariable=vBAB, text=" ", width=12, relief=GROOVE)
l80.grid(row=18,column=6,sticky=W)

#APR
vAPRDex=StringVar()
l84=Label(window, textvariable=vAPRDex, text=" ", width=24, relief=GROOVE)
l84.grid(row=19,column=6, columnspan=2)
vAPRStr=StringVar()
l85=Label(window, textvariable=vAPRStr, text=" ", width=24, relief=GROOVE)
l85.grid(row=20,column=6, columnspan=2)

#Weapon
vWep1=StringVar()
l5=Label(window, textvariable=vWep1, text=" ", width=24, relief=GROOVE)
l5.grid(row=21,column=6, columnspan=2)
vWep2=StringVar()
l12=Label(window, textvariable=vWep2, text=" ", width=24, relief=GROOVE)
l12.grid(row=22,column=6, columnspan=2)

def ResetToNA(x):
    x.set("N/A")

def GetSaveValue(x):
    iLevel = vLvl.get()
    y = 0
    #print("Level is:" + str(iLevel))
    #GoodSave
    if x == 1:
        if iLevel == "1":
            y = 2
        elif iLevel == "2":
            y = 3
        elif iLevel == "3":
            y = 3
        elif iLevel == "4":
            y = 4
        elif iLevel == "5":
            y = 4
        elif iLevel == "6":
            y = 5
        elif iLevel == "7":
            y = 5
        elif iLevel == "8":
            y = 6
        elif iLevel == "9":
            y = 6
        elif iLevel == "10":
            y = 7
        elif iLevel == "11":
            y = 7
        elif iLevel == "12":
            y = 8
        elif iLevel == "13":
            y = 8
        elif iLevel == "14":
            y = 9
        elif iLevel == "15":
            y = 9
        elif iLevel == "16":
            y = 10
        elif iLevel == "17":
            y = 10
        elif iLevel == "18":
            y = 11
        elif iLevel == "19":
            y = 11
        else:
            y = 12
    else:
        if iLevel == "1":
            y = 0
        elif iLevel == "2":
            y = 0
        elif iLevel == "3":
            y = 1
        elif iLevel == "4":
            y = 1
        elif iLevel == "5":
            y = 1
        elif iLevel == "6":
            y = 2
        elif iLevel == "7":
            y = 2
        elif iLevel == "8":
            y = 2
        elif iLevel == "9":
            y = 3
        elif iLevel == "10":
            y = 3
        elif iLevel == "11":
            y = 3
        elif iLevel == "12":
            y = 4
        elif iLevel == "13":
            y = 4
        elif iLevel == "14":
            y = 4
        elif iLevel == "15":
            y = 5
        elif iLevel == "16":
            y = 5
        elif iLevel == "17":
            y = 5
        elif iLevel == "18":
            y = 6
        elif iLevel == "19":
            y = 6
        else:
            y = 6
    #print("Bonus From Level" + str(y))
    return y

def generate():
    #Variable
    iRnd = random.randrange(1, 100)
    #Class shit
    #Save, 1 = Good, 2 = Poor
    iFortClass = 0
    iRefClass = 0
    iWillClass = 0
    iGoldClass = 0
    #BAB, 1 = Good, 2 = Average, 3 = Wizard
    iBabClass = 0
    iHPClass = 0
    iSkillClass = 0
    #Check if the class has the skill, 0 = no, 1 = yes
    iSkAppraise = 0
    iSkAppraiseUnlock = 0
    iSkAppraiseBonus = 0
    iSkBalance = 0
    iSkBalanceUnlock = 0
    iSkBalanceBonus = 0
    iSkBluff = 0
    iSkBluffUnlock = 0
    iSkBluffBonus = 0
    iSkClimb = 0
    iSkClimbUnlock = 0
    iSkClimbBonus = 0
    iSkConc = 0
    iSkConcUnlock = 0
    iSkConcBonus = 0
    iSkCraft = 0
    iSkCraftfUnlock = 0
    iSkCraftBonus = 0
    iSkDecif = 0
    iSkDecifUnlock = 0
    iSkDecifBonus = 0
    iSkDiplo = 0
    iSkDiploUnlock = 0
    iSkDiploBonus = 0
    iSkDD = 0
    iSkDDUnlock = 0
    iSkDDBonus = 0
    iSkDisg = 0
    iSkDisgUnlock = 0
    iSkDisgBonus = 0
    iSkEscape = 0
    iSkEscapeUnlock = 0
    iSkEscapeBonus = 0
    iSkForgery = 0
    iSkForgeryUnlock = 0
    iSkForgeryBonus = 0
    iSkGather = 0
    iSkGatherUnlock = 0
    iSkGatherBonus = 0
    iSkHandle = 0
    iSkHandleUnlock = 0
    iSkHandleBonus = 0
    iSkHeal = 0
    iSkHealUnlock = 0
    iSkHealBonus = 0
    iSkHide = 0
    iSkHideUnlock = 0
    iSkHideBonus = 0
    iSkInti = 0
    iSkIntiUnlock = 0
    iSkIntiBonus = 0
    iSkJump = 0
    iSkJumpUnlock = 0
    iSkJumpBonus = 0
    iSkKnow = 0
    iSkKnowUnlock = 0
    iSkKnowBonus = 0
    iSkListen = 0
    iSkListenUnlock = 0
    iSkListenBonus = 0
    iSkMS = 0
    iSkMSUnlock = 0
    iSkMSBonus = 0
    iSkOpen = 0
    iSkOpenUnlock = 0
    iSkOpenBonus = 0
    iSkPerf = 0
    iSkPerfUnlock = 0
    iSkPerfBonus = 0
    iSkProf = 0
    iSkProfUnlock = 0
    iSkProfBonus = 0
    iSkRide = 0
    iSkRideUnlock = 0
    iSkRideBonus = 0
    iSkSearch = 0
    iSkSearchUnlock = 0
    iSkSearchBonus = 0
    iSkSM = 0
    iSkSMUnlock = 0
    iSkSMBonus = 0
    iSkSleight = 0
    iSkSleightUnlock = 0
    iSkSleightBonus = 0
    iSkSpellcraft = 0
    iSkSpellcraftUnlock = 0
    iSkSpellcraftBonus = 0
    iSkSpot = 0
    iSkSpotUnlock = 0
    iSkSpotBonus = 0
    iSkSurvival = 0
    iSkSurvivalUnlock = 0
    iSkSurvivalBonus = 0
    iSkSwim = 0
    iSkSwimUnlock = 0
    iSkSwimBonus = 0
    iSkTumble = 0
    iSkTumbleUnlock = 0
    iSkTumbleBonus = 0
    iSkUMD = 0
    iSkUMDUnlock = 0
    iSkUMDBonus = 0
    iSkRope = 0
    iSkRopeUnlock = 0
    iSkRopeBonus = 0
    iACP = 0
    #-------------------
    iAlignClass = ""
    vAlignClassTest = ""
    #Bonus Stats
    iStrBonus =  0
    iDexBonus = 0
    iConBonus = 0
    iIntBonus = 0
    iWisBonus = 0
    iChaBonus = 0
    #Save
    iSaveBonus = 0
    iSaveBonus = 0
    iIni = 0
    iAttackBonus = 0
    sArmor = "Cloth"
    iArmorMaxDex = 0
    iAC = 0
    iArmorAC = 0
    iShieldAC = 0
    
    #SetShit
    #Weapon
    #Wep 2 = Commoner
    #Wep 1 = fighter
    #Wep 3 = Mage
    #Wep 4 = Monk
    iWep1 = ['Gauntlet', 'Unarmed strike', 'Dagger', 'Dagger,  punching', 'Gauntlet, spiked', 'Mace, light', 'Sickle', 'Club', 'Mace, heavy', 'Morningstar', 'Shortspear', 'Longspear', 'Quarterstaff', 'Spear', 'Javelin', 'Axe, throwing', 'Hammer, light', 'Handaxe', 'Kukri', 'Pick', 'Sword, short', 'Battleaxe', 'Flail', 'Longsword', 'Pick, heavy', 'Rapier', 'Scimitar', 'Trident', 'Warhammer', 'Falchion', 'Glaive', 'Greataxe', 'Greatclub', 'Flail,  heavy', 'Greatsword', 'Guisarme', 'Halberd', 'Lance', 'Ranseur', 'Scythe', 'Kama', 'Nunchaku', 'Sai', 'Siangham', 'Sword, bastard', 'Waraxe, dwarven', 'Whip', 'Axe, orc double', 'Chain, spiked', 'Flail, dire', 'Sword, two-bladed'] 
    iWep2 = ['Gauntlet', 'Unarmed strike', 'Dagger', 'Dagger,  punching', 'Gauntlet, spiked', 'Mace,  light', 'Sickle', 'Club', 'Mace,  heavy', 'Morningstar', 'Shortspear', 'Longspear', 'Quarterstaff', 'Spear', 'Javelin', 'Axe, throwing', 'Hammer, light', 'Handaxe', 'Pick', 'Sword, short', 'Glaive', 'Scythe'] 
    iWep3 = ['Dagger', 'Dagger,  punching', 'Quarterstaff'] 
    iWep4 = ['Gauntlet', 'Unarmed strike', 'Gauntlet, spiked', 'Sickle', 'Kama', 'Nunchaku', 'Sai'] 
    iShield1 = ['Buckler', 'Shield, light wooden', 'Shield, light steel'] 
    iShield2 = ['Shield, heavy wooden', 'Shield, heavy steel']
    
    #Sex
    if iRnd > 90:
        vSex.set("Female")
    else:
        vSex.set("Male")   
      
    #Race

    sSpecRace = c1.get();
    iRnd = 0
    if sSpecRace == "N/A":
        iRnd = random.randrange(1, 100)
    elif sSpecRace == "":
        iRnd = random.randrange(1, 100)
    elif sSpecRace == c5.get():
        iRnd = 4   
    elif sSpecRace == "Human":
        iRnd = 69     
    elif sSpecRace == "Dwarf":
        iRnd = 75      
    elif sSpecRace == "Elf":
        iRnd = 77      
    elif sSpecRace == "Gnome":
        iRnd = 81        
    elif sSpecRace == "Half-Elf":
        iRnd = 88       
    elif sSpecRace == "Half-Orc":
        iRnd = 93        
    elif sSpecRace == "Halfling":
        iRnd = 95 
        
    if iRnd < 50:
        vRace.set(c5.get())
    else:
        if iRnd < 70:
            vRace.set("Human")
        elif iRnd < 76:
            vRace.set("Dwarf")
        elif iRnd < 78:
            vRace.set("Elf")
        elif iRnd < 82:
            vRace.set("Gnome")
        elif iRnd < 89:
            vRace.set("Half-Elf")
        elif iRnd < 94:
            vRace.set("Half-Orc")
        else:
            vRace.set("Halfling")  
            
    sSpecLvl = c3.get();
    iRnd = 0
    if sSpecLvl  == "N/A":
        iRnd = random.randrange(1, 103)
    elif sSpecLvl  == "":
        iRnd = random.randrange(1, 103)
    elif sSpecLvl  == "1":
        iRnd = 9 
    elif sSpecLvl  == "2":
        iRnd = 29 
    elif sSpecLvl  == "3":
        iRnd = 69
    elif sSpecLvl  == "4":
        iRnd = 77
    elif sSpecLvl  == "5":
        iRnd = 85  
    elif sSpecLvl  == "6":
        iRnd = 88
    elif sSpecLvl  == "7":
        iRnd = 93
    elif sSpecLvl  == "8":
        iRnd = 97   
    elif sSpecLvl  == "9":
        iRnd = 99    
    elif sSpecLvl  == "10":
        iRnd = 102     
    elif sSpecLvl  == "11":
        iRnd = 103      
    elif sSpecLvl  == "12":
        iRnd = 104     
    elif sSpecLvl  == "13":
        iRnd = 105    
    elif sSpecLvl  == "14":
        iRnd = 106    
    elif sSpecLvl  == "15":
        iRnd = 107    
    elif sSpecLvl  == "16":
        iRnd = 108    
    elif sSpecLvl  == "17":
        iRnd = 109    
    elif sSpecLvl  == "18":
        iRnd = 110    
    elif sSpecLvl  == "19":
        iRnd = 111    
    elif sSpecLvl  == "20":
        iRnd = 112
        
    #Level, should be between 1 and 9
    if iRnd < 10:
        vLvl.set("1")
    elif iRnd < 30:
        vLvl.set("2")
    elif iRnd < 70:
        vLvl.set("3")
    elif iRnd < 78:
        vLvl.set("4")
    elif iRnd < 86:
        vLvl.set("5")
    elif iRnd < 89:
        vLvl.set("6")
    elif iRnd < 94:
        vLvl.set("7")
    elif iRnd < 98:
        vLvl.set("8")
    elif iRnd < 101:
        vLvl.set("9") 
    elif iRnd == 102:
        vLvl.set("10") 
    elif iRnd == 103:
        vLvl.set("11") 
    elif iRnd == 104:
        vLvl.set("12") 
    elif iRnd == 105:
        vLvl.set("13") 
    elif iRnd == 106:
        vLvl.set("14") 
    elif iRnd == 107:
        vLvl.set("15") 
    elif iRnd == 108:
        vLvl.set("16") 
    elif iRnd == 109:
        vLvl.set("17") 
    elif iRnd == 110:
        vLvl.set("18") 
    elif iRnd == 111:
        vLvl.set("19") 
    elif iRnd == 112:
        vLvl.set("20") 
      
    sSpecClass = c2.get();
    iRnd = 0
    if sSpecClass == "N/A":
        if vCommoner.get() == 0:
            iRnd = random.randrange(1, 103)
        else:
            iRnd = random.randrange(65, 103)
    elif sSpecClass == "":
        if vCommoner.get() == 0:
            iRnd = random.randrange(1, 103)
        else:
            iRnd = random.randrange(65, 103)
    elif sSpecClass == "Aristocrat":
        iRnd = 4 
    elif sSpecClass == "Commoner":
        iRnd = 59      
    elif sSpecClass == "Warrior":
        iRnd = 66      
    elif sSpecClass == "Expert":
        iRnd = 64     
    elif sSpecClass == "Barbarian":
        iRnd = 72          
    elif sSpecClass == "Bard":
        iRnd = 75       
    elif sSpecClass == "Cleric":
        iRnd = 78        
    elif sSpecClass == "Druid":
        iRnd = 81        
    elif sSpecClass == "Fighter":
        iRnd = 84       
    elif sSpecClass == "Monk":
        iRnd = 87       
    elif sSpecClass == "Paladin":
        iRnd = 90      
    elif sSpecClass == "Ranger":
        iRnd = 93      
    elif sSpecClass == "Rogue":
        iRnd = 96      
    elif sSpecClass == "Sorcerer":
        iRnd = 99      
    elif sSpecClass == "Wizard":
        iRnd = 101
    #Class, using basic class + trash npc class, we will choose job according the the class
    #Lets do the armor also
    if iRnd < 5:
        vClass.set("Aristocrat")
        iGoldClass = 10 * (random.randrange(6, 48))
        iFortClass = 2
        iRefClass = 2
        iWillClass = 1
        iBabClass = 2
        iHPClass = 8
        iSkAppraiseUnlock = 1
        iSkBluffUnlock = 1
        iSkDiploUnlock = 1
        iSkDisgUnlock = 1
        iSkForgeryUnlock = 1
        iSkGatherUnlock = 1
        iSkHandleUnlock = 1
        iSkIntiUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkPerfUnlock = 1
        iSkRideUnlock = 1
        iSkSMUnlock = 1
        iSkSpotUnlock = 1
        iSkSurvivalUnlock = 1
        iSkSwimUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']   
        iStrBonus = 0
        iDexBonus = 0
        iConBonus = 0
        iIntBonus = 4
        iWisBonus = 4
        iChaBonus = 5
        iRnd = random.randrange(1, 100)
        if iRnd < 60:
            sArmor = "Cloth"
            iArmorMaxDex = 99
        elif iRnd < 90:
            sArmor = "Padded"
            iArmorMaxDex = 8
            iArmorAC = 1
        else:
            sArmor = "Leather"
            iArmorMaxDex = 6
            iArmorAC = 2
              
        vWep1.set(secrets.choice(iWep2))
        iRnd = random.randrange(1, 100)  
        if iRnd > 90:
            vWep2.set(secrets.choice(iWep2))
        else:
            vWep2.set("")
    elif iRnd < 60:
        vClass.set("Commoner")
        iGoldClass = 1 * (random.randrange(5, 20))
        iFortClass = 2
        iRefClass = 2
        iWillClass = 2
        iBabClass = 3
        iHPClass = 4
        iSkillClass = 2
        iSkClimbUnlock = 1
        iSkCraftfUnlock = 1
        iSkHandleUnlock = 1
        iSkJumpUnlock = 1
        iSkListenUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSpotUnlock = 1
        iSkSwimUnlock = 1
        iSkRopeUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']  
        iStrBonus = 0
        iDexBonus = 0
        iConBonus = 1
        iIntBonus = 0
        iWisBonus = 0
        iChaBonus =  0 
        sArmor = "Cloth"
        iArmorMaxDex = 99
        vWep1.set(secrets.choice(iWep2))
        iRnd = random.randrange(1, 100)  
        if iRnd > 90:
            vWep2.set(secrets.choice(iShield1))
            iShieldAC = 1
        else:
            vWep2.set(secrets.choice(iWep2))
    elif iRnd < 65:
        vClass.set("Expert")
        iGoldClass = 10 * (random.randrange(3, 12))
        iFortClass = 2
        iRefClass = 2
        iWillClass = 1
        iBabClass = 2
        iHPClass = 6
        iSkillClass = 6
        iSkAppraiseUnlock =1 
        iSkBalanceUnlock = 1
        iSkBluffUnlock = 1
        iSkClimbUnlock = 1
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDiploUnlock = 1
        iSkDisgUnlock = 1
        iSkEscapeUnlock = 1
        iSkForgeryUnlock = 1
        iSkGatherUnlock = 1
        iSkHandleUnlock = 1
        iSkHealUnlock = 1
        iSkHideUnlock = 1
        iSkIntiUnlock = 1
        iSkJumpUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkMSUnlock = 1
        iSkOpenUnlock = 1
        iSkPerfUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSearchUnlock = 1
        iSkSMUnlock = 1
        iSkSleightUnlock = 1
        iSkSpellcraftUnlock = 1
        iSkSpotUnlock = 1
        iSkSurvivalUnlock = 1
        iSkSwimUnlock = 1
        iSkTumbleUnlock = 1
        iSkUMDUnlock = 1
        iSkRopeUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 0
        iDexBonus = 3
        iConBonus = 0
        iIntBonus = 5
        iWisBonus = 0
        iChaBonus = 2
        sArmor = "Cloth"
        iArmorMaxDex = 99
        vWep1.set(secrets.choice(iWep2))
        vWep2.set(secrets.choice(iWep2))
    elif iRnd < 68:
        vClass.set("Warrior")
        iGoldClass = 10 * (random.randrange(3, 12))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 2
        iBabClass = 1
        iHPClass = 8
        iSkillClass = 2
        iSkClimbUnlock = 1
        iSkHandleUnlock = 1
        iSkIntiUnlock = 1
        iSkJumpUnlock = 1
        iSkRideUnlock = 1
        iSkSwimUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 5
        iDexBonus = 2
        iConBonus = 4
        iIntBonus = 1
        iWisBonus = 0
        iChaBonus = 0
        iRnd = random.randrange(1, 100)
        if iRnd < 40:
            sArmor = "Studded leather"
            iArmorMaxDex = 5
            iArmorAC = 3
            iACP = 1
        elif iRnd < 60:
            sArmor = "Chain shirt"
            iArmorMaxDex = 4
            iArmorAC = 4
            iACP = 2
        elif iRnd < 80:
            sArmor = "Hide"
            iArmorMaxDex = 4
            iArmorAC = 3
            iACP = 3
        else:
            sArmor = "Scale mail"
            iArmorMaxDex = 3
            iArmorAC = 4
            iACP = 4
        vWep1.set(secrets.choice(iWep1))        
        iRnd = random.randrange(1, 100)  
        if iRnd > 60:
            vWep2.set(secrets.choice(iShield1))
            iShieldAC = 1
        elif iRnd > 70:
            vWep2.set(secrets.choice(iShield2))
            iShieldAC = 2
        else:
            vWep2.set(secrets.choice(iWep1))
    elif iRnd < 73:
        vClass.set("Barbarian")
        iGoldClass = 10 * (random.randrange(4, 16))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 2
        iBabClass = 1
        iHPClass = 12
        iSkillClass = 4
        iSkClimbUnlock = 1
        iSkHandleUnlock = 1
        iSkIntiUnlock = 1
        iSkJumpUnlock = 1
        iSkListenUnlock = 1
        iSkRideUnlock = 1
        iSkSurvivalUnlock = 1
        iSkSwimUnlock = 1
        iAlignClass = ['Neutre Good', 'Chaotic Good', 'Neutre Neutre', 'Chaotic Neutral', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 5
        iDexBonus = 2
        iConBonus = 6
        iIntBonus = 0
        iWisBonus = 0
        iChaBonus =  0 
        iRnd = random.randrange(1, 100)
        if iRnd < 30:
            sArmor = "Chain shirt"
            iArmorMaxDex = 4
            iArmorAC = 4
            iACP = 2
            iACP
        elif iRnd < 45:
            sArmor = "Hide"
            iArmorMaxDex = 4
            iArmorAC = 3
            iACP = 4
        elif iRnd < 60:
            sArmor = "Scale mail"
            iArmorMaxDex = 3
            iArmorAC = 4
            iACP = 4
        elif iRnd < 75:
            sArmor = "Chainmail"
            iArmorAC = 5
            iArmorMaxDex = 2
            iACP = 2
        else:
            sArmor = "Breastplate"
            iArmorAC = 5
            iArmorMaxDex = 3   
            iACP = 4         
        vWep1.set(secrets.choice(iWep1))
        vWep2.set(secrets.choice(iWep1))
    elif iRnd < 76:
        vClass.set("Bard")
        iGoldClass = 10 * (random.randrange(4, 16))
        iFortClass = 2
        iRefClass = 1
        iWillClass = 1
        iBabClass = 2
        iHPClass = 6
        iSkillClass = 6
        iAlignClass = ['Neutre Good', 'Chaotic Good', 'Neutre Neutre', 'Chaotic Neutral', 'Neutre Evil', 'Chaotic Evil']  
        iStrBonus = 0
        iDexBonus = 3
        iConBonus = 0
        iIntBonus = 2
        iWisBonus = 0
        iChaBonus = 6
        iSkAppraiseUnlock = 1
        iSkBalanceUnlock = 1
        iSkBluffUnlock = 1
        iSkClimbUnlock = 1
        iSkCraftfUnlock = 1
        iSkDecifUnlock = 1
        iSkDiploUnlock = 1
        iSkDisgUnlock = 1
        iSkEscapeUnlock = 1
        iSkGatherUnlock = 1
        iSkHideUnlock = 1
        iSkJumpUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkMSUnlock = 1
        iSkPerfUnlock = 1
        iSkProfUnlock = 1
        iSkSMUnlock = 1
        iSkSleightUnlock = 1
        iSkSpellcraftUnlock = 1
        iSkSwimUnlock = 1
        iSkTumbleUnlock = 1
        iSkUMDUnlock = 1
        iRnd = random.randrange(1, 100)
        if iRnd < 50:
            sArmor = "Cloth"
            iArmorMaxDex = 99
        else:
            sArmor = "Padded"
            iArmorAC = 1
            iArmorMaxDex = 8
        vWep1.set(secrets.choice(iWep1))
        vWep2.set(secrets.choice(iWep1))
    elif iRnd < 79:
        vClass.set("Cleric")
        iGoldClass = 1 * (random.randrange(1, 2))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 1
        iBabClass = 2
        iHPClass = 8
        iSkillClass = 2
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 2
        iDexBonus = 0
        iConBonus = 0
        iIntBonus = 0
        iWisBonus = 5
        iChaBonus = 4
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDiploUnlock = 1
        iSkHealUnlock = 1
        iSkKnowUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSpellcraftUnlock = 1
        iRnd = random.randrange(1, 100)
        if iRnd < 30:
            sArmor = "Chain shirt"
            iArmorAC = 4
            iArmorMaxDex = 4
            iACP = 2
        elif iRnd < 50:
            sArmor = "Scale mail"
            iArmorAC = 4
            iArmorMaxDex = 3
            iACP = 4
        elif iRnd < 60:
            sArmor = "Chainmail"
            iArmorAC = 5
            iArmorMaxDex = 2
            iACP = 5
        elif iRnd < 75:
            sArmor = "Breastplate"
            iArmorAC = 5
            iArmorMaxDex = 3 
            iACP = 4  
        elif iRnd < 80:
            sArmor = "Splint mail"
            iArmorAC = 6
            iArmorMaxDex = 0   
            iACP = 7  
        else:
            sArmor = "Banded mail"
            iArmorAC = 6
            iArmorMaxDex = 1 
            iACP = 6 
        vWep1.set(secrets.choice(iWep1))
        if iRnd > 70:
            vWep2.set(secrets.choice(iShield1))
            iShieldAC = 1
        elif iRnd > 80:
            vWep2.set(secrets.choice(iShield2))
            iShieldAC = 2
        else:
            vWep2.set(secrets.choice(iWep1))
    elif iRnd < 82:
        vClass.set("Druid")
        iGoldClass = 1 * (random.randrange(1, 2))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 1
        iBabClass = 2
        iHPClass = 8
        iSkillClass = 4
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDiploUnlock = 1
        iSkHandleUnlock = 1
        iSkHealUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSpellcraftUnlock = 1
        iSkSpotUnlock = 1
        iSkSurvivalUnlock = 1
        iSkSwimUnlock = 1
        iAlignClass = ['Neutre Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Neutre Evil', 'Chaotic Evil'] 
        iStrBonus = 0
        iDexBonus = 2
        iConBonus = 2
        iIntBonus = 0
        iWisBonus = 6
        iChaBonus = 0
        iRnd = random.randrange(1, 100)
        if iRnd < 30:
            sArmor = "Padded"
            iArmorAC = 1
            iArmorMaxDex = 8
        elif iRnd < 50:
            sArmor = "Leather"
            iArmorAC = 2
            iArmorMaxDex = 6
        elif iRnd < 60:
            sArmor = "Studded leather"
            iArmorAC = 2
            iArmorMaxDex = 5
            iACP = 1
        elif iRnd < 75:
            sArmor = "Hide"
            iArmorAC = 3
            iArmorMaxDex = 4    
            iACP = 3 
        else:
            sArmor = "Scale mail"
            iArmorAC = 4
            iArmorMaxDex = 3 
            iACP = 4
        vWep1.set(secrets.choice(iWep3))
        vWep2.set(secrets.choice(iWep3))
    elif iRnd < 85:
        vClass.set("Fighter")
        iGoldClass = 10 * (random.randrange(5, 20))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 2
        iBabClass = 1
        iHPClass = 10
        iSkillClass = 2
        iSkClimbUnlock = 1
        iSkCraftfUnlock = 1
        iSkHandleUnlock = 1
        iSkIntiUnlock = 1
        iSkJumpUnlock = 1
        iSkRideUnlock = 1
        iSkSwimUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']   
        iStrBonus = 4
        iDexBonus = 2
        iConBonus = 4
        iIntBonus = 2
        iWisBonus = 0
        iChaBonus = 0    
        iRnd = random.randrange(1, 100)
        if iRnd < 30:
            sArmor = "Scale mail"
            iArmorAC = 4
            iArmorMaxDex = 3
            iACP = 4
        elif iRnd < 50:
            sArmor = "Chainmail"
            iArmorAC = 5
            iArmorMaxDex = 2
            iACP = 5
        elif iRnd < 70:
            sArmor = "Breastplate"
            iArmorAC = 5
            iArmorMaxDex = 3  
            iACP = 4 
        elif iRnd < 80:
            sArmor = "Splint mail"
            iArmorAC = 6
            iArmorMaxDex = 0  
            iACP = 7   
        elif iRnd < 95:
            sArmor = "Banded mail"
            iArmorAC = 6
            iArmorMaxDex = 1  
            iACP = 6    
        else:
            sArmor = "Half-plate"
            iArmorAC = 7
            iArmorMaxDex = 0 
            iACP = 7
        vWep1.set(secrets.choice(iWep1))
        if iRnd > 60:
            vWep2.set(secrets.choice(iShield1))
            iShieldAC = 1
        elif iRnd > 70:
            vWep2.set(secrets.choice(iShield2))
            iShieldAC = 2
        else:
            vWep2.set(secrets.choice(iWep1))
    elif iRnd < 88:
        vClass.set("Monk")
        iGoldClass = 10 * (random.randrange(5, 20))
        iFortClass = 1
        iRefClass = 1
        iWillClass = 1
        iBabClass = 2
        iHPClass = 8
        iSkillClass = 4
        iSkBalanceUnlock = 1
        iSkClimbUnlock = 1
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDiploUnlock = 1
        iSkEscapeUnlock = 1
        iSkHideUnlock = 1
        iSkJumpUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkMSUnlock = 1
        iSkPerfUnlock = 1
        iSkProfUnlock = 1
        iSkSMUnlock = 1
        iSkSpotUnlock = 1
        iSkSwimUnlock = 1
        iSkTumbleUnlock = 1
        iAlignClass = ['Lawful Good', 'Lawful Neutral', 'Lawful Evil']  
        iStrBonus = 3
        iDexBonus = 3
        iConBonus = 3
        iIntBonus = 3
        iWisBonus = 3
        iChaBonus = 3
        sArmor = "Cloth"
        iArmorMaxDex = 99
        vWep1.set(secrets.choice(iWep4))
        vWep2.set(secrets.choice(iWep4))
    elif iRnd < 91:
        vClass.set("Paladin")
        iGoldClass = 10 * (random.randrange(5, 20))
        iFortClass = 1
        iRefClass = 2
        iWillClass = 2
        iBabClass = 2
        iHPClass = 10
        iSkillClass = 2
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDiploUnlock = 1
        iSkHandleUnlock = 1
        iSkHealUnlock = 1
        iSkKnowUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSMUnlock = 1
        iAlignClass = ['Lawful Good']   
        iStrBonus = 4
        iDexBonus = 0
        iConBonus = 3
        iIntBonus = 0
        iWisBonus = 3
        iChaBonus = 3    
        iRnd = random.randrange(1, 100)
        if iRnd < 30:
            sArmor = "Scale mail"
            iArmorAC = 4
            iArmorMaxDex = 3
            iACP = 4
        elif iRnd < 50:
            sArmor = "Chainmail"
            iArmorAC = 5
            iArmorMaxDex = 2
            iACP = 5
        elif iRnd < 70:
            sArmor = "Breastplate"
            iArmorAC = 5
            iArmorMaxDex = 3   
            iACP = 4
        elif iRnd < 80:
            sArmor = "Splint mail"
            iArmorAC = 6
            iArmorMaxDex = 0    
            iACP = 7 
        elif iRnd < 95:
            sArmor = "Banded mail"
            iArmorAC = 6
            iArmorMaxDex = 1 
            iACP = 6     
        else:
            sArmor = "Half-plate"
            iArmorAC = 7
            iArmorMaxDex = 0 
            iACP = 7
        vWep1.set(secrets.choice(iWep1))
        if iRnd > 60:
            vWep2.set(secrets.choice(iShield1))
            iShieldAC = 1
        elif iRnd > 70:
            vWep2.set(secrets.choice(iShield2))
            iShieldAC = 2
        else:
            vWep2.set(secrets.choice(iWep1))
    elif iRnd < 94:
        vClass.set("Ranger")
        iGoldClass = 10 * (random.randrange(5, 20))
        iFortClass = 1
        iRefClass = 1
        iWillClass = 2
        iBabClass = 1
        iHPClass = 8
        iSkillClass = 6
        iSkClimbUnlock = 1
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkHandleUnlock = 1
        iSkHealUnlock = 1
        iSkHideUnlock = 1
        iSkJumpUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkMSUnlock = 1
        iSkProfUnlock = 1
        iSkRideUnlock = 1
        iSkSearchUnlock = 1
        iSkSpotUnlock = 1
        iSkSurvivalUnlock = 1
        iSkSwimUnlock = 1
        iSkRopeUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 2
        iDexBonus = 2
        iConBonus = 2
        iIntBonus = 2
        iWisBonus = 4
        iChaBonus = 0
        iRnd = random.randrange(1, 100)
        if iRnd < 60:
            sArmor = "Cloth"
            iArmorMaxDex = 99
        elif iRnd < 90:
            sArmor = "Padded"
            iArmorMaxDex = 8
            iArmorAC = 1
        else:
            sArmor = "Leather"
            iArmorMaxDex = 6
            iArmorAC = 2
        vWep1.set(secrets.choice(iWep1))
        vWep2.set(secrets.choice(iWep1))
    elif iRnd < 97:
        vClass.set("Rogue")
        iGoldClass = 10 * (random.randrange(5, 80))
        iFortClass = 2
        iRefClass = 1
        iWillClass = 2
        iBabClass = 2
        iHPClass = 6
        iSkillClass = 8
        iSkAppraiseUnlock = 1
        iSkBalanceUnlock = 1
        iSkBluffUnlock = 1
        iSkClimbUnlock = 1
        iSkCraftfUnlock = 1
        iSkDecifUnlock = 1
        iSkDiploUnlock = 1
        iSkDDUnlock = 1
        iSkDisgUnlock = 1
        iSkEscapeUnlock = 1
        iSkForgeryUnlock = 1
        iSkGatherUnlock = 1
        iSkHideUnlock = 1
        iSkIntiUnlock = 1
        iSkJumpUnlock = 1
        iSkKnowUnlock = 1
        iSkListenUnlock = 1
        iSkMSUnlock = 1
        iSkOpenUnlock = 1
        iSkPerfUnlock = 1
        iSkProfUnlock = 1
        iSkSearchUnlock = 1
        iSkSMUnlock = 1
        iSkSleightUnlock = 1
        iSkSpotUnlock = 1
        iSkSwimUnlock = 1
        iSkTumbleUnlock = 1
        iSkUMDUnlock = 1
        iSkRopeUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']    
        iStrBonus = 0
        iDexBonus = 6
        iConBonus = 0
        iIntBonus = 4
        iWisBonus = 0
        iChaBonus = 2
        iRnd = random.randrange(1, 100)
        if iRnd < 60:
            sArmor = "Cloth"
            iArmorMaxDex = 99
        elif iRnd < 90:
            sArmor = "Padded"
            iArmorMaxDex = 8
            iArmorAC = 1
        else:
            sArmor = "Leather"
            iArmorMaxDex = 6
            iArmorAC = 2
        vWep1.set(secrets.choice(iWep1))
        vWep2.set(secrets.choice(iWep1))
    elif iRnd < 100:
        vClass.set("Sorcerer")
        iGoldClass = 10 * (random.randrange(5, 80))
        iFortClass = 2
        iRefClass = 2
        iWillClass = 1
        iBabClass = 3
        iHPClass = 4
        iSkillClass = 2
        iSkBluffUnlock = 1
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkKnowUnlock = 1
        iSkProfUnlock = 1
        iSkSpellcraftUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']   
        iStrBonus = 0
        iDexBonus = 0
        iConBonus = 3
        iIntBonus = 2
        iWisBonus = 0
        iChaBonus = 6
        sArmor = "Cloth"
        iArmorMaxDex = 99
        vWep1.set(secrets.choice(iWep3))
        vWep2.set(secrets.choice(iWep3))
    else:
        vClass.set("Wizard")
        iGoldClass = 10 * (random.randrange(5, 80))
        iFortClass = 2
        iRefClass = 2
        iWillClass = 1
        iBabClass = 3
        iHPClass = 4
        iSkillClass = 2
        iSkConcUnlock = 1
        iSkCraftfUnlock = 1
        iSkDecifUnlock = 1
        iSkKnowUnlock = 1
        iSkProfUnlock = 1
        iSkSpellcraftUnlock = 1
        iAlignClass = ['Lawful Good', 'Neutre Good', 'Chaotic Good', 'Lawful Neutral', 'Neutre Neutre', 'Chaotic Neutral', 'Lawful Evil', 'Neutre Evil', 'Chaotic Evil']   
        iStrBonus = 0
        iDexBonus = 2
        iConBonus = 1
        iIntBonus = 6
        iWisBonus = 0
        iChaBonus = 2
        sArmor = "Cloth"
        iArmorMaxDex = 99
        vWep1.set(secrets.choice(iWep3))
        vWep2.set(secrets.choice(iWep3))
    
    #BAB
    iABTotal = 0
    if iBabClass == 1:
        iABTotal = math.floor(int(vLvl.get()) * 1)
    elif iBabClass == 2:
        iABTotal = math.floor(int(vLvl.get()) * 0.75)
    elif iBabClass == 3:
        iABTotal = math.floor(int(vLvl.get()) * 0.50)
    vBAB.set(iABTotal)
    
    #Armor setting
    #AC, *Set Armor, Max dex, *ACP
    vArmor.set(sArmor)
    
    iRnd = random.randrange(1, 100)
    #Gold
    iGoldClassBonus = 0;
    if vGold.get == 1:
        iGoldClassBonus = random.randrange(4, 9)
    elif vGold.get == 2:
        iGoldClassBonus = random.randrange(10, 20)
    elif vGold.get == 3:
        iGoldClassBonus = random.randrange(12, 25)
    elif vGold.get == 4:
        iGoldClassBonus = random.randrange(16, 33)
    elif vGold.get == 5:
        iGoldClassBonus = random.randrange(21, 43)
    elif vGold.get == 6:
        iGoldClassBonus = random.randrange(28, 56)
    elif vGold.get == 7:
        iGoldClassBonus = random.randrange(36, 72)
    elif vGold.get == 8:
        iGoldClassBonus = random.randrange(47, 94)
    else:
        iGoldClassBonus = random.randrange(60, 120)
       
    iGoldClass = iGoldClass +iGoldClassBonus
    vGold.set(str(iGoldClass))
    
    #Alignment
    vAlignClassTest = secrets.choice(iAlignClass)
    vAlign.set(str(vAlignClassTest))
    
    #Stats
    vStr.set(str(random.randrange(8, 13)+iStrBonus))
    if vRace.get() == "Gnome":
        vStr.set(str(int(vStr.get()) - 2))
    elif vRace.get() == "Half-orc":
        vStr.set(str(int(vStr.get()) + 2))
    elif vRace.get() == "Halfling":
        vStr.set(str(int(vStr.get()) - 2))
    #--------------------------------------
    vDex.set(str(random.randrange(8, 13)+iDexBonus))
    if vRace.get() == "Elf":
        vDex.set(str(int(vDex.get()) + 2))
    elif vRace.get() == "Hafling":
        vDex.set(str(int(vDex.get()) + 2))
    #--------------------------------------
    vCon.set(str(random.randrange(8, 13)+iConBonus))
    if vRace.get() == "Dwarf":
        vCon.set(str(int(vCon.get()) + 2))
    elif vRace.get() == "Elf":
        vCon.set(str(int(vCon.get()) - 2))
    elif vRace.get() == "Gnome":
        vCon.set(str(int(vCon.get()) + 2))
    #--------------------------------------
    vInt.set(str(random.randrange(8, 13)+iIntBonus))
    if vRace.get() == "Half-orc":
        vInt.set(str(int(vInt.get()) - 2))
    #--------------------------------------
    vCha.set(str(random.randrange(8, 13)+iChaBonus))
    if vRace.get() == "Dwarf":
        vCha.set(str(int(vCha.get()) - 2))
    elif vRace.get() == "Half-Orc":
        vCha.set(str(int(vCha.get()) - 2))
    #--------------------------------------
    vWis.set(str(random.randrange(8, 13)+iWisBonus))
    #--------------------------------------
    
    #APR check
    iABTotalDex = 0
    iABTotalStr = 0
    iABTotalDex = iABTotal + math.floor((int(vDex.get())-10)/2)
    iABTotalStr = iABTotal + math.floor((int(vStr.get())-10)/2)
    sABDex = ""
    sABStr = ""
    
    
    if iABTotalDex > 15:
        sABDex = "+"+str(iABTotalDex)+"/+"+str(iABTotalDex - 6)+"/+"+str(iABTotalDex - 11)+"/+"+str(iABTotalDex - 16)
    elif iABTotalDex > 10:
        sABDex = "+"+str(iABTotalDex)+"/+"+str(iABTotalDex - 6)+"/+"+str(iABTotalDex - 11)
    elif iABTotalDex > 5:
        sABDex = "+"+str(iABTotalDex)+"/+"+str(iABTotalDex - 6)
    else:
        sABDex = "+"+str(iABTotalDex)
 
    if iABTotalStr > 15:
        sABStr = "+"+str(iABTotalStr)+"/+"+str(iABTotalStr - 6)+"/+"+str(iABTotalStr - 11)+"/+"+str(iABTotalStr - 16)
    elif iABTotalStr > 10:
        sABStr = "+"+str(iABTotalStr)+"/+"+str(iABTotalStr - 6)+"/+"+str(iABTotalStr - 11)
    elif iABTotalStr > 5:
        sABStr = "+"+str(iABTotalStr)+"/+"+str(iABTotalStr - 6)
    else:
        sABStr = "+"+str(iABTotalStr)

    vAPRDex.set(sABDex)
    vAPRStr.set(sABStr)
    
    #Save
    iSaveHafling = 0
    iSaveHafling = 0
    if vRace.get() == "Halfling":
        iSaveHafling = 1
        
    iSave = math.floor((int(vCon.get())-10)/2)
    iSave = int(iSave)
    iSaveBonus = GetSaveValue(iFortClass)
    iSave = iSave + iSaveBonus + iSaveHafling
    #print("iSave="+ str(iSave))
    #print("iSaveBonus="+ str(iSaveBonus))
    vFort.set(str(iSave))
    #---------------------------------------------
    iSave = math.floor((int(vDex.get())-10)/2)
    iSave = int(iSave)
    iSaveBonus = GetSaveValue(iRefClass)
    iSave = iSave + iSaveBonus + iSaveHafling
    vRef.set(str(iSave))
    #---------------------------------------------
    iSave = math.floor((int(vWis.get())-10)/2)
    iSave = int(iSave)
    iSaveBonus = GetSaveValue(iWillClass)
    iSave = iSave + iSaveBonus + iSaveHafling
    vWill.set(str(iSave))
    
    #Height, Weight and Age
    iH = 0
    iHF = 0
    iW = 0
    if vRace.get() == "Human":
        vAge.set(int(35 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 58 + random.randrange(2, 20)
            iW = (120 * (100 + random.randrange(2, 8))/100)
        elif vSex.get() == "Female":
            iH = 53 + random.randrange(2, 20)
            iW = (85 * (100 + random.randrange(2, 8))/100)
    elif vRace.get() == "Dwarf":
        vAge.set(int(125 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 41 + random.randrange(2, 8)
            iW = (130 * (100 + random.randrange(2, 12))/100)
        elif vSex.get() == "Female":
            iW = (100 * (100 + random.randrange(2, 12))/100)
            iH = 39 + random.randrange(2, 8)
    elif vRace.get() == "Elf":
        vAge.set(int(175 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 53 + random.randrange(2, 12)
            iW = (85 * (100 + random.randrange(1, 6))/100)
        elif vSex.get() == "Female":
            iH = 53 + random.randrange(2, 12)
            iW = (80 * (100 + random.randrange(1, 6))/100)
    elif vRace.get() == "Gnome":
        vAge.set(int(100 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 36 + random.randrange(2, 8)
            iW = (40 * (100 + random.randrange(1, 3))/100)
        elif vSex.get() == "Female":
            iH = 34 + random.randrange(2, 8)
            iW = (35 * (100 + random.randrange(1, 3))/100)
    elif vRace.get() == "Half-Elf":
        vAge.set(int(62 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 55 + random.randrange(2, 16)
            iW = (100 * (100 + random.randrange(2, 8))/100)
        elif vSex.get() == "Female":
            iH = 53 + random.randrange(2, 16)
            iW = (80 * (100 + random.randrange(2, 8))/100)
    elif vRace.get() == "Half-Orc":
        vAge.set(int(30 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 58 + random.randrange(2, 24)
            iW = (150 * (100 + random.randrange(2, 12))/100)
        elif vSex.get() == "Female":
            iH = 53 + random.randrange(2, 24)
            iW = (110 * (100 + random.randrange(2, 12))/100)
    elif vRace.get() == "Halfling":
        vAge.set(int(50 * (100 + random.randrange(1, 80))/100))
        if vSex.get() == "Male": 
            iH = 32 + random.randrange(2, 8)
            iW = (30 * (100 + random.randrange(1, 3))/100)
        elif vSex.get() == "Female":
            iH = 30 + random.randrange(2, 8)
            iW = (25 * (100 + random.randrange(1, 3))/100)
              
    iHF = int(iH)/12
    iHF = math.floor(int(iHF))
    iH = int(iH) - (int(iHF) * 12)
    vHeight.set(str(iHF) +"''"+str(iH))        
    vWeight.set(str(iW) + " lbs")  
    
    #HP
    vHP.set(int((iHPClass + math.floor(int(vCon.get())-10)/2) * int(vLvl.get())))
    
    #Traits
    iRnd = random.randrange(1, 100)
    if iRnd < 4:
        vTraits.set("Abrasive")
        iSkIntiBonus += 1
        iSkDiploBonus -= 1
        iSkBluffBonus -= 1
    elif iRnd < 7:
        vTraits.set("Absent-minded")
        iSkKnowBonus += 1
        iSkSpotBonus -= 1
        iSkListenBonus -= 1
    elif iRnd < 10:
        vTraits.set("Aggressive")
        iIni += 2
        iAC -= 1
    elif iRnd < 12:
        vTraits.set("Brawler")
    elif iRnd < 14:
        vTraits.set("Cautious")
    elif iRnd < 17:
        vTraits.set("Detached")
    elif iRnd < 20:
        vTraits.set("Dishonest")
        iSkBluffBonus += 1
        iSkDiploBonus -= 2
    elif iRnd < 25:
        vTraits.set("Easygoing")
        iSkGatherBonus += 1
        iSkIntiBonus -= 1
        iSkSMBonus -= 1
    elif iRnd < 28:
        vTraits.set("Farsighted")
        iSkSpotBonus += 1
        iSkSearchBonus -= 2
    elif iRnd < 31:
        vTraits.set("Focused")
        iSkConcBonus += 1
        iSkSpotBonus -= 1
        iSkListenBonus -= 1
    elif iRnd < 34:
        vTraits.set("Hard of Hearing")
        iSkSpotBonus += 1
        iSkListenBonus -= 2
    elif iRnd < 37:
        vTraits.set("Hardy (brave)")
    elif iRnd < 40:
        vTraits.set("Honest")
        iSkDiploBonus += 1
        iSkBluffBonus -= 1
        iSkSMBonus -= 1
    elif iRnd < 42:
        vTraits.set("Illiterate")
    elif iRnd < 44:
        vTraits.set("Inattentive")
    elif iRnd < 47:
        vTraits.set("Musclebound")
    elif iRnd < 50:
        vTraits.set("Nearsighted")
        iSkSearchBonus += 1
        iSkSpotBonus -= 1
    elif iRnd < 52:
        vTraits.set("Nightsighted")
    elif iRnd < 55:
        vTraits.set("Passionate")
    elif iRnd < 58:
        vTraits.set("Plucky")
    elif iRnd < 61:
        vTraits.set("Polite")
        iSkDiploBonus += 1
        iSkIntiBonus -= 1
    elif iRnd < 63:
        vTraits.set("Quick")
    elif iRnd < 66:
        vTraits.set("Reckless")
    elif iRnd < 69:
        vTraits.set("Relentless")
    elif iRnd < 71:
        vTraits.set("Saddleborn")
        iSkRideBonus += 1
        iSkHandleBonus -= 1
    elif iRnd < 74:
        vTraits.set("Skinny")
        iSkEscapeBonus += 1
    elif iRnd < 77:
        vTraits.set("Slippery")
        iSkEscapeBonus += 1
    elif iRnd < 79:
        vTraits.set("Slow")
    elif iRnd < 82:
        vTraits.set("Specialized")
    elif iRnd < 85:
        vTraits.set("Spellgifted")
    elif iRnd < 88:
        vTraits.set("Stout")
    elif iRnd < 91:
        vTraits.set("Suspicious")
        iSkSMBonus += 1
        iSkDiploBonus -= 1
        iSkIntiBonus -= 1
    elif iRnd < 94:
        vTraits.set("Torpid")
    else:
        vTraits.set("Uncivilized")
        iSkHandleBonus += 1
        iSkBluffBonus -= 1
        iSkDiploBonus -= 1
        iSkGatherBonus -= 1
    
    #AC check, armor already there, and traits already there
    iDexArmorBonus = math.floor((int(vDex.get())-10)/2)
    if iDexArmorBonus > iArmorMaxDex:
        iDexArmorBonus = iArmorMaxDex
    iAC += 10 + iDexArmorBonus + iArmorAC
    vAC.set(iAC)
    
    #Ini
    vIni.set(str(int(iIni + (int(vDex.get())-10)/2)))
    
    #Skill
    
    #First how many skillpoint that bitch has
    iLevel = int(vLvl.get())
    if vRace.get() == "Human":
        iSkillClass = iSkillClass + 1
    iSkInt = math.floor((int(vInt.get())-10)/2)
    iSkillClass = iSkillClass + iSkInt
    iSkillClass = iSkillClass * iLevel
        
    iRnd = 0
    if iSkillClass == 0:
        iSkillClass = 1
        
    while iSkillClass > 0:
        print(iSkillClass)
        if iSkAppraiseUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkAppraise = iSkAppraise + 1
                iSkillClass = iSkillClass - 1
        if iSkBalanceUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkBalance = iSkBalance + 1
                iSkillClass = iSkillClass - 1
        if iSkBluffUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkBluff = iSkBluff + 1
                iSkillClass = iSkillClass - 1
        if iSkClimbUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkClimb = iSkClimb + 1
                iSkillClass = iSkillClass - 1
        if iSkConcUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkConc = iSkConc + 1
                iSkillClass = iSkillClass - 1
        if iSkCraftfUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkCraft = iSkCraft + 1
                iSkillClass = iSkillClass - 1
        if iSkDecifUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkDecif = iSkDecif + 1
                iSkillClass = iSkillClass - 1
        if iSkDiploUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkDiplo = iSkDiplo + 1
                iSkillClass = iSkillClass - 1
        if iSkDDUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkDD = iSkDD + 1
                iSkillClass = iSkillClass - 1
        if iSkDisgUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkDisg = iSkDisg + 1
                iSkillClass = iSkillClass - 1
        if iSkEscapeUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkEscape = iSkEscape + 1
                iSkillClass = iSkillClass - 1
        if iSkForgeryUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkForgery = iSkForgery + 1
                iSkillClass = iSkillClass - 1
        if iSkGatherUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkGather = iSkGather + 1
                iSkillClass = iSkillClass - 1
        if iSkHandleUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkHandle = iSkHandle + 1
                iSkillClass = iSkillClass - 1
        if iSkHealUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkHeal = iSkHeal + 1
                iSkillClass = iSkillClass - 1
        if iSkHideUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkHide = iSkHide + 1
                iSkillClass = iSkillClass - 1
        if iSkIntiUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkInti = iSkInti + 1
                iSkillClass = iSkillClass - 1
        if iSkJumpUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkJump = iSkJump + 1
                iSkillClass = iSkillClass - 1
        if iSkKnowUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkKnow = iSkKnow + 1
                iSkillClass = iSkillClass - 1
        if iSkListenUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkListen = iSkListen + 1
                iSkillClass = iSkillClass - 1
        if iSkMSUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkMS = iSkMS + 1
                iSkillClass = iSkillClass - 1
        if iSkOpenUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkOpen = iSkOpen + 1
                iSkillClass = iSkillClass - 1
        if iSkPerfUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkPerf = iSkPerf + 1
                iSkillClass = iSkillClass - 1
        if iSkProfUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkProf = iSkProf + 1
                iSkillClass = iSkillClass - 1
        if iSkRideUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkRide = iSkRide + 1
                iSkillClass = iSkillClass - 1
        if iSkSearchUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSearch = iSkSearch + 1
                iSkillClass = iSkillClass - 1
        if iSkSMUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSM = iSkSM + 1
                iSkillClass = iSkillClass - 1
        if iSkSleightUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSleight = iSkSleight + 1
                iSkillClass = iSkillClass - 1
        if iSkSpellcraftUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSpellcraft = iSkSpellcraft + 1
                iSkillClass = iSkillClass - 1
        if iSkSpotUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSpot = iSkSpot + 1
                iSkillClass = iSkillClass - 1
        if iSkSurvivalUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkSurvival = iSkSurvival + 1
                iSkillClass = iSkillClass - 1
        if iSkTumbleUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkTumble = iSkTumble + 1
                iSkillClass = iSkillClass - 1
        if iSkUMDUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkUMD = iSkUMD + 1
                iSkillClass = iSkillClass - 1
        if iSkRopeUnlock == 1:
            iRnd = random.randrange(0, 6)
            if iRnd == 1:
                iSkRope = iSkRope + 1
                iSkillClass = iSkillClass - 1
    #Job
    iJob = ['Abjurer', 'Acater', 'Accountant', 'Accoutrementer/Coinsmith', 'Acolyte', 'Acrobat', 'Actor', 'Actuary', 'Administrator', 'Admiral', 'Advocate', 'Aerialist/Trapezist', 'Affeeror', 'Agister', 'Alchemist', 'Alderman', 'Alienist', 'Almoner', 'Animal Collector/Monster Collector', 'Animal/Monster Handler', 'Anthropologist', 'Apothecary', 'Appraiser', 'Arborist', 'Arcane Advisor', 'Archaeologist', 'Architect', 'Archivist', 'Archmage', 'Armorer', 'Arranger', 'Artificer', 'Assassin', 'Assay Master', 'Assayer', 'Astrologer', 'Astronomer', 'Athlete', 'Auctioneer', 'Bagniokeeper', 'Bailiff', 'Baker', 'Baler', 'Bandit', 'Banker', 'Barber', 'Bard', 'Barkeep', 'Barmaid/Barboy', 'Baron/Baroness', 'Basket weaver', 'Bather', 'Beekeeper', 'Beer merchant', 'Billboardposter', 'Bishop',     'Bladesmith', 'Monster Hunter', 'Bloodletter', 'Boatman', 'Boder patrol', 'Bodyguard', 'Bookbinder', 'Bookkeeper', 'Bookseller', 'Bosun', 'Bottler', 'Bouncer', 'Bounty Hunter', 'Bowyer', 'Breeder', 'Brewer', 'Brickmaker', 'Brickmason', 'Broker', 'Broom Maker', 'Burglar','Burglary', 'Business Owner', 'Busker/Street Musician', 'Butcher', 'Butler', 'Buyer', 'Buyer', 'Cabbie/Wagoner', 'Candlemaker', 'Cantor', 'Captain', 'Caravan Guard', 'Caravaneer', 'caravanner', 'Caregiver', 'Carpenter', 'carriage driver', 'Carter', 'Cartographer', 'Cartwright', 'Castellan', 'Cavalry scout', 'Cavalryman/Cavalier', 'Celebrity', 'Chancellor', 'Chandler', 'Chaplain', 'Charcoal Maker', 'Charioteer', 'Charlatan/Conman', 'Chatelaine/Majordomo', 'Chef', 'Chemist', 'Chief', 'Chimney Sweeper', 'Choirmaster', 'City guard','City Watch', 'Clerk', 'Cloistered', 'Clown', 'Cobbler', 'Cockfighter/Gamefighter', 'Collector', 'Comedian', 'Commissar', 'Con game', 'Conductor', 'Confessor', 'Conjuror', 'Conservationist', 'Constable', 'Construction Worker', 'Contortionist', 'Cook', 'Cooper', 'Cooper/Hooper', 'Copyist', 'Costumer', 'Count/Earl/Countess', 'Courier', 'Courtier', 'Cowherd', 'Crime Boss', 'Crop farmer', 'Crossing Sweeper', 'Croupier', 'Cultist', 'Curator', 'Cutler', 'Cutpurse', 'Dairy seller', 'Dairyboy/Dairymaid', 'Dancer', 'Day laborer', 'Deacon', 'Dean', 'Debt Collector', 'Deckhand', 'Defense', 'Deserter', 'Detective/Investigator', 'Diplomacy', 'Diplomat', 'Disgraced Noble.', 'Domestic servant', 'Drakologist', 'Draper', 'Drug Dealer', 'Drug Lord', 'Druid', 'Drummer/Fifer', 'Duelist', 'Duke/Duchess', 'Dungeon Delver', 'Dyer', 'Elder', 'Elementalist', 'Embroiderer', 'Emperor/Empress', 'Enchanter/Enchantress', 'Engraver', 'Engraver', 'Entomologist', 'Entrepreneur', 'Equilibrist', 'Evangelist', 'Evoker', 'Ex-Criminal', 'Executioner', 'Exorcist', 'Explorer', 'Exterminator', 'Extortioner', 'Falconer', 'Farmer', 'Farrier', 'Fashion Designer', 'Fence', 'Ferryman', 'Firefighter', 'First Mate', 'Fisher', 'Fishmonger', 'Fletcher', 'Florist', 'Florist', 'Folk Hero', 'Food & Drink Taster', 'Forager', 'Forester', 'Forger', 'Fowler','Fugitive', 'fuller', 'Furniture Artisan', 'Furniture maker', 'Furrier', 'Furrier', 'Gambler', 'Game Hunter', 'Gamekeeper', 'Gardener', 'Gardener/Landscaper', 'Gatherer', 'General', 'General Contractor', 'Gladiator', 'Glass blower', 'Glasspainter', 'Glassworker', 'Glazier', 'Glovemaker', 'Goldsmith', 'Goldsmith/Silversmith', 'Gongfarmer', 'Grain merchant', 'Grave Robber', 'Gravedigger', 'Grocer', 'Grocer', 'Groom', 'Groundskeeper', 'Guard/Sentinel', 'Guide', 'Guild Master', 'Guild official', 'Haberdasher', 'Hatter/Milliner', 'Hay merchant', 'Healer', 'Hearth Witch/Hearth Wizard', 'Heavy cavalry', 'Heavy cavalry', 'Helmsman', 'Herald', 'Herbalist', 'Herder', 'Herder', 'Heretic', 'Hermit', 'High Priest/Pope', 'Highwayman', 'Historian', 'Honor Guard', 'Horologist', 'Horse Trainer', 'Housewife/Househusband', 'Hunter', 'Hunter', 'Hunter-gatherer', 'Illuminator', 'Illusionist', 'Inn server', 'Innkeeper', 'Inquisitor', 'Inquisitor', 'Inspection Officer', 'Instrument Maker', 'Intelligence Officer', 'Interpreter', 'inventor', 'Jailer', 'Jester', 'Jeweler', 'Judge', 'Juggler', 'Keeper of the dead', 'Kidnapper', 'King/Queen', 'Kitchen Drudge', 'Knacker', 'Knight', 'Lady-in-Waiting', 'Lamplighter', 'Land Surveyor', 'Lapidary', 'Launderer', 'Laundry Worker', 'Lawyer', 'Lawyer/Advocate','Leatherworker', 'Lector', 'Librarian', 'Lieutenant', 'Limner', 'Linguist', 'Livestock merchant', 'Loan Shark', 'Locksmith', 'Longshoreman', 'Lumberjack', 'Luthier', 'Mage', 'Magic-shop owner', 'Maid', 'Makeup Artist', 'Marksman/Archer', 'Marquess/Marchioness',     'Marshall', 'Mason', 'Master-of-Coin', 'Master-of-Horses', 'Master-of-Hounds','Master-of-the-Revels', 'Mathematician', 'Medic', 'Medium', 'Mercenary', 'Mercer', 'Merchant', 'Messager', 'Messager', 'Messenge', 'Meteorologist', 'Midwife', 'Military Navy', 'Military outfitter', 'Miller', 'Miner', 'Miner', 'Minister', 'Minstrel', 'Missionary', 'Model', 'Moneychanger', 'Moneylender', 'Mortician', 'Music Theorist', 'Musician', 'Nanny/Nursemaid', 'Naturalist', 'Nature guardian', 'Nature worshiper', 'Navigator', 'Necromancer', 'Negotiator', 'Negotiator', 'Noble/Aristocrat','Notary', 'Nun', 'Nurse', 'Official', 'Operator', 'Optician', 'Optometrist', 'Orator/Spokesman', 'Page', 'Painter', 'Painter', 'paper maker', 'Pardoner', 'Pastry Chef', 'Pathfinder', 'Pawnbroker', 'Peddler', 'Philosopher', 'pickpocket', 'Pilgrim', 'Pimp/Madame', 'Pirate', 'Plantation Owner', 'Plasterer', 'Playwright', 'Plumber', 'Plumer', 'Poacher', 'Poet', 'Poisoner','politician', 'Porter', 'Porter', 'Potion brewer', 'Potter', 'Potter', 'Priest', 'Prince/Princess', 'Printer', 'Prisoner', 'Private guard', 'Privateer', 'Professor', 'Prophet', 'Prospector', 'Prostitute', 'Protection racket', 'Purser', 'Quarryman/Quarrywoman', 'Quartermaster', 'Raider', 'Raider/Marauder', 'Ranger', 'Rat catcher', 'Rebel/Political Dissident', 'Refugee', 'Religious Scholar', 'Renderer', 'Restaurant server', 'Restorer', 'Ringmaster/Ringmistress', 'Ritualist', 'Roadlayer/Streetlayer', 'Robber', 'Roofer', 'Roofer/Thatcher', 'Rope maker', 'Ropemaker', 'Ropewalker', 'Royal Guard', 'Rug maker', 'Rugmaker', 'Runaway Slave', 'Runecaster', 'Runner', 'Sacred Librarian', 'Saddler', 'Sage', 'Sailor', 'Sailor', 'Sapper', 'Scavenger', 'Scholar', 'Scientist', 'Scout', 'Scribe', 'Sculptor', 'Sculptor', 'Sea Captain', 'Sea trader', 'Seamstress/Tailor', 'Seer/Oracle', 'Senator', 'Sergeant', 'Sergeant-at-Arms', 'Servant','Sexton', 'Shaman', 'Shapeshifter', 'Shepherd', 'Sheriff', 'Ship builder', 'Ships marine', 'Shipwrecked', 'Shipwright', 'Shock Trooper', 'Siege', 'Siege Artillerist.', 'Silversmith', 'Singer/Soprano', 'Skald', 'Skinner', 'Slave', 'Slave Driver', 'Slaver', 'Smuggler', 'Soaper', 'Soapmaker', 'Soldier', 'Soldier/Man-at-Arms', 'Sorcerer/Sorceress', 'Special Force Soldier', 'Speculator', 'spice merchant', 'Spy', 'Spymaster', 'Squatte', 'Squire', 'Stablehand', 'Stage Magician', 'Stagehand', 'Steward', 'Stonemason', 'storyteller','Stowaway', 'Street Cleaner', 'Street Crime', 'Street fighter', 'Student', 'Stuntman/Stuntwoman', 'Summoner', 'Surgeon/Chirurgeon', 'Tactician', 'Tailor', 'Talent Scout', 'Tanner', 'Tanner', 'Tattooist', 'Tavern server', 'Tax Collector', 'Taxidermist', 'Taxonomis','Teacher', 'Temple Guard', 'Temple Leader', 'Theater Director', 'Theocraft', 'Theologian', 'Thief', 'Thresher', 'Thriftdealer', 'tinker', 'Tinker', 'Tobacco merchant', 'Tollkeeper', 'Torturer', 'Tout', 'Town crier', 'Toymaker', 'Toymaker', 'Tradesman', 'Trainer', 'Translator', 'Transmuter', 'Trapper', 'Trapper', 'Traveler', 'Traveling merchant', 'Tunner', 'Tutor', 'Urchin', 'used clothier', 'Vendor', 'Veterinarian', 'village guard', 'Vintner', 'Viscount/Viscountess', 'Wandering minstrel', 'War', 'Ward', 'Warden', 'Warehouser', 'Warlock', 'Warmage', 'Watchmaker', 'Water Bearer', 'Weaponsmith', 'Weaver', 'Weaver', 'Wet Nurse', 'Wheelwright', 'Wheelwright', 'Whittler/Woodcarver', 'Wind-bringer', 'Wind-bringer', 'Wine merchant', 'Witch', 'Witchdoctor', 'Woodcarver', 'Woodseller', 'Wool merchant', 'Wordsmith', 'Wrestler', 'Writer', 'Writer', 'Zookeeper']
    vJob1.set(secrets.choice(iJob))
    vJob2.set(secrets.choice(iJob))
    vJob3.set(secrets.choice(iJob))
    
    #Race Bonus
    if vRace.get() == "Dwarf":
        iSkSearchBonus += 2
        iSkAppraiseBonus += 2
        iSkCraftBonus += 2
    elif vRace.get() == "Elf":
        iSkListenBonus += 2
        iSkSearchBonus += 2
        iSkSpotBonus += 2
    elif vRace.get() == "Gnome":
        iSkListenBonus += 2
        iSkCraftBonus += 2
    elif vRace.get() == "Half-Elf":
        iSkListenBonus += 1
        iSkSearchBonus += 1
        iSkSpotBonus += 1
        iSkDiploBonus += 2
        iSkGatherBonus += 2
    elif vRace.get() == "Halfling":
        iSkClimbBonus += 2
        iSkJumpBonus += 2
        iSkListenBonus += 2
        iSkMSBonus += 2
            
    #Skill Synergy
    if iSkBluff > 4:
        iSkDiploBonus += 2
        iSkDisgBonus += 2
        iSkIntiBonus += 2
        iSkSleightBonus += 2
    if iSkCraft > 4:
        iSkAppraiseBonus += 2
    if iSkDecif > 4:
        iSkUMDBonus += 2
    if iSkEscape > 4:
        iSkRopeBonus += 2
    if iSkHandle >4:
        iSkRideBonus += 2
    if iSkJump > 4:
        iSkTumbleBonus += 2
    if iSkKnow > 4:
        iSkSpellcraftBonus += 2
        iSkSearchBonus += 2
        iSkSurvivalBonus += 2
    if iSkSearch > 4:
        iSkSearchBonus += 2
    if iSkSM > 4:
        iSkDiploBonus += 2
    if iSkSpellcraft > 4:
        iSkUMDBonus += 2
    if iSkSurvival > 4:
        iSkKnowBonus +=2
    if iSkTumble > 4:
        iSkBalanceBonus += 2
        iSkJumpBonus += 2
    if iSkUMD > 4:
        iSkSpellcraftBonus +=2
    if iSkRope > 4:
        iSkClimbBonus +=2
        iSkEscapeBonus +=2
        
    #On rajoute le ability modifier    
    #Skill Ability modifier
    iSkStrBonus = math.floor((int(vStr.get())-10)/2)
    iSkDexBonus = math.floor((int(vDex.get())-10)/2)
    iSkConBonus = math.floor((int(vCon.get())-10)/2)
    iSkIntBonus = math.floor((int(vInt.get())-10)/2)
    iSkWisBonus = math.floor((int(vWis.get())-10)/2)
    iSkChaBonus = math.floor((int(vCha.get())-10)/2)
    
    #Str
    iSkClimbBonus += iSkStrBonus
    iSkJumpBonus += iSkStrBonus
    iSkSwimBonus += iSkStrBonus
    
    #Dex
    iSkBalanceBonus += iSkDexBonus
    iSkEscapeBonus += iSkDexBonus
    iSkHideBonus += iSkDexBonus
    iSkMSBonus += iSkDexBonus
    iSkOpenBonus += iSkDexBonus
    iSkRideBonus += iSkDexBonus
    iSkSleightBonus += iSkDexBonus
    iSkTumbleBonus += iSkDexBonus
    iSkRopeBonus += iSkDexBonus
    
    #Con
    iSkConcBonus += iSkConBonus
    
    #Int
    iSkCraftBonus += iSkIntBonus
    iSkDecifBonus += iSkIntBonus
    iSkAppraiseBonus += iSkIntBonus
    iSkDDBonus += iSkIntBonus
    iSkForgeryBonus += iSkIntBonus
    iSkKnowBonus += iSkIntBonus
    iSkSearchBonus += iSkIntBonus
    iSkSpellcraftBonus += iSkIntBonus
    
    #Wis
    iSkHealBonus += iSkWisBonus
    iSkListenBonus += iSkWisBonus
    iSkProfBonus += iSkWisBonus
    iSkSMBonus += iSkWisBonus
    iSkSpotBonus += iSkWisBonus
    iSkSurvivalBonus += iSkWisBonus
    
    #Cha
    iSkBluffBonus += iSkChaBonus
    iSkDiploBonus += iSkChaBonus
    iSkDisgBonus += iSkChaBonus
    iSkGatherBonus += iSkChaBonus
    iSkHandleBonus += iSkChaBonus
    iSkIntiBonus += iSkChaBonus
    iSkPerfBonus += iSkChaBonus
    iSkUMDBonus += iSkChaBonus
    
    #Skill Disable trained only
    if iSkDecifUnlock == 0:
        l33.config(bg="red")
    else:
        l33.config(bg="#fff")
        
    if iSkDDUnlock == 0:
        l42.config(bg="red")
    else:
        l42.config(bg="#fff")
        
    if iSkHandleUnlock == 0:
        l47.config(bg="red")
    else:
        l47.config(bg="#fff")
        
    if iSkKnowUnlock == 0:
        l35.config(bg="red")
    else:
        l35.config(bg="#fff")
        
    if iSkOpenUnlock == 0:
        l38.config(bg="red")
    else:
        l38.config(bg="#fff")
        
    if iSkProfUnlock == 0:
        l40.config(bg="red")
    else:
        l40.config(bg="#fff")
        
    if iSkSleightUnlock == 0:
        l54.config(bg="red")
    else:
        l54.config(bg="#fff")
        
    if iSkSpellcraftUnlock == 0:
        l55.config(bg="red")
    else:
        l55.config(bg="#fff")
        
    if iSkTumbleUnlock == 0:
        l59.config(bg="red")
    else:
        l59.config(bg="#fff")
        
    if iSkUMDUnlock == 0:
        l60.config(bg="red")
    else:
        l60.config(bg="#fff")
        
        
    
    #Skill On Applique les skills au slot associer
    vSk19.set(iSkAppraise + iSkAppraiseBonus)    
    vSk20.set(str(iSkBalance + iSkBalanceBonus) + " (" + str(iSkBalance + iSkBalanceBonus - iACP) + ")")       
    vSk21.set(iSkBluff + iSkBluffBonus)   
    vSk22.set(str(iSkClimb + iSkClimbBonus)    + " (" + str(iSkClimb + iSkClimbBonus - iACP) + ")") 
    vSk23.set(iSkConc + iSkConcBonus)   
    vSk24.set(iSkCraft + iSkCraftBonus)   
    vSk25.set(iSkDecif + iSkDecifBonus)   
    vSk26.set(iSkDiplo + iSkDiploBonus)   
    vSk27.set(iSkDD + iSkDDBonus)   
    vSk28.set(iSkDisg + iSkDisgBonus)   
    vSk29.set(str(iSkEscape + iSkEscapeBonus)  + " (" + str(iSkEscape + iSkEscapeBonus - iACP) + ")")   
    vSk30.set(iSkForgery + iSkForgeryBonus)   
    vSk31.set(iSkGather + iSkGatherBonus)   
    vSk32.set(iSkHandle + iSkHandleBonus)   
    vSk33.set(iSkHeal + iSkHealBonus)   
    vSk34.set(str(iSkHide + iSkHideBonus)  + " (" + str(iSkHide + iSkHideBonus - iACP) + ")")   
    vSk35.set(iSkInti + iSkIntiBonus)   
    vSk36.set(str(iSkJump + iSkJumpBonus)  + " (" + str(iSkJump + iSkJumpBonus - iACP) + ")") 
    #/////////////////////////////////
    vSkA19.set(iSkKnow + iSkKnowBonus) 
    vSkA20.set(iSkListen + iSkListenBonus) 
    vSkA21.set(str(iSkMS + iSkMSBonus)  + " (" + str(iSkMS + iSkMSBonus - iACP) + ")") 
    vSkA22.set(iSkOpen + iSkOpenBonus) 
    vSkA23.set(iSkPerf + iSkPerfBonus) 
    vSkA24.set(iSkProf + iSkProfBonus) 
    vSkA25.set(iSkRide + iSkRideBonus) 
    vSkA26.set(iSkSearch + iSkSearchBonus) 
    vSkA27.set(iSkSM + iSkSMBonus) 
    vSkA28.set(str(iSkSleight + iSkSleightBonus) + " (" + str(iSkSleight + iSkSleightBonus - iACP) + ")") 
    vSkA29.set(iSkSpellcraft + iSkSpellcraftBonus) 
    vSkA30.set(iSkSpot + iSkSpotBonus) 
    vSkA31.set(iSkSurvival + iSkSurvivalBonus) 
    vSkA32.set(str(iSkSwim + iSkSwimBonus)  + " (" + str(iSkSwim + iSkSwimBonus - (iACP *2) ) + ")") 
    vSkA33.set(str(iSkTumble + iSkTumbleBonus)  + " (" + str(iSkTumble + iSkTumbleBonus - iACP) + ")") 
    vSkA34.set(iSkUMD + iSkUMDBonus) 
    vSkA35.set(iSkRope + iSkRopeBonus) 
        
#Define Button 
b1=Button(window, text="Reset", width=9, command=lambda: ResetToNA(c1))
b1.grid(row=2,column=3) 
b2=Button(window, text="Reset", width=9, command=lambda: ResetToNA(c2))
b2.grid(row=3,column=3) 
b3=Button(window, text="Reset", width=9, command=lambda: ResetToNA(c3))
b3.grid(row=2,column=6,sticky=W) 
b6=Button(window, text="Generate", width=9, command=lambda: generate())
b6.grid(row=38,column=6) 

#Define Menu
c1list = ["Human", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc","Hafling"]
c1=ttk.Combobox(window, values = c1list, width=12)
c1.set("N/A")
c1.grid(row=2,column=2)

c2list = ["N/A", "Aristocrat", "Barbarian", "Bard", "Cleric", "Commoner", "Druid", "Expert","Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warrior","Wizard"]
c2=ttk.Combobox(window, values = c2list, width=12)
c2.set("N/A")
c2.grid(row=3,column=2)

c3list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
c3=ttk.Combobox(window, values = c3list, width=12)
c3.set("N/A")
c3.grid(row=2,column=5)

c5list = ["Human", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc","Halfling"]
c5=ttk.Combobox(window, values = c5list, width=12)
c5.set("Human")
c5.grid(row=1,column=2)

window.mainloop()