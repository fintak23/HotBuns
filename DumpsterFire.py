#Utter disgust
#Delete this

from random import randint
import time, os, sys
#Default inventory.
f = open("inventory.txt","r")
#Important stuff/preset stuff
system=os.name
secret = False
command = ""
inventory = f.read().split(',')
action = ""
health = 100
progress = False
word = ["traveller","you common dandy", "rumbleyguts", "stretchyskin"]
#System Function stuff
#Check if system is windows or linux (fuck you OSX)
def cistest(system, command):
	if "nt" in system:
		command="\"cls\""
	if "pos" in system:
		command="\"clear\""
	if "mac" in system:
		command="No"
	return command
#Function to clear screen based on OS
def clearscreen(command):
	print "Cleared screen"
	os.system(command)
#Function to print text slowly for DRAMA (Totally not stolen)
def print_slowly(text,t):
    for c in text:
        print c,
        sys.stdout.flush()
        time.sleep(t)
#Function to assign clear screen command based on os
command = cistest(system,command)
if command == "no":
	print "Your kind is not welcome here"
	time.sleep(500000000000000000)
	exit()	
clearscreen(command)

#Player stuff
def plAction(action, area):
 action = raw_input("> ")
 if  "north" in action.lower():
 	print "You go north, fgdfg" 
 elif "east" in action.lower():
 	print "You go east, fgdfg" 
 elif "west" in action.lower():
 	print "You go west, fgdfg" 
 elif "south" in action.lower():
 	print "You go south, fgdfg"
 elif "scream" in action.lower():
 	print "You scream for a long time. You scream until your throat is horse. Your throat is horse. Neigh whinny"
 elif area == 1 and "look" in action.lower():
 	print "I just told you, you're in some sort of mysterious courtyard, vines and such, it's all very mysterious"
 elif action.lower() in "open inventory":
 	clearscreen(command)
 	print "You open your inventory"
 	print "Contained inside is:"
 	for i in inventory:
 		print(i + " ") 	
 #If game has no idea what the happen
 else:
 	print ("I'm sorry, I don't understand " +action)
 return action 

name = raw_input("What is your name " + word[randint(0,len(word))-1] + "? " +"\n>")

#Area 1
clearscreen(command)
print 'Everything is spinning',
print_slowly('.....',1)
clearscreen(command)
print 'Faster now',
print_slowly('.....',0.5)
clearscreen(command)
print 'EVEN FASTER',
print_slowly('..........................',0.1)
clearscreen(command)
print 'HNNNNNNNNNNNNNNNNG',
print_slowly('........................',0.05)
clearscreen(command)
print 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH FUUUUUU',
print_slowly('....................................................',0.01)
clearscreen(command)
print "You open your eyes. You're standing in the south of a small circular courtyard paved with bricks. Vines grow between many of these bricks. Surrounding the edges of the courtyard are a ring of towering, identical stone statues. The statues stand so close together that you cannot see through any of the small spaces between them. Warm light filters through these small gaps. In the center of the courtyard is a small raised pool. What will you do?"
while progress == False :
	plAction(action, 1)



