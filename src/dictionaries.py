from room import Room
from item import Item

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

# Declare all items
item = {
    "stick": Item("stick", """It's just an ordinary stick. Probably not going to do you much good."""),
    "rock": Item("rock", """Good weight and fits just right in your hand. Maybe you can chuck it at someone's head!"""),
    "flower": Item("flower", """A wildflower that grows locally. It smells nice."""),
    "torch": Item("torch", """A wall torch that was mysteriously still lit in this supposedly abandoned cave."""),
    "skull": Item("skull", """Alas, poor Yorick! I didn't know him at all but he seemed real decent."""),
    "cloth": Item("cloth", """A torn bit of cloth from the edge of the cliff, probably off some poor bloke who got Fus Ro Dah'd into oblivion."""),
    "rabbit": Item("rabbit", """A friend! He doesn't seem to mind being picked up."""),
    "crossbow": Item("crossbow", """People really shouldn't leave weapons just lying around like this...but maybe someone left some arrows, too?"""),
    "arrow": Item("arrow", """A single arrow, sharpened to a deadly point. Not bad alone, but if only you had something to launch it with..."""),
    "goldpiece": Item("goldpiece", """A shiny coin made of gold."""),
    "dust": Item("dust", """It seems like ordinary dust, but then it's got a slightly odd shimmer to it..."""),
    "note": Item("note", """Someone has left a note behind. It's written in some kind of moon-man language you can't parse."""),
    "lint": Item("lint", """That one tiny clump of lint that gets stuck to that one loose string in your worn pockets."""),
    "compass": Item("compass", """You're the kind of cat who travels by the cardinal directions."""),
}


# Add items to rooms
room["outside"].items = [item["stick"], item["rock"], item["flower"]]
room["foyer"].items = [item["torch"], item["skull"]]
room["overlook"].items = [item["cloth"], item["rabbit"], item["crossbow"]]
room["narrow"].items = [item["arrow"]]
room["treasure"].items = [item["goldpiece"], item["dust"], item["note"]]