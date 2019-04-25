# * Create a file called `item.py` and add an `Item` class in there.
#   * This will be the _base class_ for specialized item types to be declared
#     later.
#   * The item should have `name` and `description` attributes.
#      * Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        item_string = f"{self.name}"
        return item_string
    
    def on_take(self):
        print(("You picked up the {}.").format(self.name))
        print(self.desc)
    
    def on_drop(self):
        print(("You dropped your {} like a common litterbug.").format(self.name))