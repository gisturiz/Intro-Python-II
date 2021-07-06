from room import Room


class Item():
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
    
    def onTake(self):
        print(f"\nYou have picked up the {self.item_name}")

    def onDrop(self):
        print(f"\nYou dropped the {self.item_name}")

    def __repr__(self):
       return self.item_name
