# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")

    def add_item(self, item_name):
       self.inventory.append(item_name)

    def drop_item(self, item_name):
        if item_name not in self.inventory:
            print("There's no such item")
        else:
            self.inventory.remove(item_name)
    
    def get_items(self):
        if self.inventory == []:
            print("There are no items in your inventory")
        else:
            for item in self.inventory:
                print(f"{item}")
