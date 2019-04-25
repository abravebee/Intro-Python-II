# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.contains = []
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc

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
