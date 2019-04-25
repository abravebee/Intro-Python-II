from room import Room
from player import Player
from dictionaries import *

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("Jane", room["outside"])
player.inventory = [item["lint"], item["compass"]]
# Write a loop that:
print(('\n\n\n--->>> ADVENTURE GAME --->>>'
        f'\n\nWelcome, {player.name}'
        '\nEnter h for the Help Menu and available commands.'))

while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

    print(f'{player.current_room}')
    
# * Waits for user input and decides what to do.
    userin = input((
        "What would you like to do?\n"
        "> ")).lower().split(" ")

    verb = userin[0]
    
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
        if verb == 'l':
            player.current_room.print_items()
            continue
    
        if verb == 'i':
            player.print_items()
            continue

        if verb == 'n':
            try:
                player.current_room = player.current_room.n_to
                print("You went north.")
            except:
                print("You can't go that way.")
            continue
        
        if verb == 's':
            try:
                player.current_room = player.current_room.s_to
                print("You went south.")
            except:
                print("You can't go that way.")
            continue

        if verb == 'e':
            try:
                player.current_room = player.current_room.e_to
                print("You went east.")
            except:
                print("You can't go that way.")
            continue

        if verb == 'w':
            try:
                player.current_room = player.current_room.w_to
                print("You went west.")
            except:
                print("You can't go that way.")
            continue

        if verb == 'q':
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