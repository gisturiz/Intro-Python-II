from room import Room

class Item(Room):
    def __init__(self, item_name, item_description, name):
        super().__init__(name)
        # Name, description
        self.item_name = item_name
        self.item_description = item_description
