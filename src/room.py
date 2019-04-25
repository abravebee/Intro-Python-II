# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        room_string = f"\n\n\n {self.name}\n"
        room_string += f"      {self.description}\n\n"
        room_string += f" You can travel:  \n"
        room_string += f" You can see: \n"
        return room_string

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def print_items(self):
        if len(self.contains) == 0:
            print(" You look around, but there are no items here!")
        else:
            print(" You look around and see the following items: ")
            for x in self.items:
                print(('  {}').format(x.name))
