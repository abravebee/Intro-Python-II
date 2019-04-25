# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)

    def print_items(self):
        if len(self.inventory) == 0:
            print(" Your inventory is empty.")
        else:
            print(" Your Inventory: ")
            for x in self.inventory:
                print(('   {}').format(x.name))
