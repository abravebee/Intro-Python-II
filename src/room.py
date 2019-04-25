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
        room_string += f" You can travel: {self.print_directions()} \n"
        room_string += f" You can see: {self.print_items()}\n\n"
        return room_string 

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def print_items(self):
        if self.items == None:
            return "nothing"
        else:
            return ', '.join([str(i) for i in self.items])
    
    def print_directions(self):
        directions = []
        if self.n_to is not None:
            directions.append('N')
        if self.s_to is not None:
            directions.append('S')
        if self.e_to is not None:
            directions.append('E')
        if self.w_to is not None:
            directions.append('W')
        if len(directions) < 1:
            return "You're trapped!"
        else:
            return ', '.join([str(d) for d in directions])
