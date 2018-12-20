#Dictionary of global actions that can be accessed anywhere
globalActions = {}

def lookRoom(room, player, command):
    print("You look around the " + room.name)
    print(room.description)

def move(room, player, command):
    nextRoom = room.links.get(command)
    if nextRoom is not None:
        player.currentRoom = nextRoom
        player.action('look', True)

def confused(room, player, command):
    print("u wot m8???")
    
globalActions['lookRoom'] = lookRoom
globalActions['n'] = globalActions['e'] = globalActions['s'] = globalActions['w'] = move
globalActions[None] = confused

#Translator to allow multiple player commands to access the same action,
#Also contains the failure case where no action is available
def translateActions(command):
    if command in ['look','look room','look around']:
        return 'lookRoom'
    elif command in ['n', 's', 'e', 'w']:
        return command
    else:
        return None

#Room class
class Room:
    #Instantiate and grab global actions
    def __init__(self, name, description, links = {}):
        self.name = name
        self.description = description
        self.links = links
        self.actions = globalActions

    #If actions are a perfect match, execute
    #Else look in the translator and execute
    def action(self, player, command, silent):
        if not silent:
            print("> " + command)
        if command in self.actions:
            self.actions[command](self, player, command)
        else:
            self.actions[translateActions(command)](self, player, command)

    #Allows rooms to be added after instantiation
    def addOrUpdateLink(self, key, newLink):
        self.links[key] = newLink

#Player class
#Only contains a position and a pass-through to the current room action
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom

    def action(self, command, silent = False):
        self.currentRoom.action(self, command, silent)

#Instantiate two rooms and the player in the first room
world = {}
world['area1'] = Room(
    "area1", 
    "You open your eyes. You're standing in the south of a small circular courtyard paved with bricks. Vines grow between many of these bricks. Surrounding the edges of the courtyard are a ring of towering, identical stone statues. The statues stand so close together that you cannot see through any of the small spaces between them. Warm light filters through these small gaps. In the center of the courtyard to the north is a small raised pool. What will you do?", 
    {'n': 'pool'}
)
world['pool'] = Room(
    'pool',
    'You are standing by a small raised pool',
    {'s': 'area1'}
)
world['statues'] = Room(
    'statues',
    'You are facing',
    {'s': 'area1'}
)
world['black'] = Room(
	'black',
	"Everything is black, like everything everywhere. Lots of smells though, and some feelings too",
	{'s': 'black','n':'black', 'e': 'black', 'w': 'black'}
)	
theBoy = Player(world['area1'])


#Perform the stuff. In the real game this would be player input, not written here
