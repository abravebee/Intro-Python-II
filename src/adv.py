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
player = Player("Jane", "outside")
rm_current = room[player.current_room]
rm_name = room[player.current_room].name
rm_desc = room[player.current_room].desc
# Write a loop that:
#
# * Prints the current room name
print(rm_name)
# * Prints the current description (the textwrap module might be useful here).
print(rm_desc)

# * Waits for user input and decides what to do.
#
user_in = input(
    ("What would you like to do? \n" "Enter a cardinal direction or Q to quit.\n")
)
# If the user enters a cardinal direction, attempt to move to the room there.

while not user_in == "Q" and not user_in == "q":
    if "north" in user_in or "North" in user_in:
        try:
            print("You go North")
            player.current_room = rm_current.n_to.name
            print(player.current_room)
        except:
            print("You can't go that way.")
    elif "south" in user_in or "South" in user_in:
        try:
            print("You go South")

        except:
            print("You can't go that way.")
    elif "east" in user_in or "East" in user_in:
        try:
            print("You go East")

        except:
            print("You can't go that way.")
    elif "west" in user_in or "West" in user_in:
        try:
            print("You go West")

        except:
            print("You can't go that way.")
    else:
        print("I don't understand.")
    #print(room[player.current_room].name)
    user_in = input(
        ("What would you like to do? \n" "Enter a cardinal direction or Q to quit.\n")
    )

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
