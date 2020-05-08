# Implement a class to hold room information. This should have name and
class Room:
    def __init__(self, name, description):
        # Name, description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        display_string += f"\nItems inside this room: {self.get_items()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_items(self):
        if self.items == []:
            return "No items in this room"
        else:
            return self.items
            
    def pick_item(self, item):
        if item not in self.items:
            print("There's no such item")
        else:
            self.items.remove(item)

    def drop_item(self, item):
        self.items.append(item)

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"
