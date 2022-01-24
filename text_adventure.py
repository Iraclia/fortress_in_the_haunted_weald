from text_adventure_blocks import *  # functional code separated from text blocks for ease of organizing

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

# establishes variations of yes/no that will be accepted
positives = ["y", "yes", "yeah", "sure", "ok", "okay", "yep", "yah"]
negatives = ["n", "no", "nah", "nope", "nu"]

# establishing words to exit the game at any point
exit_words = ["exit", "stop", "leave", "quit", "terminate", "escape", "close"]

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

def welcome():
    print("Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, try not to die on the way! \n")

    rule_checker()        

    # collect user name for use in future text blocks
    user_name = input("What is your name, adventurer? ").strip()
    # instantiate user as an Adventurer
    if user_name.lower() not in exit_words:
        player = Adventurer(user_name)
        return player
    else:
        return

# Function to check/add player visit to a room and to print the room description, player inventory and get player choices for the room 
def room_basic(room_name, room_return, room_choices, input_options, return_choices=None):
    if return_choices == None:
        return_choices = room_choices
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name)
        print(player.__repr__())
        room_choice = get_choice(room_choices, input_options)
        return room_choice
    else:
        print(room_return)
        print(player.__repr__())
        room_choice = get_choice(return_choices, input_options)
        return room_choice

# Function for conditional entry to a room for the first time to print the room descrition, player inventory and choices for the room
def room_basic_conditional(room_name, room_choices, input_options):
    player.room_visited(room_name)
    print(room_name)
    print(player.__repr__())
    room_choice = get_choice(room_choices, input_options)
    return room_choice

# Function for just the return to a room to print the room description, player inventory and choices for the room
def room_return(room_name, room_choices, input_options):
    print(room_name)
    print(player.__repr__())
    room_choice = get_choice(room_choices, input_options)
    return room_choice

# Function to check/add player visit to a room and to print the room description including the player name, player inventory and choices for the room -- Perhaps see if this can be combined with the basic room function? Options for including a name based on a T/F name parameter with a default F?
def room_with_player_name(room_name, room_return, room_choices, input_options, return_choices=None):
    if return_choices == None:
        return_choices = room_choices
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name.format(player.name))
        print(player.__repr__())
        room_choice = get_choice(room_choices, input_options)
        return room_choice
    else:
        print(room_return.format(player.name))
        print(player.__repr__())
        room_choice = get_choice(room_choices, input_options)
        return room_choice

# Function for just the return to a room with a contingent item to print the room description, player inventory and choices for the room
def room_return_item(room_name_item, room_name_no_item, room_choices, input_options, item_name):
    if item_name in player.items:
        print(room_name_item)
    else: 
        print(room_name_no_item)
    print(player.__repr__())
    room_choice = get_choice(room_choices, input_options)
    return room_choice

# Function for just the return to a room dependent on visiting another room to print the room description, player inventory and choices for the room
def room_return_conditional(room_name, contingent_room, room_return, contingent_return, room_choices, input_options):
    if room_name not in player.visited:
        player.room_visited(room_name)
        print(room_name)
    else:
        if contingent_room not in player.visited:
            print(room_return)
        else:
            print(contingent_return)
    print(player.__repr__())
    room_choice = get_choice(room_choices, input_options)
    return room_choice

# Function to gather user choices from the room options, check for exit words and make sure choice is valid
def get_choice(room_choices, input_options):
    room_choice = input(room_choices).strip()
    if room_choice.lower() in exit_words:
        print("Sorry to see you go! Thank you for playing!")
        return
    elif room_choice not in input_options:
        print("Sorry, that is not a valid choice. Please select a valid option number to continue. ")
        get_choice(room_choices, input_options)
    else:
        return room_choice
    

# Introduces game, establishes player variable 
player = welcome()

# Begins the game, calls upon all the following functions in turn based on layout of the rooms - all the following functions have the same basic structure: check if the current room has been visited before, print out the needed text, print the user information, and then prompt choices to make the next action (to move rooms/handle objects)

def begin_adventuring(player):
    intro_options = ["1", "2"]
    intro_pick = room_basic(intro, intro_return, intro_choices, intro_options, intro_choices_return)
    if intro_pick == "1":
        print(run_away.format(player.name))
        replay()
    elif intro_pick == "2":
        pick_enter_fortress()

def pick_enter_fortress():
    enter_fortress_options = ["1", "2", "3", "4"]
    enter_fortress_pick = room_basic(enter_fortress, enter_fortress_return, enter_fortress_choices, enter_fortress_options)
    if enter_fortress_pick == "1":
        pick_guard_room()
    elif enter_fortress_pick == "2":
        pick_round_hall()
    elif enter_fortress_pick == "3":
        pick_lower_corridor()
    elif enter_fortress_pick == "4":
        begin_adventuring(player)
    
def pick_guard_room():
    if "crowbar" in player.items:
        guard_room_options = ["1"]
        guard_room_pick = room_return(guard_room_return_with_crowbar, guard_room_choices_crowbar, guard_room_options)
        if guard_room_pick == "1":
            pick_enter_fortress()
    else:
        guard_room_options = ["1", "2"]
        guard_room_pick = room_basic(guard_room, guard_room_return_no_crowbar, guard_room_choices, guard_room_options)
        if guard_room_pick == "1":
            player.add_item("crowbar")
            pick_enter_fortress()
        elif guard_room_pick == "2":
            pick_enter_fortress()
    
def pick_round_hall():
    round_hall_options = ["1", "2", "3", "4"]
    round_hall_pick = room_basic(round_hall, round_hall_return, round_hall_choices, round_hall_options)
    if round_hall_pick == "1":
        pick_shrine()
    elif round_hall_pick == "2":
        pick_reception_room()
    elif round_hall_pick == "3":
        pick_room_to_stairs()
    elif round_hall_pick == "4":
        pick_enter_fortress()

def pick_shrine():
    if "key" in player.items:
        shrine_options = ["1"]
        shrine_pick = room_return(shrine_return_with_key, shrine_choices_key, shrine_options)
        if shrine_pick == "1":
            pick_round_hall()
    else:
        shrine_options = ["1", "2"]
        shrine_pick = room_basic(shrine, shrine_return_no_key, shrine_choices, shrine_options)
        if shrine_pick == "1":
            if "stone seed" in player.items:
                player.remove_item("stone seed")
                player.add_item("key")
                print(shrine_trade_key)
                pick_round_hall()
            else:
                shrine_options = ["1"]
                shrine_pick = room_return(shrine_key_stuck, shrine_options_stuck_key, shrine_options)
                if shrine_pick == "1":
                    pick_round_hall()
        elif shrine_pick == "2":
            pick_round_hall()

def pick_reception_room():
    reception_room_options = ["1"]
    reception_room_pick = room_basic(reception_room, reception_room_return, reception_room_choices, reception_room_options)
    if reception_room_pick == "1":
        pick_round_hall()

def pick_room_to_stairs():
    room_to_stairs_options = ["1", "2"]
    room_to_stairs_pick = room_basic(room_to_stairs, room_to_stairs_return, room_to_stairs_choices, room_to_stairs_options)
    if room_to_stairs_pick == "1":
        pick_lower_corridor()
    elif room_to_stairs_pick == "2":
        pick_round_hall()

def pick_lower_corridor():
    lower_corridor_options = ["1", "2", "3", "4", "5"]
    lower_corridor_pick = room_basic(lower_corridor, lower_corridor_return, lower_corridor_choices, lower_corridor_options)
    if lower_corridor_pick == "1":
        pick_library()
    elif lower_corridor_pick == "2":
        pick_lower_hall()
    elif lower_corridor_pick == "3":
        pick_study_room()
    elif lower_corridor_pick == "4":
        pick_room_to_stairs()
        #this needs another examination, if you return from the lower corridor the text doesn't read right
    elif lower_corridor_pick == "5":
        pick_enter_fortress()
        
def pick_library():    
    if ("scroll" or "ashes") in player.items:
        library_options = ["1"]
        library_pick = room_return_item(library_return_with_scroll, library_return_scroll_used, library_choices_took_scroll, library_options, 'scroll')
        if library_pick == "1":
            pick_lower_corridor()
    else:
        library_options = ["1", "2"]
        library_pick = room_with_player_name(library, library_return_no_scroll, library_choices, library_options)
        if library_pick == "1":
            player.add_item("scroll")
            library_options_2 = ["1"]
            library_pick_2 = room_return(library_take_scroll, library_choices_take_scroll, library_options_2)
            if library_pick_2 == "1":
                pick_lower_corridor()
        elif library_pick == "2":  
            library_options_3 = ["1", "2"]
            library_pick_3 = room_return(library_leave_scroll, library_choices_leave_scroll, library_options_3)
            if library_pick_3 == "1":
                pick_lower_corridor()
            elif library_pick_3 == "2": 
                library_options_4 = ["1"]
                library_pick_4 = room_return(library_take_scroll, library_choices_took_scroll, library_options_4)
                if library_pick_4 == "1":
                    pick_lower_corridor() 

def pick_lower_hall():
    lower_hall_options = ["1", "2", "3", "4"]
    lower_hall_pick = room_return_conditional(lower_hall, trapdoor_room, lower_hall_return, lower_hall_return_open_door, lower_hall_choices, lower_hall_options)
    if lower_hall_pick == "1":
        pick_barracks()
    elif lower_hall_pick == "2":
        pick_mess_hall()
    elif lower_hall_pick == "3":
        pick_trapdoor_room()
    elif lower_hall_pick == "4":
        pick_lower_corridor()

def pick_barracks(): 
    if ("stone seed" or "key") in player.items:
        barracks_options = ["1"]
        barracks_pick = room_return_item(barracks_return_with_seed, barracks_return_with_key, barracks_choices_seed_taken, barracks_options, "stone seed")
        if barracks_pick == "1":
            pick_lower_hall()
    else:
        barracks_options = ["1", "2"]
        barracks_pick = room_basic(barracks, barracks_return_no_seed_or_key, barracks_choices, barracks_options)
        if barracks_pick == "1":
            player.add_item("stone seed")
            pick_lower_hall()
        elif barracks_pick == "2":
            pick_lower_hall()

def pick_mess_hall(): 
    mess_hall_options = ["1", "2"]
    mess_hall_pick = room_return_conditional(mess_hall, kitchen, mess_hall_return, mess_hall_return_post_kitchen, mess_hall_choices, mess_hall_options)
    if mess_hall_pick == "1":
        pick_kitchen()
    elif mess_hall_pick == "2":
        pick_lower_hall()

def pick_kitchen():
    if ("candle" not in player.items) and (kitchen not in player.visited):
            print(kitchen_no_candle.format(player.name))
            replay()
    elif ("candle" in player.items) and (kitchen not in player.visited):
        player.room_visited(kitchen)
        print(kitchen)
        player.remove_item("candle")
    else:
        print(kitchen_return) 
    print(player.__repr__())
    kitchen_options = ["1", "2", "3"]
    kitchen_pick = get_choice(kitchen_choices, kitchen_options)
    if kitchen_pick == "1":
        print(pantry_sudden_death.format(player.name))
        replay()
    elif kitchen_pick == "2":
        print(kitchen_boxes)
        kitchen_boxes_options = ["1", "2"]
        kitchen_boxes_pick = get_choice(kitchen_boxes_choices, kitchen_boxes_options)
        if kitchen_boxes_pick == "1":
            print(kitchen_figurine)
        elif kitchen_boxes_pick == "2":
            pick_kitchen()
    else:
        pick_mess_hall()

  # finish building out the above texts - include options for returning with/without the figurine being taken      

def pick_study_room(): 
    if "candle" in player.items:
        study_room_options = ["1"]
        study_room_pick = room_return(study_room_return_candle, study_room_choices_took_candle, study_room_options)
        if study_room_pick == "1":
            pick_lower_corridor()
    else:
        study_room_options = ["1", "2"]
        study_room_pick = room_basic(study_room, study_room_return_no_candle, study_room_choices, study_room_options)
        if study_room_pick == "1":
            pick_lower_corridor()
        elif study_room_pick == "2":
            print(study_room_candle)
            player.add_item("candle")
            print(player.__repr__())
            study_room_options_post_candle = ["1", "2"] 
            study_room_pick = get_choice(study_room_choices_post_candle, study_room_options_post_candle)
            if study_room_pick == "1":
                print(check_study_room)
                print(player.__repr__())
                study_room_options_post_check = ["1"]
                study_room_pick = get_choice(study_room_choices_post_check, study_room_options_post_check)
                if study_room_pick == "1":
                    pick_lower_corridor()
            elif study_room_pick == "2":
                pick_lower_corridor()    

def pick_trapdoor_room():
    if trapdoor_room not in player.visited:
        trapdoor_room_options = ["1", "2"]
        trapdoor_room_pick = room_basic_conditional(trapdoor_room, trapdoor_room_choices, trapdoor_room_options)
        if trapdoor_room_pick == "1":
            if "crowbar" in player.items:
                print(opening_trapdoor)
                player.remove_item("crowbar")
                player.add_item("broken crowbar")
                pick_trapdoor_room()
            else:
                print(trapdoor_no_crowbar)
                pick_trapdoor_room()
        elif trapdoor_room_pick == "2":
            pick_lower_hall()
    else:
        if "broken crowbar" in player.items:
            trapdoor_room_options = ["1", "2"]
            trapdoor_room_pick = room_return(trapdoor_room_return_opened, trapdoor_room_choices_open, trapdoor_room_options)
            if trapdoor_room_pick == "1":
                pick_base_of_ladder()
            elif trapdoor_room_pick == "2":
                pick_lower_hall()
        else:
            trapdoor_room_options = ["1", "2"]
            trapdoor_room_pick = room_return(trapdoor_room_return_closed, trapdoor_room_choices, trapdoor_room_options)
            if trapdoor_room_pick == "1":
                if "crowbar" in player.items:
                    print(opening_trapdoor)
                    player.remove_item("crowbar")
                    player.add_item("broken crowbar")
                    pick_base_of_ladder()
                else:
                    print(trapdoor_no_crowbar)
                    pick_trapdoor_room()
            elif trapdoor_room_pick == "2":
                pick_lower_hall()

def pick_base_of_ladder(): 
    if base_of_ladder not in player.visited:
        player.room_visited(base_of_ladder)
        print(base_of_ladder)
    else:
        print(base_of_ladder_return)
    print(player.__repr__())
    base_of_ladder_options = ["1", "2", "3"]
    if sudden_death_scroll in player.visited:
        base_of_ladder_pick = get_choice(base_of_ladder_choices_survivor, base_of_ladder_options)
    else:
        base_of_ladder_pick = get_choice(base_of_ladder_choices, base_of_ladder_options)
    if base_of_ladder_pick == "1":
        pick_sudden_death()
    elif base_of_ladder_pick == "2":
        pick_treasure_room()
    elif base_of_ladder_pick == "3":
        pick_trapdoor_room()

def pick_sudden_death():
    if "scroll" in player.items:
        player.room_visited(sudden_death_scroll)
        print(sudden_death_scroll)
        player.remove_item("scroll")
        player.add_item("ashes")
        pick_base_of_ladder()
    else:
        print(sudden_death_no_scroll.format(player.name))
        replay()

def pick_treasure_room(): 
    treasure_room_options = ["1", "2"]
    treasure_room_pick = room_basic(treasure_room, treasure_room_return, treasure_room_choices, treasure_room_options)
    if treasure_room_pick == "1":
        if "key" in player.items:
            print(treasure_retrieval)
            player.remove_item("key")
            replay()
        else:
            print(treasure_room_chest)
            pick_treasure_room()
    elif treasure_room_pick == "2":
        pick_base_of_ladder()

def replay():
    restart = input("\nWould you like to play again? (Y/N) ").lower().strip()
    if restart in positives:
        player.items = []
        player.visited = []
        begin_adventuring(player)
    elif restart in negatives:
        print("Thank you for playing!")
        return
    else:
        print("\nSorry, that is not a valid response. Please select Y or N to continue. ")
        replay()


# starts the actual gameplay
if player:
    begin_adventuring(player)



''' In the future, if going to build out additional functionality:
- add additional rooms, etc
- and/or additional interaction within rooms - opening cupboards, looking around/under things, etc
  - maybe add a 'search' method to the adventurer class to do so? to search rooms for things?
- add more needed keys/items/etc
- add more ways to die/lose
- add puzzles?
- add a time limit? tracked by number of turns
  - perhaps leading to an earthquake, etc, with warnings at certain thresholds to hint at such

- perhaps add random endings? write up a few different endings, choose random number to pick which one you get
- add an easter egg ^^
'''