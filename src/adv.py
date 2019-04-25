from room import Room
from player import Player
from dictionaries import *
import sys

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("Jane", room["outside"])
player.inventory = [item["lint"], item["compass"]]
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
        print((
        '\n === Help Menu ==='
        '\n To play Adventure Game, enter a command to explore or interact with your environment.'
        '\n go n -> Go North, go s -> Go South, go e -> Go East, go w -> Go West'
        '\n i -> Inventory'
        '\n h -> Help Menu'
        '\n q -> Quit'
        '\n ================='
        ))
        continue

    elif len(userin) == 1:
        if verb in ('go', 'get', 'take', 'drop'):
            print(f'{verb} what? Please be more specific.')
        elif verb in ('q', 'quit'):
            quit_check = None
            while quit_check not in ('y', 'n'):
                quit_check = input(f' Really quit?'
                                f'\n> Y/N: ').lower()
                if quit_check == 'y':
                    print(" See ya!")
                    sys.exit()
                if quit_check == 'n':
                    print(" Returning to game...")
                    continue
            
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