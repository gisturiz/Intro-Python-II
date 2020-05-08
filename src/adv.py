from item import Item
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

# Items

item = {
    'sword': Item("Sword", "Long Sword"),
    'knife': Item("Knife", "Dagger"),
    'hat': Item("Hat", "Top Hat")
}

room['outside'].items.append(item['sword'])
room['outside'].items.append(item['knife'])
room['foyer'].items.append(item['hat'])




#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)

directions = ["n", "s", "e", "w"]
actions = ["get", "drop"]
# Create basic REPL loop
while True:
    # Read command
    cmd = input("~~> ")
    # Check if it's n/s/e/w/q
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
    elif cmd == "i":
        player.get_items()
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        exit()
    elif len(cmd) > 1:
        item_cmd = cmd.split()
        if item_cmd[0] == 'get':
            player.add_item(item[item_cmd[1]])
            player.current_room.pick_item(item[item_cmd[1]])
            print(f"You picked up {item_cmd[1]}")
        elif item_cmd[0] == 'drop':
            player.drop_item(item[item_cmd[1]])
            player.current_room.drop_item(item[item_cmd[1]])
            print(f"You dropped up {item_cmd[1]}")
    else:
        print("I did not recognize that command")
