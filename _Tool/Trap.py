#Import everything from tkinter
from tkinter import *
from tkinter import Menu
from tkinter import ttk
import random
import ctypes
import secrets
import math

#Create Windows object
window=Tk()
window.title('Trap')
window.geometry("280x430")
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
file_menu.add_command(label='Which Manual?', command=lambda: Help2())
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.destroy)

# add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

#Creating trap menu
def rollTrap():
    sType2 = ""
    sTrigger = ""
    sReset = ""
    iSearch = ""
    iDD = ""
    iPrice = ""
    sName = ""
    sType = c1.get()
    sText = "•"
    iXP = "N/A"
    print("Type: " + sType)
    
    if sType == "CR1":
        c2list = ["Basic Arrow Trap",
              "Camouflaged Pit Trap",
              "Deeper Pit Trap",
              "Doorknob Smeared with Contact Poison",
              "Fusillade of Darts",
              "Poison Dart Trap",
              "Poison Needle Trap",
              "Portcullis Trap",
              "Razor-Wire across Hallway",
              "Rolling Rock Trap",
              "Scything Blade Trap",
              "Spear Trap",
              "Hall of Spears Trap",
              "Feeding Chute",
              "Swinging Block Trap",
              "Wall Blade Trap",
             ]
    elif sType == "CR2":
        c2list = ["Box of Brown Mold",
              "Bricks from Ceiling",
              "Burning Hands Trap",
              "Camouflaged Pit Trap",
              "Inflict Light Wounds Trap",
              "Javelin Trap",
              "Large Net Trap",
              "Pit Trap",
              "Poison Needle Trap",
              "Spiked Pit Trap",
              "Tripping Chain",
              "Mind Thrust Trap",
              "Dart Swarm Trap",
              "Well-Camouflaged Pit Trap"
             ]
    elif sType == "CR3":
        c2list = ["Burning Hands Trap",
              "Camouflaged Pit Trap",
              "Ceiling Pendulum",
              "Extended Bane Trap",
              "Fire Trap",
              "Ghoul Touch Trap",
              "Hail of Needles",
              "Melf ’s Acid Arrow Trap",
              "Pit Trap",
              "Destiny Dissonance Trap",
              "Poisoned Arrow Trap",
              "Spiked Pit Trap",
              "Stone Blocks from Ceiling"
             ]
    elif sType == "CR4":
        c2list = ["Bestow Curse Trap",
                  "Camouflaged Pit Trap",
                  "Collapsing Column",
                  "Glyph of Warding (Blast)",
                  "Lightning Bolt Trap",
                  "Pit Trap",
                  "Crisis of Breath Trap",
                  "Poisoned Dart Trap",
                  "Sepia Snake Sigil Trap",
                  "Crossed Swords Trap",
                  "Spiked Pit Trap",
                  "Sliding Wall Trap",
                  "Wall Scythe Trap",
                  "Missile Crystal Trap",
                  "Water-Filled Room Trap",
                  "Wide-Mouth Spiked Pit Trap"
             ]
    elif sType == "CR5":
        c2list = ["Camouflaged Pit Trap",
                  "Doorknob Smeared with Contact Poison",
                  "Falling Block Trap",
                  "Fire Trap",
                  "Fireball Trap",
                  "Flooding Room Trap",
                  "Fusillade of Darts",
                  "Moving Executioner Statue",
                  "Phantasmal Killer Trap",
                  "Pit Trap",
                  "Poison Wall Spikes",
                  "Spiked Pit Trap (80 Ft. Deep)",
                  "Spiked Pit Trap",
                  "Ego Whip Trap",
                  "Psychic Vampire Trap",
                  "Ungol Dust Vapor Trap"
             ]           
    elif sType == "CR6":
        c2list = ["Built-to-Collapse Wall",
                  "Compacting Room",
                  "Flame Strike Trap",
                  "Fusillade of Spears",
                  "Glyph of Warding (Blast)",
                  "Psychic Crush Trap",
                  "Lightning Bolt Trap",
                  "Spiked Blocks from Ceiling",
                  "Spiked Pit Trap (100 Ft. Deep)",
                  "Spiked Ceiling Trap",
                  "Summon Monster V Trap",
                  "Whirling Poison Blades",
                  "Wide-Mouth Pit Trap",
                  "Wyvern Arrow Trap"
             ]
    elif sType == "CR7":
        c2list = ["Acid Fog Trap",
                  "Blade Barrier Trap",
                  "Burnt Othur Vapor Trap",
                  "Chain Lightning Trap",
                  "Death Urge Trap",
                  "Evard’s Black Tentacles Trap",
                  "Fusillade of Greenblood Oil Darts",
                  "Lock Covered in Dragon Bile",
                  "Geyser Cavern",
                  "Summon Monster VI Trap",
                  "Antimagic Trap, Chain",
                  "Counterspell Trap",
                  "Antimagic Trap",
                  "Water-Filled Room",
                  "Well-Camouflaged Pit Trap"
             ]  
    elif sType == "CR8":
        c2list = ["Deathblade Wall Scythe",
                  "Destruction Trap",
                  "Earthquake Trap",
                  "Insanity Mist Vapor Trap",
                  "Melf ’s Acid Arrow Trap",
                  "Adder’s Breath Trap",
                  "Power Word Stun Trap",
                  "Dragon Hammer Trap",
                  "Decerebrate Trap",
                  "Prismatic Spray Trap",
                  "Reverse Gravity Trap",
                  "Retracting Bridge",
                  "Lightning Hexagon Trap",
                  "Well-Camouflaged Pit Trap",
                  "Word of Chaos Trap"
             ]
    elif sType == "CR9":
        c2list = ["Drawer Handle Smeared with Contact Poison",
                  "Dropping Ceiling",
                  "Incendiary Cloud Trap",
                  "Catapult Trap",
                  "Mindwipe Trap",
                  "Wide-Mouth Pit Trap",
                  "Wide-Mouth Spiked Pit with Poisoned Spikes"
             ]
    elif sType == "CR10":
        c2list = ["Crushing Room",
                  "Crushing Wall Trap",
                  "Energy Drain Trap",
                  "Forcecage and Summon Monster VII trap",
                  "Poisoned Spiked Pit Trap",
                  "Antimagic Trap, Greater",
                  "Razor Pendulums Trap",                  
                  "Wail of the Banshee Trap"
             ]                
    elif sType == "CR11":
        c2list = ["Greater Wyvern Arrow Trap" , "Lasting Pain Trap" , "Mind Thrust Trap"
             ] 
    elif sType == "CR12":
        c2list = ["Boulder Alley Trap" , "Dispelling Pit Trap" , "Large Flaming Greataxe Trap" , "Energy Burst Trap"
             ]                    
    elif sType == "CR13":
        c2list = ["Greensickness Spore Trap" , "Maximized Meteor Swarm Trap"
             ]               
    elif sType == "CR14":
        c2list = ["Glacial Jet Trap" , "Sucking Void Trap"
             ]               
    elif sType == "CR15":
        c2list = ["Huge Unholy Greatsword Trap"
             ]                                    
    elif sType == "CR16":
        c2list = ["Prismatic Doom Trap", "Slashing Deathblade Trap" ,"Rain of Arrows Trap"
             ]                    
    elif sType == "CR17":
        c2list = ["Deadly Needle Trap" , "Intelligent Empowered Polar Ray Trap"
             ]                                    
    elif sType == "CR18":
        c2list = ["Lava Curtains Trap"
             ]                    
    elif sType == "CR20":
        c2list = ["Dance of Death Trap"
             ]   
    elif sType == "CR22":
        c2list = ["Devil’s Throne Trap"
             ]   
    elif sType == "CR25":
        c2list = ["Glaive of Doom Trap"
             ]   
         
    sName = secrets.choice(c2list)
    #CR1 Trap
    if sName == "Basic Arrow Trap":
        sType2 = "mechanical"
        sTrigger = "proximity"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "2,000 gp"
        sText = "•Atk +10 ranged (1d6/×3, arrow)"
        iXP = "N/A"
    elif sName == "Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "24"
        iDD = "20"
        iPrice = "1,800 gp"
        sText = "•DC 20 Reflex save avoids\n•10 ft. deep (1d6, fall)"
        iXP = "N/A"
    elif sName == "Deeper Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "23"
        iDD = "20"
        iPrice = "1,300 gp"
        sText = "•Hidden switch bypass (Search DC 25)\n•DC 15 Reflex save avoids\n•20 ft. deep (2d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)"
        iXP = "N/A"
    elif sName == "Doorknob Smeared with Contact Poison":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "19"
        iDD = "19"
        iPrice = "900 gp"
        sText = "•Poison (carrion crawler brain juice, DC 13 Fortitude save resists, paralysis/0)"
    elif sName == "Fusillade of Darts":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "14"
        iDD = "20"
        iPrice = "500 gp"
        sText = "•Atk +10 ranged (1d4+1, dart)\n•Multiple targets (fires 1d4 darts at each target in two adjacent 5-ft. squares)"
        iXP = "N/A"
    elif sName == "Poison Dart Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "18"
        iPrice = "700 gp"
        sText = "•Atk +8 ranged (1d4 plus poison, dart)\n•Poison (bloodroot, D12 Fortitude save resists, 0/1d4 Con plus 1d3 Wis)"
        iXP = "N/A"
    elif sName == "Poison Needle Trap":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "22"
        iDD = "20"
        iPrice = "1,300 gp"
        sText = "•Atk +8 ranged (1 plus greenblood oil poison)"
        iXP = "N/A"
    elif sName == "Portcullis Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "1,400 gp"
        sText = "•Atk +10 melee (3d6)" + "" + "Note: Damage applies only to those underneath the portcullis. Portcullis blocks passageway." 
        iXP = "N/A"
    elif sName == "Razor-Wire across Hallway":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "no reset"
        iSearch = "22"
        iDD = "15"
        iPrice = "400 gp"
        sText = "•Atk +10 melee (2d6, wire)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)"  
        iXP = "N/A"      
    elif sName == "Rolling Rock Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "22"
        iPrice = "1,400 gp"
        sText = "•Atk +10 melee (2d6, rock)"
    elif sName == "Scything Blade Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "21"
        iDD = "20"
        iPrice = "1,700 gp"
        sText = "•Atk +8 melee (1d8/×3)"
        iXP = "N/A"
    elif sName == "Spear Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "1,200 gp"
        sText = "•Atk +12 ranged (1d8/×3, spear)" + "" + "Note: 200-ft. max range, target determined randomly from those in its path."
        iXP = "N/A"
    elif sName == "Swinging Block Trap":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "500 gp"
        sText = "•Atk +5 melee (4d6, stone block)"
        iXP = "N/A"
    elif sName == "Wall Blade Trap":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "automatic"
        iSearch = "22"
        iDD = "22"
        iPrice = "2,500 gp"
        sText = "•Hidden switch bypass (Search DC 25)\n•Atk +10 melee (2d4/×4, scythe)" 
        iXP = "N/A"
    elif sName == "Hall of Spears Trap":#
        sType2 = "mechanical"#
        sTrigger = "Trigger"#
        sReset = "Manual"#
        iSearch = "16"#
        iDD = "16"#
        iPrice = "N/A"#
        sText = "••Init +0\n•One Small shortspear (Atk +3, 1d4 points of piercing damage) per square per round\n•Duration 4 rounds"# 
        iXP = "N/A"
    elif sName == "Feeding Chute":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "22"#
        iDD = "22"#
        iPrice = "2,900 gp"#
        sText = "•Reflex DC 22 avoids\n•10 ft. deep (1d6 points of falling damage)" 
        iXP = "N/A"#
        
    #CR2 Trap
    elif sName == "Box of Brown Mold":
        sType2 = "mechanical"
        sTrigger = "location"#
        sReset = "automatic"
        iSearch = "22"
        iDD = "16"
        iPrice = "3,000 gp"
        sText = "•5-ft. cold aura (3d6, cold nonlethal)" 
        iXP = "N/A"
    elif sName == "Bricks from Ceiling":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "repair"
        iSearch = "20"
        iDD = "20"
        iPrice = "2,400 gp"
        sText = "•Atk +12 melee (2d6, bricks)\n•Multiple targets (all targets in two adjacent 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Burning Hands Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "26"
        iDD = "26"
        iPrice = "500 gp"
        sText = "•Spell effect (burning hands, 1st-level wizard, 1d4 fire, DC 11 Reflex save half damage)"
        iXP = "40" 
    elif sName == "Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "24"
        iDD = "19"
        iPrice = "3,400"
        sText = "•DC 20 Reflex save avoids\n•20 ft. deep (2d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Inflict Light Wounds Trap":
        sType2 = "magic"
        sTrigger = "touch"
        sReset = "automatic"
        iSearch = "26"
        iDD = "26"
        iPrice = "500 gp"
        sText = "•Spell effect (inflict light wounds, 1st-level cleric, 1d8+1, DC 11 Will save half damage)" 
        iXP = "40"
    elif sName == "Javelin Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "18"
        iPrice = "4,800 gp"
        sText = "•Atk +16 ranged (1d6+4, javelin)" 
        iXP = "N/A"
    elif sName == "Large Net Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "25"
        iPrice = "3,000 gp"
        sText = "•Atk +5 melee (see note)\n•Note: Characters in 10-ft. square are grappled by net (Str 18) if they fail a DC 14 Reflex save." 
        iXP = "N/A"
    elif sName == "Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "2,000 gp"
        sText = "•DC 20 Reflex save avoids\n•40 ft. deep (4d6, fall)" 
        iXP = "N/A"
    elif sName == "Poison Needle Trap":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "repair"
        iSearch = "22"
        iDD = "17"
        iPrice = "4,720 gp"
        sText = "•Lock bypass (Open Lock DC 30)\n•Atk +17 melee (1 plus poison, needle)\n•Poison (blue whinnis, DC 14 Fortitude save resists (poison only), 1 Con/unconsciousness)"
        iXP = "N/A" 
    elif sName == "Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "18"
        iDD = "15"
        iPrice = "1,600 gp"
        sText = "•DC 20 Reflex save avoids\n•20 ft. deep (2d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+2 each)" 
        iXP = "N/A"
    elif sName == "Tripping Chain":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "15"
        iDD = "18"
        iPrice = "3,800 gp"
        sText = "•Multiple traps (tripping and melee attack)\n•Atk +15 melee touch (trip), Atk +15 melee (2d4+2, spiked chain)\n•Note: This trap is really one CR 1 trap that trips and a second CR 1 trap that attacks with a spiked chain. If the tripping attack succeeds, a +4 bonus applies to the spiked chain attack because the opponent is prone." 
        iXP = "N/A"
    elif sName == "Well-Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "27"
        iDD = "20"
        iPrice = "4,400 gp"
        sText = "•DC 20 Reflex save avoids\n•10 ft. deep (1d6, fall)" 
        iXP = "N/A"
    elif sName == "Dart Swarm Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "No reset"#
        iSearch = "17"#
        iDD = "17"#
        iPrice = "N/A"#
        sText = "•Init +1\n•1d4 darts (Atk +2 ranged, 1d4 points of piercing damage) per target per round\n•Duration 9 rounds\n•Destruction AC 12; hp 5 (each ceiling square)" 
        iXP = "N/A"
    elif sName == "Mind Thrust Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "26"#
        iDD = "26"#
        iPrice = "750 gp"
        sText = "•psionic effect (mind thrust, 1st-level psion, 1d10 points of mind-affecting damage, Will DC 11 negates)" 
        iXP = "60 XP"
        
        
    #CR3 Trap
    elif sName == "Burning Hands Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "26"
        iDD = "26"
        iPrice = "2,500 gp"
        sText = "•Spell effect (burning hands, 5th-level wizard, 5d4 fire, DC 11 Reflex save half damage)" 
        iXP = "200"
    elif sName == "Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "24"
        iDD = "18"
        iPrice = "4,800 gp"
        sText = "•DC 20 Reflex save avoids\n•30 ft. deep (3d6, fall)\n•Multiple targets (first target in each of two adjacent squares)" 
        iXP = "N/A"
    elif sName == "Ceiling Pendulum":
        sType2 = "mechanical"
        sTrigger = "timed"
        sReset = "automatic"
        iSearch = "15"
        iDD = "27"
        iPrice = "14,100 gp"
        sText = "•Atk +15 melee (1d12+8/×3, greataxe)" 
        iXP = "N/A"
    elif sName == "Extended Bane Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "27"
        iDD = "27"
        iPrice = "3,500 gp"
        sText = "•Spell effect (extended bane, 3rd-level cleric, DC 13 Will save negates)" 
        iXP = "280"
    elif sName == "Fire Trap":
        sType2 = "spell"
        sTrigger = "spell"
        sReset = "no reset"
        iSearch = "27"
        iDD = "27"
        iPrice = "85 gp"
        sText = "•Spell effect (fire trap, 3rd-level druid, 1d4+3 fire, DC 13 Reflex save half damage)" 
        iXP = "N/A"
    elif sName == "Ghoul Touch Trap":
        sType2 = "magic"
        sTrigger = "touch "
        sReset = "automatic"
        iSearch = "27"
        iDD = "27"
        iPrice = "3,000 gp"
        sText = "•Spell effect (ghoul touch, 3rd-level wizard, DC 13 Fortitude save negates)" 
        iXP = "240"
    elif sName == "Hail of Needles":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "22"
        iDD = "22"
        iPrice = "5,400 gp"
        sText = "•Atk +20 ranged (2d4)" 
        iXP = "N/A"
    elif sName == "Melf ’s Acid Arrow Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "27"
        iDD = "27"
        iPrice = "3,000 gp"
        sText = "•Atk +2 ranged touch\n•Spell effect (Melf ’s acid arrow, 3rd-level wizard, 2d4 acid/round for 2 rounds)" 
        iXP = "240"
    elif sName == "Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "3,000 gp"
        sText = "•DC 20 Reflex save avoids\n•60 ft. deep (6d6, fall)" 
        iXP = "N/A"
    elif sName == "Poisoned Arrow Trap":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "19"
        iDD = "15"
        iPrice = "2,900 gp"
        sText = "•Lock bypass (Open Lock DC 30)\n•Atk +12 ranged (1d8 plus poison, arrow)\n•Poison (Large monstrous scorpion venom, DC 14 Fortitude save resists, 1d4 Con/1d4 Con)" 
        iXP = "N/A"
    elif sName == "Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "21"
        iDD = "20"
        iPrice = "3,600 gp"
        sText = "•DC 20 Reflex save avoids\n•20 ft. deep (2d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+2 each)" 
        iXP = "N/A"
    elif sName == "Stone Blocks from Ceiling":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "25"
        iDD = "20"
        iPrice = "5,400 gp"
        sText = "•Atk +10 melee (4d6, stone blocks)" 
        iXP = "N/A"
    elif sName == "Destiny Dissonance Trap":#
        sType2 = "psionic"#
        sTrigger = "touch"#
        sReset = "automatic"#
        iSearch = "27"#
        iDD = "27"#
        iPrice = "3,750 gp"#
        sText = "•psionic effect (extended destiny dissonance, 3rd-level psion, sickened for 6 rounds, no save); " 
        iXP = "180 XP"#

    #CR4
    elif sName == "Bestow Curse Trap":
        sType2 = "magic"
        sTrigger = "touch"
        sReset = "automatic"
        iSearch = "28"
        iDD = "28"
        iPrice = "8,000 gp"
        sText = "•Spell effect (bestow curse, 5th-level cleric, DC 14 Will save negates)" 
        iXP = "640"
    elif sName == "Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "25"
        iDD = "17"
        iPrice = "6,800 gp"
        sText = "•DC 20 Reflex save avoids\n•40 ft. deep (4d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Collapsing Column":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "no reset"
        iSearch = "20"
        iDD = "24"
        iPrice = "8,800 gp"
        sText = "•Atk +15 melee (6d6, stone blocks)" 
        iXP = "N/A"
    elif sName == "Glyph of Warding (Blast)":
        sType2 = "spell"
        sTrigger = "spell"
        sReset = "no reset"
        iSearch = "28"
        iDD = "28"
        iPrice = "350 gp"
        sText = "•Spell effect (glyph of warding[blast], 5th-level cleric, 2d8 acid, DC 14 Reflex save half damage)\n•Multiple targets (all targets within 5 ft.)" 
        iXP = "N/A"
    elif sName == "Lightning Bolt Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "28"
        iDD = "28"
        iPrice = "7,500 gp"
        sText = "•Spell effect (lightning bolt, 5th-level wizard, 5d6 electricity, DC 14 Reflex save half damage)" 
        iXP = "600"
    elif sName == "Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "4,000 gp"
        sText = "•DC 20 Reflex save avoids\n•80 ft. deep (8d6, fall)" 
        iXP = "N/A"
    elif sName == "Poisoned Dart Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "21"
        iDD = "22"
        iPrice = "12,090 gp"
        sText = "•Atk +15 ranged (1d4+4 plus poison, dart)\n•Multiple targets (1 dart per target in a 10-ft.-by-10-ft. area)\n•Poison (Small monstrous centipede poison, DC 10 Fortitude save resists, 1d2 Dex/1d2 Dex)" 
        iXP = "N/A"
    elif sName == "Sepia Snake Sigil Trap":
        sType2 = "spell"
        sTrigger = "spell"
        sReset = "no reset"
        iSearch = "28"
        iDD = "28"
        iPrice = "650 gp"
        sText = "•Spell effect (sepia snake sigil, 5th-level wizard, DC 14 Reflex save negates)" 
    elif sName == "Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "20"
        iDD = "20"
        iPrice = "4,000 gp"
        sText = "•DC 20 Reflex save avoids\n•60 ft. deep (6d6, fall)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+5 each)" 
        iXP = "N/A"
    elif sName == "Wall Scythe Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "21"
        iDD = "18"
        iPrice = "17,200 gp"
        sText = "•Atk +20 melee (2d4+8/×4, scythe)" 
        iXP = "N/A"
    elif sName == "Water-Filled Room Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "17"
        iDD = "23"
        iPrice = "11,200 gp"
        sText = "•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (5 rounds)\n•Liquid" 
        iXP = "N/A"
    elif sName == "Wide-Mouth Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "18"
        iDD = "25"
        iPrice = "7,200 gp"
        sText = "•DC 20 Reflex save avoids\n•20 ft. deep (2d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+2 each)" 
        iXP = "N/A"
    elif sName == "Crossed Swords Trap":
        sType2 = "mechanical"#
        sTrigger = "Detection"#
        sReset = "Auto 7rd"#
        iSearch = "19"#
        iDD = "23"#
        iPrice = "N/A"#
        sText = "•Init +2\n•One or two greatswords (Atk +4, 2d6 points of damage) per target per round\n•Duration 7 rounds\n•Destruction AC 14; nhp 10; hardness 10 (each greatsword)" 
        iXP = "N/A"  
    elif sName == "Missile Crystal Trap":#
        sType2 = "Magical"#
        sTrigger = "Detection"#
        sReset = "automatic 1m"
        iSearch = "19"#
        iDD = "26"#
        iPrice = "N/A"
        sText = "•Init +2\n•One magic missile (automatically hits, 1d4+1 points of damage, CL 5th) per crystal per creature\n•Duration 7 rounds\n•Destruction AC 14; nhp 10; hardness 5 (each corner crystal)\n•Destruction AC 16; hp 18; hardness 5 (crystal chest)" 
        iXP = "N/A"
    elif sName == "Sliding Wall Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "29"#
        iDD = "24"#
        iPrice = "28,400 gp"#
        sText = "•DC 30 Reflex save avoids\n•20 ft. deep (2d6 points of falling damage)\n•multiple targets (all within a 10-ft.-by-15 ft. area)" 
        iXP = "N/A"
    elif sName == "Crisis of Breath Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "28"#
        iDD = "28"#
        iPrice = "8,750 gp"
        sText = "•psionic effect (crisis of breath, 5th-level psion, unable to breathe except as a standard action, Will DC 14 negates)" 
        iXP = "700 XP"       
    
    #CR5
    elif sName == "Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "25"
        iDD = "17"
        iPrice = "8,500 gp"
        sText = "•DC 20 Reflex save avoids\n•50 ft. deep (5d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Doorknob Smeared with Contact Poison":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "25"
        iDD = "19"
        iPrice = "9,650 gp"
        sText = "•Poison (nitharit, DC 13 Fortitude save resists, 0/3d6 Con)" 
        iXP = "N/A"
    elif sName == "Falling Block Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "25"
        iPrice = "15,000 gp"
        sText = "•Atk +15 melee (6d6)\n•Multiple targets (can strike all characters in two adjacent specified squares)" 
        iXP = "N/A"
    elif sName == "Fire Trap":
        sType2 = "spell"
        sTrigger = "spell"
        sReset = "no reset"
        iSearch = "29"
        iDD = "29"
        iPrice = "305 gp"
        sText = "•Spell effect (fire trap, 7th-level wizard, 1d4+7 fire, DC 16 Reflex save half damage)" 
        iXP = "N/A"
    elif sName == "Fireball Trap":
        sType2 = "magic"
        sTrigger = "touch"
        sReset = "automatic"
        iSearch = "28"
        iDD = "28"
        iPrice = "12,000 gp"
        sText = "•Spell effect (fireball, 8th-level wizard, 8d6 fire, DC 14 Reflex save half damage)" 
        iXP = "960"
    elif sName == "Flooding Room Trap":
        sType2 = "mechanical"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "20"
        iDD = "25"
        iPrice = "17,500 gp"
        sText = "•No attack roll necessary (see note below)\n•Note: Room floods in 4 rounds (see Drowning, page 304)." 
        iXP = "N/A"
    elif sName == "Fusillade of Darts":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "19"
        iDD = "25"
        iPrice = "18,000 gp"
        sText = "•Atk +18 ranged (1d4+1, dart)\n•Multiple targets (1d8 darts per target in a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Moving Executioner Statue":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "25"
        iDD = "18"
        iPrice = "22,500 gp"
        sText = "•Hidden switch bypass (Search DC 25)\n•Atk +16 melee (1d12+8/×3, greataxe)\n•Multiple targets (both arms attack)"
        iXP = "N/A" 
    elif sName == "Phantasmal Killer Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "29"
        iDD = "29"
        iPrice = "14,000 gp"
        sText = "•Spell effect (phantasmal killer, 7th-level wizard, DC 16 Will save for disbelief and DC 16 Fort save for partial effect)" 
        iXP = "1120"
    elif sName == "Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "5,000 gp"
        sText = "•DC 20 Reflex save avoids\n•100 ft. deep (10d6, fall)" 
        iXP = "N/A"
    elif sName == "Poison Wall Spikes":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "17"
        iDD = "21"
        iPrice = "12,650 gp"
        sText = "•Atk +16 melee (1d8+4 plus poison, spike)\n•Multiple targets (closest target in each of two adjacent 5-ft. squares)\n•Poison (Medium monstrous spider venom, DC 12 Fortitude save resists, 1d4 Str/1d4 Str)" 
        iXP = "N/A"
    elif sName == "Spiked Pit Trap (80 Ft. Deep)":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "21"
        iDD = "20"
        iPrice = "13,500 gp"
        sText = "•DC 25 Reflex save avoids\n•40 ft. deep (4d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+4 each)" 
        iXP = "N/A"
    elif sName == "Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "21"
        iDD = "20"
        iPrice = "13,500 gp"
        sText = "•DC 25 Reflex save avoids\n•40 ft. deep (4d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+4 each)" 
        iXP = "N/A"
    elif sName == "Ungol Dust Vapor Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "16"
        iPrice = "9,000 gp"
        sText = "•Gas\n•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (2 rounds)\n•Poison (ungol dust, DC 15 Fortitude save resists, 1 Cha/1d6 Cha plus 1 Cha drain)" 
        iXP = "N/A"
    elif sName == "Ego Whip Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "29"#
        iDD = "29"#
        iPrice = "15,750 gp"
        sText = "•psionic effect (ego whip, 7th-level psion, augmented by 4 power points, 2d4 points of Cha damage [Will DC 15 half], dazed for 1 round [Will DC 15 negates])" 
        iXP = "1,260 XP" 
    elif sName == "Psychic Vampire Trap":#
        sType2 = "psionic"#
        sTrigger = "touch/psi"#
        sReset = "automatic"#
        iSearch = "29"#
        iDD = "29"#
        iPrice = "16,500 gp"#
        sText = "•psionic effect (psychic vampire, 7th-level psion, drains 14 power points or deals 2 points of Wis damage to creatures that have no power points, Fortitude DC 16 negates)" 
        iXP = "1,320 XP"#

    #CR6
    elif sName == "Built-to-Collapse Wall":
        sType2 = "mechanical"
        sTrigger = "proximity"
        sReset = "no reset"
        iSearch = "14"
        iDD = "16"
        iPrice = "15,000 gp"
        sText = "•Atk +20 melee (8d6, stone blocks)\n•Multiple targets (all targets in a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Compacting Room":
        sType2 = "mechanical"
        sTrigger = "timed"
        sReset = "automatic"
        iSearch = "25"
        iDD = "22"
        iPrice = "25,200 gp"
        sText = "•Walls move together (12d6, crush)\n•Multiple targets (all targets in a 10-ft.-by10-ft. room)\n•Never miss\n•Onset delay (4 rounds)"  + "" + "Note: Hidden switch bypass"
        iXP = "N/A"
    elif sName == "Flame Strike Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "30"
        iDD = "30"
        iPrice = "22,750 gp"
        sText = "•Spell effect (flame strike, 9th-level cleric, 9d6 fire, DC 17 Reflex save half damage)" 
        iXP = "1820"
    elif sName == "Fusillade of Spears":
        sType2 = "mechanical"
        sTrigger = "proximity"
        sReset = "repair"
        iSearch = "26"
        iDD = "20"
        iPrice = "31,200 gp"
        sText = "•Atk +21 ranged (1d8, spear)\n•Multiple targets (1d6 spears per target in a 10 ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Glyph of Warding (Blast)":
        sType2 = "spell"
        sTrigger = "spell"
        sReset = "no reset"
        iSearch = "28"
        iDD = "28"
        iPrice = "680 gp"
        sText = "•Spell effect (glyph of warding [blast], 16th-level cleric, 8d8 sonic, DC 14 Reflex save half damage)\n•Multiple targets (all targets within 5 ft.)" 
        iXP = "N/A"
    elif sName == "Lightning Bolt Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "28"
        iDD = "28"
        iPrice = "15,000 gp"
        sText = "•Spell effect (lightning bolt, 10th-level wizard, 10d6 electricity, DC 14 Reflex save half damage)" 
        iXP = "1200"
    elif sName == "Spiked Blocks from Ceiling":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "24"
        iDD = "20"
        iPrice = "21,600 gp"
        sText = "•Atk +20 melee (6d6, spikes)\n•Multiple targets (all targets in a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Spiked Pit Trap (100 Ft. Deep)":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "6,000 gp"
        sText = "•DC 20 Reflex save avoids\n•100 ft. deep (10d6, fall)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+5 each)" 
        iXP = "N/A"
    elif sName == "Whirling Poison Blades":
        sType2 = "mechanical"
        sTrigger = "timed"
        sReset = "automatic"
        iSearch = "20"
        iDD = "20"
        iPrice = "30,200 gp"
        sText = "•Hidden lock bypass (Search DC 25, Open Lock DC 30)\n•Atk +10 melee (1d4+4/19–20 plus poison, dagger)\n•Poison (purple worm poison, DC 24 Fortitude save resists, 1d6 Str/2d6 Str)\n•Multiple targets (one target in each of three preselected 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Wide-Mouth Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "26"
        iDD = "25"
        iPrice = "28,200 gp"
        sText = "•DC 25 Reflex save avoids\n•40 ft. deep (4d6, fall)\n•Multiple targets (all targets within a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Wyvern Arrow Trap":
        sType2 = "mechanical"
        sTrigger = "proximity"
        sReset = "manual"
        iSearch = "20"
        iDD = "16"
        iPrice = "17,400 gp"
        sText = "•Atk +14 ranged (1d8 plus poison, arrow)\n•Poison (wyvern poison, DC 17 Fortitude save resists, 2d6 Con/2d6 Con)"
        iXP = "N/A" 
    elif sName == "Spiked Ceiling Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "Auto 9rd"#
        iSearch = "21"#
        iDD = "27"#
        iPrice = "N/A"#
        sText = "•Init +3\n•Spikes (Atk +8 melee, 1d6 spikes per target for 1d8+1 piercing damage); reduce the number of spikes by 1 for each chain mechanism disabled or destroyed (minimum 0)\n•Duration 9 rounds\n•Destruction AC 16; hp 15 (all spikes in one square)\n•Destruction AC 19; hp 27 (each chain mechanism)" 
        iXP = "N/A"       
    elif sName == "Summon Monster V Trap":#
        sType2 = "magic"#
        sTrigger = "proximity"#
        sReset = "automatic"#
        iSearch = "30"#
        iDD = "30"#
        iPrice = "4,700 gp"#
        sText = "•magic effect (summon monster V, 9th-level wizard, fiendish dire wolverine)\n•magic effect (arcane mark, 1st-level wizard, inscribes rune on summoned monster)" 
        iXP = "1,820 XP"#
    elif sName == "Baleful Teleport Trap":#
        sType2 = "psionic"#
        sTrigger = "proximity"#
        sReset = "automatic"#
        iSearch = "30"#
        iDD = "30"#
        iPrice = "33,500 gp"#
        sText = "•psionic effect (baleful teleport, 9th-level psion, 9d6 points of damage, Fortitude DC 17 half)" 
        iXP = "2,680 XP"#
    elif sName == "Psychic Crush Trap":
        sType2 = "psionic"#
        sTrigger = "thought"#
        sReset = "automatic"#
        iSearch = "30"#
        iDD = "30"#
        iPrice = "28,500 gp"#
        sText = "•psionic effect (psychic crush, 9th-level psion, target drops to –1 hit points, Will DC 16 (made at +4) partial (target takes 3d6 points of mind-affecting damage)" 
        iXP = "2,280 XP"#
        
    #CR7
    elif sName == "Acid Fog Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "31"
        iDD = "31"
        iPrice = "33,000 gp"
        sText = "•Spell effect (acid fog, 11th-level wizard, 2d6/round acid for 11 rounds)" 
        iXP = "2640"
    elif sName == "Blade Barrier Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "31"
        iDD = "31"
        iPrice = "33,000 gp"
        sText = "•Spell effect (blade barrier, 11th-level cleric, 11d6 slashing, DC 19 Reflex save half damage)"
        iXP = "2640" 
    elif sName == "Burnt Othur Vapor Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "21"
        iDD = "21"
        iPrice = "17,500 gp"
        sText = "•Gas\n•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (3 rounds)\n•Poison (burnt othur fumes, DC 18 Fortitude save resists, 1 Con drain/3d6 Con)" 
        iXP = "N/A"
    elif sName == "Chain Lightning Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "31"
        iDD = "31"
        iPrice = "33,000 gp"
        sText = "•Spell effect (chain lightning, 11th-level wizard, 11d6 electricity to target nearest center of trigger area plus 5d6 electricity to each of up to eleven secondary targets, DC 19 Reflex save half damage)" 
        iXP = "2640"
    elif sName == "Evard’s Black Tentacles Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "no reset"
        iSearch = "29"
        iDD = "29"
        iPrice = "1,400 gp"
        sText = "•Spell effect (Evard’s black tentacles, 7th-level wizard, 1d4+7 tentacles, Atk +7 melee [1d6+4, tentacle])\n•Multiple targets (up to six tentacles per target in each of two adjacent 5-ft. squares)" 
        iXP = "112"
    elif sName == "Fusillade of Greenblood Oil Darts":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "25"
        iDD = "25"
        iPrice = "33,000 gp"
        sText = "•Atk +18 ranged (1d4+1 plus poison, dart)\n•Poison (greenblood oil, DC 13 Fortitude save resists, 1 Con/1d2 Con)\n•Multiple targets (1d8 darts per target in a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Lock Covered in Dragon Bile":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "no reset"
        iSearch = "27"
        iDD = "16"
        iPrice = "11,300 gp"
        sText = "•Poison (dragon bile, DC 26 Fortitude save resists, 3d6 Str/0)" 
        iXP = "N/A"
    elif sName == "Summon Monster VI Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "no reset"
        iSearch = "31"
        iDD = "31"
        iPrice = "3,300 gp"
        sText = "•Spell effect (summon monster VI, 11th-level wizard)" 
        iXP = "264"
    elif sName == "Water-Filled Room":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "25"
        iPrice = "21,000 gp"
        sText = "•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (3 rounds)\n•Water" 
        iXP = "N/A"
    elif sName == "Well-Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "27"
        iDD = "18"
        iPrice = "24,500 gp"
        sText = "•DC 25 Reflex save avoids\n•70 ft. deep (7d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)" 
        iXP = "N/A"
    elif sName == "Antimagic Trap":#
        sType2 = "magic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "31"#
        iDD = "31"#
        iPrice = "66,000 gp"#
        sText = "•spell effect (antimagic field, 11thlevel wizard, 10-ft.-radius antimagic emanation for 110 minutes)" 
        iXP = "2,640 XP"#
    elif sName == "Geyser Cavern":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "300 yr"#
        iSearch = "22"#
        iDD = "22"#
        iPrice = "N/A"#
        sText = "•Init +3\n•Scalding hot jets of water (automatically hit, 4d6 points of bludgeoning damage + 5d6 points of fire damage, DC 17 Reflex half)\n•trap attacks 10 random squares per round\n•Duration 10 rounds" #
        iXP = "N/A"
    elif sName == "Antimagic Trap, Chain":#
        sType2 = "magic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "31#"#
        iDD = "31"#
        iPrice = "68,500 gp"#
        sText = "•spell effect (antimagic field, 11th-level wizard, 10-ft.-radius antimagic emanation for 110 minutes), spell effect (dancing lights, 11th-level wizard)" 
        iXP = "2,740 XP"#
    elif sName == "Counterspell Trap":#
        sType2 = "magic"#
        sTrigger = "intelligent"#
        sReset = "automatic"#
        iSearch = "31"#
        iDD = "31"#
        iPrice = "57,000 gp"#
        sText = "•magic effect (greater dispel magic, 15th-level wizard, counterspells, dispel check +15)\n•Int 13, Wis 13, Cha 10, Ego 4; Spellcraft +11, Spot +11" 
        iXP = "4,080 XP"#
    elif sName == "Death Urge Trap":#
        sType2 = "psionic"#
        sTrigger = "hostility"#
        sReset = "automatic"#
        iSearch = "31"#
        iDD = "31"#
        iPrice = "39,500 gp"#
        sText = "•psionic effect (death urge, 11th-level psion, augmented by 4 power points, target seeks to end its own life for 2 rounds, Will DC 18 negates);" #
        iXP = "3,160 XP"#
       
    #CR8
    elif sName == "Deathblade Wall Scythe":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "24"
        iDD = "19"
        iPrice = "31,400 gp"
        sText = "•Atk +16 melee (2d4+8 plus poison, scythe)\n•Poison (deathblade, DC 20 Fortitude save resists, 1d6 Con/2d6 Con)" 
        iXP = "N/A"
    elif sName == "Destruction Trap":
        sType2 = "magic"
        sTrigger = "touch"
        sReset = "automatic"
        iSearch = "32"
        iDD = "32"
        iPrice = "45,500 gp"
        sText = "•Spell effect (destruction, 13th-level cleric, DC 20 Fortitude save for 10d6 damage)" 
        iXP = "3640"
    elif sName == "Earthquake Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "32"
        iDD = "32"
        iPrice = "45,500 gp"
        sText = "•Spell effect (earthquake, 13th-level cleric, 65-ft. radius, DC 15 or 20 Reflex save, depending on terrain)" 
        iXP = "3,640"
    elif sName == "Insanity Mist Vapor Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "25"
        iDD = "20"
        iPrice = "23,900 gp"
        sText = "•Gas\n•Never miss\n•Onset delay (1 round)\n•Poison (insanity mist, DC 15 Fortitude save resists, 1d4 Wis/2d6 Wis)\n•Multiple targets (all targets in a 10-ft.-by-10-ft. room)" 
        iXP = "N/A"
    elif sName == "Melf ’s Acid Arrow Trap":
        sType2 = "magic"
        sTrigger = "visual"
        sReset = "automatic"
        iSearch = "27"
        iDD = "27"
        iPrice = "83,500 gp"
        sText = "•Multiple traps (two simultaneous Melf ’s acid arrow traps)\n•Atk +9 ranged touch and +9 ranged touch\n•Spell effect (Melf ’s acid arrow, 18th-level wizard, 2d4 acid damage for 7 rounds)" 
        iXP = "4,680 XP"
    elif sName == "Power Word Stun Trap":
        sType2 = "magic"
        sTrigger = "touch"
        sReset = "no reset"
        iSearch = "32"
        iDD = "32"
        iPrice = "4,550 gp"
        sText = "•Spell effect (power word stun, 13th-level wizard)," 
        iXP = "364 XP"
    elif sName == "Prismatic Spray Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "trigger"
        iSearch = "32"
        iDD = "32"
        iPrice = "45,500 gp"
        sText = "•Automatic reset\n•Spell effect (prismatic spray, 13th-level wizard, DC 20 Reflex, Fortitude, or Will save, depending on effect)" 
        iXP = "3,640 XP"
    elif sName == "Reverse Gravity Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "32"
        iDD = "32"
        iPrice = "45,500 gp"
        sText = "•Spell effect (reverse gravity, 13th-level wizard, 6d6 fall [upon hitting the ceiling of the 60-ft.-high room], then 6d6 fall [upon falling 60 ft. to the floor when the spell ends], DC 20 Reflex save avoids damage)" 
        iXP = "3,640 XP"
    elif sName == "Well-Camouflaged Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "27"
        iDD = "18"
        iPrice = "16,000 gp"
        sText = "•DC 20 Reflex save avoids\n•100 ft. deep (10d6, fall)" 
        iXP = "N/A"
    elif sName == "Word of Chaos Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "32"
        iDD = "32"
        iPrice = "46,000 gp"
        sText = "•Spell effect (word of chaos, 13th-level cleric)" 
        iXP = "3,680 XP"
    elif sName == "Adder’s Breath Trap":#
        sType2 = "Magical"#
        sTrigger = "Touch"#
        sReset = "Auto 11rd"#
        iSearch = "23"#
        iDD = "29"#
        iPrice = "N/A"
        sText = "•Init +4\n•Poison (Atk +8 ranged touch, 1d10 points of Con damage, DC 16 Fortitude negates, save again after 1 minute, CL 7th)\n•two random targets per round\n•Duration 11 rounds\n•Destruction AC 18; hp 20; hardness 8 (each spitting statue)\n•Destruction AC 22; hp 12; hardness 8 (each serpent holding the treasure)" 
        iXP = "N/A"    
    elif sName == "Dragon Hammer Trap":#
        sType2 = "Mechanical"#
        sTrigger = "Detection"#
        sReset = "Auto 11rd"
        iSearch = "23"#
        iDD = "23"#
        iPrice = "N/A"#
        sText = "•Init +4\n•One stone column (Atk +8, 6d6 points of damage) in each of four alcoves, or\n•Jet of alchemical flame (6d6 fire damage, DC 18 Reflex half) in whole room except alcoves\n•Duration 11 rounds\n•Destruction AC 18; hp 20; hardness 8 (each column)\n•Destruction AC 18; hp 28; hardness 8 (dragon statue)"# 
        iXP = "N/A"#
    elif sName == "Lightning Hexagon Trap":#
        sType2 = "Magic"#
        sTrigger = "Detection"#
        sReset = "No reset"#
        iSearch = "23"#
        iDD = "28"#
        iPrice = "46,000 gp"
        sText = "•Init +4\n•Effect Lightning bolt (8d6 points of damage, Reflex DC 14 half) shoots between three pillars\n•Duration 11 rounds\n•Destruction AC 18; hp 20; hardness 8 (each pillar)" 
        iXP = "N/A"
    elif sName == "Retracting Bridge":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "29"#
        iDD = "24"#
        iPrice = "50,400 gp"#
        sText = "•multiple targets (all creatures in a 20-ft.-by-5-ft. area), retracting bridge (dumps into water, Reflex DC 29 to cling to bridge as it retracts, Climb DC 15 to return to edge of pit); " 
        iXP = "N/A"#
    elif sName == "Decerebrate Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "32"#
        iDD = "32"#
        iPrice = "73,500 gp"
        sText = "•psionic effect (decerebrate, 13thlevel psion, target loses all mental unctions and dies in 1d4 days, Fortitude DC 20 negates); " #
        iXP = "5,880 XP"
      
        
    #CR9
    elif sName == "Drawer Handle Smeared with Contact Poison":
        sType2 = "mechanical"
        sTrigger = "touch"
        sReset = "manual"
        iSearch = "18"
        iDD = "26"
        iPrice = "21,600 gp"
        sText = "•Poison (black lotus extract, DC 20 Fortitude save resists, 3d6 Con/3d6 Con)" 
        iXP = "N/A"
    elif sName == "Dropping Ceiling":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "repair"
        iSearch = "20"
        iDD = "16"
        iPrice = "12,600 gp"
        sText = "•Ceiling moves down (12d6, crush)\n•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (1 round)" 
        iXP = "N/A"
    elif sName == "Incendiary Cloud Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "33"
        iDD = "33"
        iPrice = "60,000 gp"
        sText = "•Spell effect (incendiary cloud, 15th-level wizard, 4d6/round for 15 rounds, DC 22 Reflex save half damage)" 
        iXP = "4,800 XP"
    elif sName == "Wide-Mouth Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "25"
        iDD = "25"
        iPrice = "40,500 gp"
        sText = "•DC 25 Reflex save avoids\n•100 ft. deep (10d6, fall)\n•Multiple targets (all targets within a 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
    elif sName == "Wide-Mouth Spiked Pit with Poisoned Spikes":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "20"
        iDD = "20"
        iPrice = "11,910 gp"
        sText = "•Hidden lock bypass (Search DC 25, Open Lock DC 30)\n•DC 20 Reflex save avoids\n•70 ft. deep (7d6, fall)\n•Multiple targets (all targets within a 10-ft.-by-10-ft. area)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+5 plus poison each)\n•Poison (giant wasp poison, DC 14 Fortitude save resists, 1d6 Dex/1d6 Dex)" 
        iXP = "N/A"
    elif sName == "Sliding Wall Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "24"#
        iDD = "15"#
        iPrice = "23,080 gp"#
        sText = "•Reflex DC 24 avoids; 2,000 ft. thrown (20d6 points of falling damage)\n•multiple targets (all within a 10-ft.-by-10 ft. area)" 
        iXP = "N/A"#
    elif sName == "Mindwipe Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "33"#
        iDD = "33"#
        iPrice = "73,500 gp"
        sText = "•psionic effect (mindwipe, 13th-level psion, augmented by 6 power points, bestows three negative levels, Fortitude DC 18 negates)" 
        iXP = "5,880 XP"
        
    #CR10
    elif sName == "Crushing Room":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "22"
        iDD = "20"
        iPrice = "29,000 gp"
        sText = "•Walls move together (16d6, crush)\n•Multiple targets (all targets in a 10-ft.-by-10-ft. room)\n•Never miss\n•Onset delay (2 rounds)" 
        iXP = "N/A"
    elif sName == "Crushing Wall Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "automatic"
        iSearch = "20"
        iDD = "25"
        iPrice = "25,000 gp"
        sText = "•No attack roll required (18d6, crush)" 
        iXP = "N/A"
    elif sName == "Energy Drain Trap":
        sType2 = "magic"
        sTrigger = "visual"
        sReset = "automatic"
        iSearch = "34"
        iDD = "34"
        iPrice = "124,000 gp"
        sText = "•Atk +8 ranged touch\n•Spell effect (energy drain, 17th-level wizard, 2d4 negative levels for 24 hours, DC 23 Fortitude save negates)" 
        iXP = "7,920 XP"
    elif sName == "Forcecage and Summon Monster VII trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "32"
        iDD = "32"
        iPrice = "241,000 gp"
        sText = "•Multiple traps (one forcecage trap and one summon monster VII trap that summons a hamatula)\n•Spell effect (forcecage, 13th-level wizard), spell effect (summon monster VII, 13th-level wizard, hamatula)" 
        iXP = "7,280 XP"
    elif sName == "Poisoned Spiked Pit Trap":
        sType2 = "mechanical"
        sTrigger = "location"
        sReset = "manual"
        iSearch = "16"
        iDD = "25"
        iPrice = "19,700 gp"
        sText = "•Hidden lock bypass (Search DC 25, Open Lock DC 30)\n•DC 20 Reflex save avoids\n•50 ft. deep (5d6, fall)\n•Multiple targets (first target in each of two adjacent 5-ft. squares)\n•Pit spikes (Atk +10 melee, 1d4 spikes per target for 1d4+5 plus poison each)\n•Poison (purple worm poison, DC 24 Fortitude save resists, 1d6 Str/2d6 Str)" 
        iXP = "N/A"
    elif sName == "Wail of the Banshee Trap":
        sType2 = "magic"
        sTrigger = "proximity"
        sReset = "automatic"
        iSearch = "34"
        iDD = "34"
        iPrice = "76,500 gp"
        sText = "•Spell effect (wail of the banshee, 17th-level wizard, DC 23 Fortitude save negates)\n•Multiple targets (up to 17 creatures)" 
        iXP = "6,120 XP"
    elif sName == "Razor Pendulums Trap":#
        sType2 = "Mechanical"#
        sTrigger = "Detection"#
        sReset = "Auto 13rd"
        iSearch = "25"#
        iDD = "25"#
        iPrice = "N/A"
        sText = "•Init +5\n•12 pendulum blades (Atk +10 melee, 7d6 points of slashing damage)\n•each blade attacks all creatures in one 5-foot by-20-foot row\n•Duration 13 rounds\n•Destruction AC 20; hp 20 (each pendulum)" 
        iXP = "N/A"#
    elif sName == "Antimagic Trap, Greater":#
        sType2 = "magic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "34"#
        iDD = "34"#
        iPrice = "127,500 gp"#
        sText = "•spell effect (widened antimagic field, 17th-level wizard, 20-ft.-radius antimagic emanation for 170 minutes)" 
        iXP = "5,100 XP"
    
    #CR11
    elif sName == "Greater Wyvern Arrow Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "manual"#
        iSearch = "28"#
        iDD = "24"#
        iPrice = "77,600 gp"
        sText = "•Atk +24 ranged (1d8+4 plus poison, arrow); poison (Gargantuan wyvern poison, Fort DC 21 resists, 2d6 Con/2d6 Con); " 
        iXP = "N/A"
    elif sName == "Lasting Pain Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "32"#
        iDD = "30"#
        iPrice = "230,450 gp"#
        sText = "•Atk +36 ranged (1d8+5 plus 1d6 electricity plus poison, +1 shocking arrow); poison (shrieking terror saliva, Fort DC 19 resists, unable to heal wound caused by trap magically or naturally); " 
        iXP = "N/A"#
    elif sName == "Mind Thrust Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "34"
        iDD = "34"
        iPrice = "124,500 gp"
        sText = "•psionic effect (mind thrust, 19th-level psion, augmented by 18 power points, 19d10 points of mind-affecting damage, Will DC 20 negates)" 
        iXP = "9,960 XP"
     
    
    #CR12    
    elif sName == "Boulder Alley Trap":#
        sType2 = "magic/mecha"#
        sTrigger = "Location"#
        sReset = "No Reset"#
        iSearch = "27"#
        iDD = "30"#
        iPrice = "N/A"#
        sText = "•Init +6\n•Rolling boulder (10d6 points of bludgeoning damage, DC 22 Reflex negates), and Effect Hold monster (duration 9 rounds, DC 17 Will save each round negates) on targets not already held\n•the effect emanates from glyphs in the center of each groove\n•dispelling or destroying a glyph eliminates this effect in its groove\n•Duration 15 rounds\n•Destruction AC 22; hp 30; hardness 8 (each boulder)\n•Destruction AC 22; hp 30 (each glyph)" 
        iXP = "N/A"#
    elif sName == "Dispelling Pit Trap":#
        sType2 = "Magical"#
        sTrigger = "Detection"#
        sReset = "No Reset"#
        iSearch = "27"#
        iDD = "31"#
        iPrice = "N/A"#
        sText = "•Init +6\n•Effect Greater dispel magic (cast at each target in the area of the pit, CL 13th)\n•anyone falling in the pit takes 6d6 points of falling damage\n•Duration 15 rounds\n•Destruction AC 28; hp 54; hardness 8 (stone face)" 
        iXP = "N/A"#
    elif sName == "Large Flaming Greataxe Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "34"#
        iDD = "30"#
        iPrice = "367,600 gp"#
        sText = "•Atk +30 melee (3d6+13 plus 1d6 fire, Large +1 flaming greataxe); " #
        iXP = "N/A"#
    elif sName == "Energy Burst Trap":#
        sType2 = "psionic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "36"#
        iDD = "36"#
        iPrice = "134,750 gp"#
        sText = "•psionic effect (energy burst, 20th-level psion, augmented by 15 power points, 20d6+20 points of cold damage, Fortitude DC 20 half)\n•multiple targets (40-ft.-radius burst) " 
        iXP = "10,780 XP"

    #CR13
    elif sName == "Greensickness Spore Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "repair"#
        iSearch = "28"#
        iDD = "28"#
        iPrice = "69,000 gp"#
        sText = "•gas\n•never miss\n•onset delay (1 round)\n•poison (greensickness, Fort DC 33 resists, 2d6 Str + 1d4 Con/2d6 Str + 1d4 Con)\n•multiple targets (all in 10-ft.-by-10-ft. room) " 
        iXP = "N/A"
    elif sName == "Maximized Meteor Swarm Trap":#
        sType2 = "magic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "37"#
        iDD = "37"#
        iPrice = "166,500 gp"#
        sText = "•Atk +12/+12/+12/+12 ranged touch\n•spell effect (maximized meteor swarm, 24th-level wizard, 12 points of bludgeoning damage and 36 points of fire damage per hit, 36 points of fire damage to all creatures within 40 ft. of each hit [Reflex DC 28 half])" 
        iXP = "13,320 XP"
    

    #CR14
    elif sName == "Glacial Jet Trap":#
        sType2 = "Mechanical"#
        sTrigger = "Detection"#
        sReset = "No Reset"#
        iSearch = "34"##
        iDD = "29"#
        iPrice = "N/A"#
        sText = "•Init +7\n•Jet of freezing water (8d6 points of cold damage + 4d6 points of nonlethal damage, Reflex DC 22 half)\n•targets who fail their save are also knocked prone by the force of the water\n•Duration 17 rounds\n•Destruction hp 180 (+20 hp per round while jet sprays), hardness 5 (fire damage ignores hardness and deals 1-1/2 × damage) (block of ice)" #
        iXP = "N/A"#
    elif sName == "Sucking Void Trap":#
        sType2 = "magic"#
        sTrigger = "visual"#
        sReset = "automatic"#
        iSearch = "34"#
        iDD = "34"#
        iPrice = "272,000 gp"
        sText = "•spell effect (greater dispel magic, 17th-level cleric, targeted dispel, dispel check +17), spell effect (energy drain, 17th-level cleric, bestows 2d4 negative levels)\n•spell effect (implosion, 17th-level cleric, death, Fort DC 23 negates)" 
        iXP = "21,760 XP"
   
    #CR15
    elif sName == "Huge Unholy Greatsword Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "36"#
        iDD = "36"#
        iPrice = "258,850 gp"#
        sText = "•Atk +39 melee (4d6+19 plus 2d6 unholy, Huge +3 unholy greatsword)" 
        iXP = "N/A"#
     
    
    #CR16
    elif sName == "Prismatic Doom Trap":#
        sType2 = "Magical"#
        sTrigger = "Detection"#
        sReset = "no reset"#
        iSearch = "31"#
        iDD = "33"#
        iPrice = "N/A"#
        sText = "•Init +8\n•Heightened prismatic spray (Fortitude DC 22, Reflex DC 22, Will DC 22, CL 16th; see PH 264)\n•Duration 19 rounds\n•Destruction AC 26; hp 40; hardness 10 (each mirror)" 
        iXP = "N/A"#
    elif sName == "Slashing Deathblade Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "38"#
        iDD = "29"#
        iPrice = "245,600 gp"#
        sText = "•Atk +35/+30/+25/+20 melee (2d4+9 plus poison, +1 adamantine scythe)\n•poison (death blade, Fort DC 20 resists, 1d6 Con/2d6 Con, one dose per triggering);" 
        iXP = "N/A"#
    elif sName == "Rain of Arrows Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "manual"#
        iSearch = "38"#
        iDD = "24"#
        iPrice = "367,600 gp"#
        sText = "•Atk +34 ranged (1d8+4 plus poison, arrow)\n•poison (Colossal scorpion venom, Fort DC 33 resists, 1d10 Con/1d10 Con)\n•multiple targets (1d8 arrows per target in 10-ft.-by-10-ft. area)" 
        iXP = "N/A"
 
    #CR17
    elif sName == "Deadly Needle Trap":#
        sType2 = "mechanical"#
        sTrigger = "touch"#
        sReset = "manual"#
        iSearch = "39"#
        iDD = "32"#
        iPrice = "278,200 gp"#
        sText = "•Atk +48 melee (1 plus poison, needle); poison (pit fiend venom, Fort DC 27 resists, 1d6 Con/death)" 
        iXP = "N/A"#
    elif sName == "Intelligent Empowered Polar Ray Trap":#
        sType2 = "magic"#
        sTrigger = "intelligent"#
        sReset = "automatic"#
        iSearch = "36"#
        iDD = "36"#
        iPrice = "417,900 gp"#
        sText = "•Atk +11/+11/+11 ranged touch\n•spell effect (three empowered polar rays, 21st-level wizard, 21d6 points of cold damage (×1-1/2) each)\n•lesser powers (3/day: hold person [DC 14], zone of truth [DC 13]\n•1/day: major image [DC 14])\n•greater power (at will: detect thoughts [DC 13]); Int 17, Wis 17, Cha 10, Ego 13" #
        iXP = "33,432 XP"#

        
    #CR18
    elif sName == "Lava Curtains Trap":#
        sType2 = "Mechanical"#
        sTrigger = "Location"#
        sReset = "No reset"#
        iSearch = "33"#
        iDD = "51"#
        iPrice = "N/A"#
        sText = "•Init +18\n•Lava curtain (18d6 points of fire damage, DC 28 Reflex half); no save for anyone who crosses through a lava curtain willingly\n•Duration 21 rounds\n•Destruction AC 28; hp 45; hardness 10 (each slot)" 
        iXP = "N/A"#
  
    #CR20
    elif sName == "Dance of Death Trap":#
        sType2 = "Magical"#
        sTrigger = "Detection"#
        sReset = "Auto 23rnd"#
        iSearch = "35"#
        iDD = "34"#
        iPrice = "N/A"#
        sText = "•Init +10\n•Effect Otto’s irresistible dance (subject does nothing but dance for 1d4+1 rounds, no save, CL 17th; see PH 259); this spell affects anyone who contacts the skull in anyway; the dancing does not begin until the action is resolved, but additional attacks made from a full attack action are lost\n•Effect Energy drain (+20 ranged touch, 2d4 negative levels, DC Fortitude 23 removes one level after 24 hours, CL 17th); two rays per round at random targets\n•Duration 23 rounds\n•Destruction AC 40; hp 90; hardness 10 (skull)" 
        iXP = "N/A"#
 
    #CR22
    elif sName == "Devil’s Throne Trap":#
        sType2 = "Magical"#
        sTrigger = "Detection"#
        sReset = "No Reset"
        iSearch = "37"#
        iDD = "37"#
        iPrice = "N/A"#
        sText = "•Init +11\n•Effect Crushing limbs (Atk +20 melee, 10d6 points of bludgeoning damage + 6d6 points of fi re damage; half of the fire damage is profane and not reduced by resistance to fire based attacks); nine random targets per round; if fewer than nine targets are available, the trap attacks some targets with multiple limbs\n•Effect Mass hold monster (paralysis, DC 25 Will negates, CL 17th), targets all creatures in the room that are not devils\n•Duration 25 rounds\n•Destruction AC 32; hp 55; hardness 11 (each stone limb)\n•Destruction AC 43; hp 99; hardness 11 (throne)" 
        iXP = "N/A"#
 
    #CR25
    elif sName == "Glaive of Doom Trap":#
        sType2 = "mechanical"#
        sTrigger = "location"#
        sReset = "automatic"#
        iSearch = "55"#
        iDD = "50"
        iPrice = "1,102,808 gp"#
        sText = "•Atk +45/+40/+35/+30 melee (3d8+17 plus poison, Huge cold iron +1 glaive); poison (megapede poison, Fort DC 44 resists, 2d6 Con + 1d4 Dex/2d6 Con + 1d4 Dex; one dose per triggering)" 
        iXP = "N/A"
 

    #New Effect
    v6.set(iSearch)
    v7.set(iDD)
    v9.set(sType2)
    v11.set(sTrigger)
    v13.set(iPrice)
    v15.set(sReset)    
    v8.set(sName)  
    v17.set(iXP)  
    t1.delete(1.0,"end")
    t1.insert(1.0, sText)

#Help menu
def Help():
    ctypes.windll.user32.MessageBoxW(0, "Select the CR required, then use 'Generate'. All those trap are official from D&D manual", "How does it work?", 0)
def Help2():
    ctypes.windll.user32.MessageBoxW(0, "The tool include all trap in the following manual: DungeonMastersGuide $  Dungeonscape", "Which Manual are included?", 0)

#define buttons
l1=Label(window , text="Trap CR", width=9, state = DISABLED)
l1.grid(row=0,column=0)

b1=Button(window , text="Generate", width=9,  command=lambda: rollTrap())
b1.grid(row=0,column=2)

l2=Label(window , text="------------------------------------------", width=20, state = DISABLED)
l2.grid(row=1,column=0, columnspan=4)

c1list1 = ["CR1","CR2","CR3", "CR4", "CR5", "CR6", "CR7", "CR8", "CR9","CR10","CR11", "CR12","CR13", "CR14", "CR15", "CR16","CR17" "CR18", "CR20", "CR22", "CR25"]
c1=ttk.Combobox(window, values = c1list1, width=6)
c1.set("CR1")
c1.grid(row=0,column=1)

l3=Label(window , text="Search DC", width=9, state = DISABLED)
l3.grid(row=2,column=0)

l4=Label(window , text="Disable DC", width=9, state = DISABLED)
l4.grid(row=2,column=2)

v6=StringVar()
l6=Label(window, textvariable=v6 , text="1", width=9)
l6.grid(row=2,column=1)

v7=StringVar()
l7=Label(window, textvariable=v7 , text="2", width=9)
l7.grid(row=2,column=3)

l5=Label(window , text="Type", width=9, state = DISABLED)
l5.grid(row=3,column=0)

v9=StringVar()
l9=Label(window, textvariable=v9 , text="3", width=9)
l9.grid(row=3,column=1)

l10=Label(window , text="Trigger", width=9, state = DISABLED)
l10.grid(row=3,column=2)

v11=StringVar()
l11=Label(window, textvariable=v11 , text="4", width=9)
l11.grid(row=3,column=3)

l12=Label(window , text="Value", width=9, state = DISABLED)
l12.grid(row=4,column=2)

v13=StringVar()
l13=Label(window, textvariable=v13, text="5", width=9)
l13.grid(row=4,column=3)

l14=Label(window , text="Reset", width=9, state = DISABLED)
l14.grid(row=4,column=0)

v15=StringVar()
l15=Label(window, textvariable=v15 , text="6", width=9)
l15.grid(row=4,column=1)

l16=Label(window , text="Exp", width=9, state = DISABLED)
l16.grid(row=5,column=0)

v17=StringVar()
l17=Label(window, textvariable=v17 , text="6", width=9)
l17.grid(row=5,column=1)

v8=StringVar()
l8=Label(window, textvariable=v8, text="", relief=RIDGE, width=34, bg="#00ffff")
l8.grid(row=6,column=0, columnspan=4)

#Text
t1 = Text(window, width=34, height=16)
t1.grid(row=7,column=0, columnspan=4, rowspan=16)

window.mainloop()
