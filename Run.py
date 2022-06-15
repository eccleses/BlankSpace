import random
import time
import numpy
#------------------------------------------------------------------------------------------------------
""" This program says hello to the user when prompted with the hello() command"""
def Hello():
    print("Hello!")
#------------------------------------------------------------------------------------------------------
""" This program says goodbye to the user when prompted with the goodbye() command"""
def Goodbye():
    print("Goodbye!")
#------------------------------------------------------------------------------------------------------
def About():
    print('BlankSpace Library About Page')
    print('Use the BlankSpace.Run.Hello() function to say hello')
    print('Use the BlankSpace.Run.Goodbye() function to say goodbye')
    print('Use the BlankSpace.Run.Filler() function with the the first number in the brackets representing facts shown and the second')
    print('number to represent category, 0 for random, 1 for Hardware, 2 for Things, 3 for (Outdated) Pop Culture')
#------------------------------------------------------------------------------------------------------
#summons the Matrix
x = 1#used for forever loop
def infiniteMatrix():
    while x != 42:
        iMatrixBoolean = random.randint(0,1)
        print(iMatrixBoolean, end ='')
#------------------------------------------------------------------------------------------------------
def Matrix(mLoops):
    for x in range (mLoops):
        matrixBoolean = random.randint(0,1)
        print(matrixBoolean, end ='')

#------------------------------------------------------------------------------------------------------
"""
This program prints random silly messages in case you need facts for a loading screen, stats menu etc.
Originally created by Github User VeryCoolNameThatIsDefinitelyNotAPlaceholder
"""
"""
HOW TO USE
1.type filler()
2.in the brackets, first type the number of facts you want to read/seconds the program will run for/loops of the code from line 25 and below
3.Type a comma
4.Type the mode you wish to run. 0 for random, 1 for PC parts, 2 for Things, 3 for Pop Culture(outdated)
"""

#contains all categories for later displaying
partVer = ['degreasifying ', 'vicariously sniffing ', 'having an intense staring contest with ','RGX+Testing ', 'Removing hot dog grease from ','Hitting head against ']
part = ['RAM', 'CPU', 'VRM', 'Heatsink', 'PSU', 'GPU', 'USB Header', 'RJ45 port', 'Fans', 'GPIO','Ethernet', 'WiFi Dongle','Keyboard', 'Mouse']
thingVer = ['demystifying ', 'revealingMagicTricksTo ', 'having An Intense Staring Contest With ', 'rapBattlingWith ', 'improving ', 'preventingDeathFrom ', 'imitating ','reprogramming','compiling']
thing = ['AI ', 'CGI Chipmunks',  ' Horses', ' Belgian Insurance', ' Caravan Carpet','Holly','Kryten 2X4B-523P']
personVer = ['conversing with','having An Intense Staring Contest With','rap Battling With','demystifying','revealing Magic Tricks To']
person = [' Queenie',' Mr. Bean',' Dave Lister',' Arthur Dent',' Cat',' Arnold Rimmer',' Ford Prefect',' Zaphod',' Slartibartfast',' Monty Python']
def Filler(loops,mode):
    for x in range(loops):
        if mode == 0:
            category = random.randint(0,2)
            if category == 0:
                print(random.choice(partVer), end ='')#end = bit means we do not start a new line
                print(random.choice(part))
                time.sleep(1)
            elif category == 1:
                print(random.choice(thingVer), end ='')
                print(random.choice(thing))
                time.sleep(1)
            elif category == 2:
                print(random.choice(personVer), end ='')
                print(random.choice(person))
                time.sleep(1)
        if mode == 1:
            print(random.choice(partVer), end ='')#end = bit means we do not start a new line
            print(random.choice(part))
            time.sleep(1)
        elif mode == 2:
            print(random.choice(thingVer), end ='')
            print(random.choice(thing))
            time.sleep(1)
        elif mode == 3:
            print(random.choice(personVer), end ='')
            print(random.choice(person))
            time.sleep(1)