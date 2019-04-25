# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.contains = []
    
    def __str__(self):
        room_string = f"\n\n\n{self.name}\n"
        room_string += f"      {self.desc}\n"
        return room_string

    def add_item(self, item):
        self.contains.append(item)
    
    def remove_item(self, item):
        self.contains.remove(item)
    
    def print_items(self):
        if len(self.contains) == 0:
            print(" You look around, but there are no items here!")
        else:
            print(" You look around and see the following items: ")
            for x in self.contains:
                print(('  {}').format(x.name))
