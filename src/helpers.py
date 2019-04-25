import sys

def quit_game():
    quit_check = None
    while quit_check not in ('y', 'n'):
        quit_check = input(f' Really quit?'
                            f'\n> Y/N: ').lower()
        if quit_check == 'y':
            print("\n See ya!")
            sys.exit()
        if quit_check == 'n':
            print("\n Returning to game...")
            continue

def invalid():
    print('\n Invalid command. '
            '\n H -> Help. Q -> Quit.')