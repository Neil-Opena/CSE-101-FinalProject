#Neil Opena 110878452

#Final Programming Project
#Part 2: Lindenmayer Fractais (L-systems)

from turtle import *

bob = Turtle()
screen = bob.getscreen()

productiondict = {}

pattern = screen.textinput("Enter Seed String", "Enter the seed string: ")

#This is for the regular project
"""numrules = screen.numinput("Enter Number of Rules", "Enter the amount of production rules: ")

for rule in range(int(numrules)):
    targetchar = screen.textinput("Enter Target Character", "Enter the target character: ")
    replacement = screen.textinput("Enter Replacement", "Enter the replacement: ")
    productiondict[targetchar] = replacement

if numrules > 0:
    numrecursion = screen.numinput("Enter Recursion Depth", "Enter the recursion depth: ")
else:
    numrecursion = 0"""


#EXTRA CREDIT:
inputFile = open('test.txt')
text = inputFile.readlines()
    
keys = text[::2]
values = text[1::2]
    
for key in keys:
    productiondict[key] = values[keys.index(key)]
    
inputFile.close()
    
numrecursion = screen.numinput("Enter Recursion Depth", "Enter the recursion depth: ")

dist = screen.numinput("Enter Distance", "Enter the fixed distance: ")
ang = screen.numinput("Enter Angle", "Enter the fixed angle: ")


            
def deriveLSystem(seed, productions, depth):
    global bob 
    if depth <= 0:
        return seed
    else:
        newPattern = ''
        for char in seed:
            #
            char = (char + '\n')
            if char in productions:
                newPattern = (newPattern + productions[char])
            else:
                newPattern = (newPattern + char)
        return deriveLSystem(newPattern, productions, depth - 1)

def drawLSystem(string, angle, distance):
    global bob
    bob.pendown()
    speed(0)
    for command in string:
        if command == 'F':
            bob.forward(distance)
        elif command == '-':
            bob.left(angle)
        elif command == '+':
            bob.right(angle)
        else:
            print ('null')

                
  
pattern = deriveLSystem(pattern, productiondict, numrecursion)
drawLSystem(pattern, ang, dist)




