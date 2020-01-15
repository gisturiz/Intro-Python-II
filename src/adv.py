import textwrap

from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Gustavo', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    current_room = player.room
    print('\nYou are currently: ' + str(current_room))

    my_wrap = textwrap.TextWrapper(width = 40)
    room_description = textwrap.shorten(text = player.room.description, width=150)
    print('\n' + my_wrap.fill(text = room_description))

    print('\nWhere do you want to go? Press `N` for North, `E` for East, `S` for South, `W` for West \nOr press q to quit')
    ans = input()

    if ans == 'n' or ans == 'N':
        if not hasattr(current_room, 'n_to'):
            print("Sorry you cannot take that path, try again.")
        else:
            player.room = player.room.n_to
    elif ans == 'e' or ans == 'E': 
        if not hasattr(current_room, 'e_to'):
            print("Sorry you cannot take that path, try again.")  
        else:
            player.room = player.room.e_to
    elif ans == 's' or ans == 'S':
        if not hasattr(current_room, 's_to'):
            print("Sorry you cannot take that path, try again.") 
        else: 
            player.room = player.room.s_to
    elif ans == 'w' or ans == 'W':
        if not hasattr(current_room, 'w_to'):
           print("Sorry you cannot take that path, try again.")
        else:
            player.room = player.room.w_to
    elif ans == 'q' or ans == 'Q':
        break
print("\nThanks for playing!")
