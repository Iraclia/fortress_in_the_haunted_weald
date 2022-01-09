#This document sets up all necessary variables and functions to run the text adventure game

class Adventurer:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.visited = []

    # description used at the end of each text block to remind user of inventory items available
    def __repr__(self):
        return "The adventurer {0} currently has: {1} in their inventory.".format(self.name, self.items)

    # inventory list for items collected - items added and removed
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # list of rooms visited updates text upon returning for a shorter version
    def room_visited(self, room):
        self.visited.append(room)


def rule_checker():
    # prompt user input to display rules or not
    rule_check = input("Would you like to read the rules? (Y/N) \n").lower().strip()
    if rule_check in positives:
        return print("\nThis is a text adventure game. As the scenes are described, you will be prompted to make choices, find items, and traverse through the rooms in search of a treasure. Type the number of your response when promted and hit enter to continue to the next step. If you would like to exit the game, type 'Exit' at any point. Have fun! \n\n*** Disclaimer: Lots of reading involved. :) ***\n")
    elif rule_check in negatives:
        return print(" ")
    else:
        print("\nSorry, that is not a valid response. Please choose Y or N to continue.")
        return rule_checker()

# establishes variations of yes/no that will be accepted
positives = ["y", "yes", "yeah", "sure", "ok", "okay", "yep", "yah"]
negatives = ["n", "no", "nah", "nope", "nu"]

# establishing words to exit the game at any point
exit_words = ['exit', 'stop', 'leave', 'quit']

# Function to check/add player visit to a room and to print the room description, player inventory and choices for the room -- maybe some of the issues with unique set up could be fixed by breaking this into 2 functions? one for first visit, one for return?
def room_basic(room_name, room_return, room_choices, return_choices=None):
    if return_choices == None:
        return_choices = room_choices
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name)
        print(player.__repr__())
        room_choice = input(room_choices).strip()
        return room_choice
    else:
        print(room_return)
        print(player.__repr__())
        room_choice = input(return_choices).strip()
        return room_choice

# Function for just the return to a room to print the room description, player inventory and choices for the room
def room_return(room_name, room_choices):
    print(room_name)
    print(player.__repr__())
    room_choice = input(room_choices).strip()
    return room_choice

# Function to check/add player visit to a room and to print the room description including the player name, player inventory and choices for the room -- Perhaps see if this can be combined with the basic room function? Options for including a name based on a T/F name parameter with a default F?
def room_with_player_name(room_name, room_return, room_choices, return_choices=None):
    if return_choices == None:
        return_choices = room_choices
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name.format(player.name))
        print(player.__repr__())
        room_choice = input(room_choices).strip()
        return room_choice
    else:
        print(room_return.format(player.name))
        print(player.__repr__())
        room_choice = input(return_choices).strip()
        return room_choice

# Function for just the return to a room with a contingent item to print the room description, player inventory and choices for the room
def room_return_item(room_name_item, room_name_no_item, room_choices, item_name):
    if item_name in player.items:
        print(room_name_item)
    else: 
        print(room_name_no_item)
    print(player.__repr__())
    room_choice = input(room_choices).strip()
    return room_choice

# Function for just the return to a room dependent on visiting another room to print the room description, player inventory and choices for the room
def room_return_conditional(room_name, contingent_room, room_return, contingent_return, room_choices):
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name)
    else:
        if contingent_room not in player.visited:
            print(room_return)
        else:
            print(contingent_return)
    print(player.__repr__())
    room_choice = input(room_choices).strip()
    return room_choice


# Function to take the player choice for each room and process it - her consider the input set up for when player has incorrect input - instead of just asking for the input again it should re-call the whole function to start again which may fix the inability to exit after making one wrong choice/input