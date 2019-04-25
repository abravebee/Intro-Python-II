import sys

def quit_game():
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