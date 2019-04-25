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
    userin = input(("> ")).lower().split(" ")

    verb = userin[0]

    if "help" in userin or verb == 'h':
        helpmenu()
        continue

    elif len(userin) == 1:
        if verb in ('go', 'get', 'take', 'drop'):
            print(f' \n{verb} ...? Be more specific.')
        elif verb in ('q', 'quit'):
            quit_game()
        elif verb in ('i', 'inventory'):
            print("\n Inventory: ")
            print(" ", player.print_items())         
        else:
            invalid()

    elif len(userin) == 2:
        object = userin[1]
        if verb in ('get', 'take'):
            try:
                player.add_item(item[object])
                player.current_room.remove_item(item[object])
                item[object].on_take()
            except:
                print(f'\n There is no {object} to be found.')

        elif verb == 'drop':
            try:
                player.remove_item(item[object])
                player.current_room.add_item(item[object])
                item[object].on_drop()
            except:
                print(f'\n You do not have a {object} to drop.')

        elif verb == 'go':
            direction = userin[1]
            if direction in directions:
                player.travel(direction)
            else:
                print('\n You want to go where?')

        else:
            invalid()
    else:
        invalid()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.