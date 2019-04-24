from room import Room
from player import Player

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


while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

    print((
        '\n You are here: {}'
        '\n {}\n'
        ).format(
            player.current_room.name,
            player.current_room.desc
        ))
# * Waits for user input and decides what to do.
    userin = input((
        "What would you like to do?\n"
        "> ")).lower()
    
    if "help" in userin or userin == 'h':
        print((
        '\nHELP MENU'
        '\n N > Go North, S > Go South, E > Go East, W > Go West'
        '\n H > Help Menu'
        '\n Q > Quit'
        ))
        continue

    if "north" in userin or userin == 'n':
        try:
            player.current_room = player.current_room.n_to
            print("You went north.")
        except:
            print("You can't go that way.")
        continue
    
    if "south" in userin or userin == 's':
        try:
            player.current_room = player.current_room.s_to
            print("You went south.")
        except:
            print("You can't go that way.")
        continue

    if "east" in userin or userin == 'e':
        try:
            player.current_room = player.current_room.e_to
            print("You went east.")
        except:
            print("You can't go that way.")
        continue

    if "west" in userin or userin == 'w':
        try:
            player.current_room = player.current_room.w_to
            print("You went west.")
        except:
            print("You can't go that way.")
        continue

    if "quit" in userin or userin == 'q':
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
        print("userin", userin)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.