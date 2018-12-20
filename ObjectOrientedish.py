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
globalActions['n'] = move
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
firstRoom = Room('First Room', 'Full of beans')
secondRoom = Room('Second Room', 'Empty of beans')
theBoy = Player(firstRoom)

#Link first room's North to second room
firstRoom.addOrUpdateLink('n', secondRoom)

#Add room-specific action to second room
def fillWithBeans(room, player, command):
    room.description = 'Full of beans'
    print('You fill ' + room.name + ' with beans')
    player.action('look', True)
secondRoom.actions['fill with beans'] = fillWithBeans


#Perform the stuff. In the real game this would be player input, not written here
theBoy.action('look around')
theBoy.action('n')
theBoy.action('fill with beans')
theBoy.action('squeeze buttocks')
