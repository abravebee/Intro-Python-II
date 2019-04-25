from room import Room
from player import Player
from dictionaries import *
from menus import *
from helpers import *

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("Jane", room["outside"])
player.items = [item["lint"], item["compass"]]
directions = ['n', 's', 'e', 'w']
# Write a loop that:
print(('\n\n\n--->>> ADVENTURE GAME --->>>'
        f'\n\n Welcome, {player.name}'
        '\n Enter H for the Help Menu and available commands.'))

while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

    print(f'{player.current_room}')
    
# * Waits for user input and decides what to do.
    userin = input((
        " What would you like to do?\n"
        "> ")).lower().split(" ")

    verb = userin[0]

    if "help" in userin or userin == 'h':
        helpmenu()
        continue

    elif len(userin) == 1:
        if verb in ('go', 'get', 'take', 'drop'):
            print(f' \n{verb} ...? Be more specific.')
        elif verb in ('q', 'quit'):
            quit_game()
        elif verb in ('i', 'inventory'):
            print(" Inventory: ")
            print(player.print_items())         
        else:
            print('Invalid command.')

        # if verb in directions:

    elif len(userin) == 2:
        object = userin[1]
        if verb == 'get' or verb == 'take':
            try:
                player.add_item(item[object])
                player.current_room.remove_item(item[object])
                item[object].on_take()
            except:
                print(("There is no {} to be found.").format(object))

        elif verb == 'drop':
            try:
                player.remove_item(item[object])
                player.current_room.add_item(item[object])
                item[object].on_drop()
            except:
                print(("You don't have a {} to drop.").format(object))
        
        else:
            print("Invalid command.\nPlease try a different one, or enter 'h' for the Help Menu")
    else:
        print("Invalid command.\nPlease try a different one, or enter 'h' for the Help Menu")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.