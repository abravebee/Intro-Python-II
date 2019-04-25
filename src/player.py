# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if len(self.items) == 0:
            return '\n\n Your inventory is empty.'
        else:
            return ', '.join([str(i) for i in self.items])

    def travel(self, direction):
        next_room = self.current_room.next_room(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print('\n There is nothing in that direction.')