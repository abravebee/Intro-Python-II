from room import Room
from player import Player
from helpers import *

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("Jane", room["outside"])
# Write a loop that:
#
room["outside"].contains = ["stick", "rock", "flower"]
room["foyer"].contains = ["torch", "skull"]
room["overlook"].contains = ["cloth", "rabbit", "crossbow"]
room["narrow"].contains = ["armor", "sword", "book"]
room["treasure"].contains = ["goldpiece", "dust", "note"]
player.inventory = ["lint", "compass", "food"]

print(('\n\n   === Welcome to Adventure Game, {} ===\n'
       'Enter h for the Help Menu and available commands.').format(player.name))

while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

    print((
        '\n You are here: {}'
        '\n {}\n'
        ).format(
            player.current_room.name,
            player.current_room.desc,
        ))
    
# * Waits for user input and decides what to do.
    userin = input((
        "What would you like to do?\n"
        "> ")).lower().split(" ")
    
    print("\n DEV NOTE\n","userin: ", userin, "\n\n")

    if "help" in userin or userin == 'h':
        print((
        '\n === Help Menu ==='
        '\n To play Adventure Game, enter a command to explore or interact with your environment.'
        '\n n -> Go North, s -> Go South, e -> Go East, e-> Go West'
        '\n l -> Look around'
        '\n i -> Inventory check'
        '\n h -> Help Menu'
        '\n q -> Quit'
        '\n ================='
        ))
        continue
    
    if len(userin) == 1:
        command = userin[0]
        if userin[0] == 'l':
            player.current_room.print_items()
            continue
    
        if userin[0] == 'i':
            player.print_items()
            continue

        if userin[0] == 'n':
            try:
                player.current_room = player.current_room.n_to
                print("You went north.")
            except:
                print("You can't go that way.")
            continue
        
        if userin[0] == 's':
            try:
                player.current_room = player.current_room.s_to
                print("You went south.")
            except:
                print("You can't go that way.")
            continue

        if userin[0] == 'e':
            try:
                player.current_room = player.current_room.e_to
                print("You went east.")
            except:
                print("You can't go that way.")
            continue

        if userin[0] == 'w':
            try:
                player.current_room = player.current_room.w_to
                print("You went west.")
            except:
                print("You can't go that way.")
            continue

        if userin[0] == 'q':
            quit_check = input((
                '\nReally quit?  y/n'
                '\n> '
            )).lower()
            if quit_check == 'y':
                print("See ya!")
                break
            elif quit_check == 'n':
                print("Returning to game...")
                continue

        else:
            print("Invalid command.\nPlease try a different one, or enter 'h' for the Help Menu")

    elif len(userin) == 2:
        

        else:
            print("Invalid command.\n Please try a different one, or enter 'h' for the Help Menu")
        

    else:
        print("Invalid command.\n Please try a different one, or enter 'h' for the Help Menu")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.