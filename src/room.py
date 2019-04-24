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