#Utter disgust
#Delete this

from random import randint
import time, os, sys
#Default inventory.
f = open("inventory.txt","r")
#Important stuff/preset stuff
system=os.name
secret = False
clear = ""
inventory = f.read().split(',')
health = 100
progress = False
word = ["traveller","you common dandy", "rumbleyguts", "stretchyskin"]

#System Function stuff
#Check if system is windows or linux (fuck you OSX)
def cistest(system, clear):
	if "nt" in system:
		clear="\"cls\""
	if "pos" in system:
		clear="\"clear\""
	if "mac" in system:
		clear="No"
	return clear
#Function to assign clear screen command based on os
clear = cistest(system,clear)
if clear == "no":
	print "Your kind is not welcome here"
	time.sleep(500000000000000000)
	exit()	

#Function to clear screen based on OS
def clearscreen(clear):
	os.system(clear)
clearscreen(clear)
#Function to print text slowly for DRAMA (Totally not stolen)
def print_slowly(text,t):
    for c in text:
        print c,
        sys.stdout.flush()
        time.sleep(t)

#Player stuff
#player class, not stolen at all
class Room:
    def __init__(self, name, description, links): 
	   self.name = name
	   self.description = description
	   self.links = links
world = {}
world['area1'] = Room(
    "area1", 
    "You open your eyes. You're standing in the south of a small circular courtyard paved with bricks. Vines grow between many of these bricks. Surrounding the edges of the courtyard are a ring of towering, identical stone statues. The statues stand so close together that you cannot see through any of the small spaces between them. Warm light filters through these small gaps. In the center of the courtyard is a small raised pool. What will you do?", 
    {'n': 'pool'}
)
world['pool'] = Room(
    'pool',
    'You are standing by a small raised pool',
    {'s': 'area1'}
)
class Player:
    def __init__(self, name, health, room_name):
        self.name = name
        self.room = world[room_name]
    def move(self, direction):
		if direction not in self.room.links:
			print("Cannot move in that direction!")
			return
		new_room_name = self.room.links[direction]
		self.room = world[new_room_name]

#All player actions to go in hurr
def action(a,player):
	if a.lower() in {'n', 'e', 's', 'w'}:
		print_slowly("moving...",0.1)
		player.move(command)
		clearscreen(clear)
		print(player.room.description)
	elif 'look' in a.lower() and 'area1' in player.room.name:
		print"I just told you, you're in some sort of mysterious courtyard, vines and such, it's all very mysterious"
	elif a.lower() == 'look':
		print(player.room.description)
		#If you want to show the player current directions they can move(N,S,E,W)
		#print('current exits are: ' + str(player.room.links.keys()))		
	elif "scream" in a.lower():
		print "You scream for a long time. You scream until your throat is horse. Your throat is horse. Neigh whinny"    
	#Might throw error on terminal
	elif a.lower() in "open inventory":
		clearscreen(clear)
		print "You open your inventory"
		print "Contained inside is:"
		for i in inventory:
			print(i + " ") 	
	#If game don't know what doing
	else:
		print("I'm sorry, I don't understand " + "'"+ a +"'")

clearscreen(clear)
#Set player name
name = raw_input("What is your name " + word[randint(0,len(word))-1] + "? " +"\n>")
#Create player object
p = Player(name,100,"area1")

#intro
clearscreen(clear)
print 'Everything is spinning',
print_slowly('.....',1)
clearscreen(clear)
print 'Faster now',
print_slowly('.....',0.5)
clearscreen(clear)
print 'EVEN FASTER',
print_slowly('..........................',0.1)
clearscreen(clear)
print 'HNNNNNNNNNNNNNNNNG',
print_slowly('........................',0.05)
clearscreen(clear)
print 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH FUUUUUU',
print_slowly('....................................................',0.01)
clearscreen(clear)
#Area 1 room 
print(p.room.description)
#Main running
while True:
	command = raw_input('>>').lower()
	action(command,p) 


