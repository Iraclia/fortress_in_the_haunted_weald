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
exit_words = ['exit', 'stop', 'leave']

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
    print("Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, don't die on the way! \n")

    rule_checker()        

    # collect user name for use in future text blocks
    user_name = input("What is your name, adventurer? ").strip()
    # instantiate user as an Adventurer
    if user_name.lower() not in exit_words:
        user_info = Adventurer(user_name)
        return user_info
    else:
        return

#introduces game, establishes player variable 
player = welcome()

# begins the game, calls upon all the following functions in turn based on layout of the rooms - all the following functions have the same basic structure: check if the current room has been visited before, print out the needed text, print the user information, and then prompt choices to make the next action (to move rooms/handle objects)
def begin_adventuring(player):
    if intro not in player.visited:
        player.room_visited(intro)
        print(intro)
        print(player.__repr__())
        intro_pick = input(intro_choices).strip()
    else:
        print(intro_return)
        print(player.__repr__())
        intro_pick = input(intro_choices_return).strip()
    intro_options = ["1", "2"]
    if intro_pick.lower() in exit_words:
        return
    while intro_pick not in intro_options:
        intro_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
    if intro_pick == "1":
        print(run_away.format(player.name))
        replay()
    elif intro_pick == "2":
        pick_enter_fortress()

def pick_enter_fortress():
    if enter_fortress not in player.visited:
        player.room_visited(enter_fortress)
        print(enter_fortress)
    else:
        print(enter_fortress_return)
    print(player.__repr__())
    enter_fortress_pick = input(enter_fortress_choices).strip()
    enter_fortress_options = ["1", "2", "3", "4"]
    if enter_fortress_pick.lower() in exit_words:
        return
    while enter_fortress_pick not in enter_fortress_options:
        enter_fortress_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ").strip()
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
        print(guard_room_return_with_crowbar)
        print(player.__repr__())
        guard_room_pick = input(guard_room_choices_crowbar).strip()
        if guard_room_pick.lower() in exit_words:
            return
        while guard_room_pick != "1":
            guard_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
        if guard_room_pick == "1":
            pick_enter_fortress()
    else:
        if guard_room not in player.visited:
            player.room_visited(guard_room)
            print(guard_room)
        else:
            print(guard_room_return_no_crowbar)
        print(player.__repr__())
        guard_room_pick = input(guard_room_choices).strip()
        guard_room_options = ["1", "2"]
        if guard_room_pick.lower() in exit_words:
            return
        while guard_room_pick not in guard_room_options:
            guard_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if guard_room_pick == "1":
            player.add_item("crowbar")
            pick_enter_fortress()
        elif guard_room_pick == "2":
            pick_enter_fortress()
    
def pick_round_hall():
    if round_hall not in player.visited:
        player.room_visited(round_hall)
        print(round_hall)
    else:
        print(round_hall_return)
    print(player.__repr__())
    round_hall_pick = input(round_hall_choices).strip()
    if round_hall_pick.lower() in exit_words:
        return
    round_hall_options = ["1", "2", "3", "4"]
    while round_hall_pick not in round_hall_options:
        round_hall_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ").strip()
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
        print(shrine_return_with_key)
        print(player.__repr__())
        shrine_pick = input(shrine_choices_key).strip()
        if shrine_pick.lower() in exit_words:
            return
        while shrine_pick != "1":
            shrine_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
        if shrine_pick == "1":
            pick_round_hall()
    else:
        if shrine not in player.visited:
            player.room_visited(shrine)
            print(shrine)
        else:
            print(shrine_return_no_key)
        print(player.__repr__())
        shrine_pick = input(shrine_choices).strip()
        shrine_options = ["1", "2"]
        if shrine_pick.lower() in exit_words:
            return
        while shrine_pick not in shrine_options:
            shrine_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if shrine_pick == "1":
            if "stone seed" in player.items:
                player.remove_item("stone seed")
                player.add_item("key")
                print(shrine_trade_key)
                pick_round_hall()
            else:
                print(shrine_key_stuck)
                pick_shrine()
        elif shrine_pick == "2":
            pick_round_hall()

def pick_reception_room():
    if reception_room not in player.visited:
        player.room_visited(reception_room)
        print(reception_room)
    else:
        print(reception_room_return)
    print(player.__repr__())
    reception_room_pick = input(reception_room_choices).strip()
    if reception_room_pick.lower() in exit_words:
        return
    if reception_room_pick != "1":
        reception_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
    elif reception_room_pick == "1":
        pick_round_hall()

def pick_room_to_stairs():
    if room_to_stairs not in player.visited:
        player.room_visited(room_to_stairs)
        print(room_to_stairs)
    else:
        print(room_to_stairs_return)
    print(player.__repr__())
    room_to_stairs_pick = input(room_to_stairs_choices).strip()
    room_to_stairs_options = ["1", "2"]
    if room_to_stairs_pick.lower() in exit_words:
        return
    while room_to_stairs_pick not in room_to_stairs_options:
        room_to_stairs_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
    if room_to_stairs_pick == "1":
        pick_lower_corridor()
    elif room_to_stairs_pick == "2":
        pick_round_hall()

def pick_lower_corridor():
    if lower_corridor not in player.visited:
        player.room_visited(lower_corridor)
        print(lower_corridor)
    else:
        print(lower_corridor_return)
    print(player.__repr__())
    lower_corridor_pick = input(lower_corridor_choices).strip()
    lower_corridor_options = ["1", "2", "3", "4", "5"]
    if lower_corridor_pick.lower() in exit_words:
        return
    while lower_corridor_pick not in lower_corridor_options:
        lower_corridor_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3, 4 or 5 to continue. ").strip()
    if lower_corridor_pick == "1":
        pick_library()
    elif lower_corridor_pick == "2":
        pick_lower_hall()
    elif lower_corridor_pick == "3":
        pick_study_room()
    elif lower_corridor_pick == "4":
        pick_room_to_stairs()
    elif lower_corridor_pick == "5":
        pick_enter_fortress()
        
def pick_library():    
    if ("scroll" or "ashes") in player.items:
        if "scroll" in player.items:
            print(library_return_with_scroll)
        else: 
            print(library_return_scroll_used)
        print(player.__repr__())
        library_pick = input(library_choices_took_scroll).strip()
        if library_pick.lower() in exit_words:
            return
        while library_pick != "1":
            library_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
        if library_pick == "1":
            pick_lower_corridor()
    else:
        if library not in player.visited:
            player.room_visited(library)
            print(library.format(player.name))
        else:
            print(library_return_no_scroll.format(player.name))
        print(player.__repr__())
        library_pick = input(library_choices).strip()
        library_options = ["1", "2"]
        if library_pick.lower() in exit_words:
            return
        while library_pick not in library_options:
            library_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if library_pick == "1":
            player.add_item("scroll")
            library_pick_2 = input(library_choices_take_scroll).strip()
            while library_pick_2 != "1":
                library_pick_2 = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
            if library_pick_2 == "1":
                pick_lower_corridor()
        elif library_pick == "2":  
            library_pick_3 = input(library_choices_leave_scroll).strip()
            library_choice_3_options = ["1", "2"]
            while library_pick_3 not in library_choice_3_options:
                library_pick_3 = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
            if library_pick_3 == "1":
                pick_lower_corridor()
            else: 
                library_pick_4 = input(library_choices_take_scroll).strip()
                while library_pick_4 != "1":
                    library_pick_4 = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
                if library_pick_4 == "1":
                    pick_lower_corridor() 

def pick_lower_hall():
    if lower_hall not in player.visited:
        player.room_visited(lower_hall)
        print(lower_hall)
    else:
        if trapdoor_room not in player.visited:
            print(lower_hall_return)
        else:
            print(lower_hall_return_open_door)
    print(player.__repr__())
    lower_hall_pick = input(lower_hall_choices).strip()
    if lower_hall_pick.lower() in exit_words:
        return
    lower_hall_options = ["1", "2", "3", "4"]
    while lower_hall_pick not in lower_hall_options:
        lower_hall_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ").strip()
    if lower_hall_pick == "1":
        pick_barracks()
    elif lower_hall_pick == "2":
        pick_mess_hall()
    elif lower_hall_pick == "3":
        pick_trapdoor_room()
    elif lower_hall_pick == "4":
        pick_lower_corridor()

def pick_barracks(): 
    if "stone seed" or "key" in player.items:
        if "stone seed" in player.items:
            print(barracks_return_with_seed)
        else:
            print(barracks_return_with_key)
        print(player.__repr__())
        barracks_pick = input(barracks_choices_seed_taken).strip()
        if barracks_pick.lower() in exit_words:
            return
        while barracks_pick != "1":
            barracks_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
        if barracks_pick == "1":
            pick_lower_hall()
    else:
        if barracks not in player.visited:
            player.room_visited(barracks)
            print(barracks)
        else:
            print(barracks_return_no_seed_or_key)
        print(player.__repr__())
        barracks_pick = input(barracks_choices).strip()
        barracks_options = ["1", "2"]
        if barracks_pick.lower() in exit_words:
            return
        while barracks_pick not in barracks_options:
            barracks_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if barracks_pick == "1":
            player.add_item("stone seed")
            pick_lower_hall()
        elif barracks_pick == "2":
            pick_lower_hall()

def pick_mess_hall(): 
    if mess_hall not in player.visited:
        player.room_visited(mess_hall)
        print(mess_hall)
    elif kitchen not in player.visited:
        print(mess_hall_return)
    else:
        print(mess_hall_return_post_kitchen)
    print(player.__repr__())
    mess_hall_pick = input(mess_hall_choices).strip()
    mess_hall_options = ["1", "2"]
    if mess_hall_pick.lower() in exit_words:
        return
    while mess_hall_pick not in mess_hall_options:
        mess_hall_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
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
    kitchen_pick = input(kitchen_choices).strip()
    kitchen_options = ["1", "2", "3"]
    if kitchen_pick.lower() in exit_words:
        return
    while kitchen_pick not in kitchen_options:
        kitchen_pick = input("Sorry, that is not a valid choice. Please select 1, 2 or 3 to continue. ").strip()
    if kitchen_pick == "1":
        print(pantry_sudden_death.format(player.name))
        replay()
    elif kitchen_pick == "2":
        print(kitchen_boxes)
        kitchen_boxes_pick = input(kitchen_boxes_choices).strip()
        kitchen_boxes_options = ["1", "2"]
        if kitchen_boxes_pick.lower() in exit_words:
            return
        while kitchen_boxes_pick not in kitchen_boxes_options:
            kitchen_boxes_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if kitchen_boxes_pick == "1":
            print(kitchen_figurine)
        elif kitchen_boxes_pick == "2":
            pick_kitchen()
    else:
        pick_mess_hall()

  # finish building out the above texts - include options for returning with/without the figurine being taken      


def pick_trapdoor_room():
    if trapdoor_room not in player.visited:
        player.room_visited(trapdoor_room)
        print(trapdoor_room)
        print(player.__repr__())
        trapdoor_room_pick = input(trapdoor_room_choices).strip()
        trapdoor_room_options = ["1", "2"]
        if trapdoor_room_pick.lower() in exit_words:
            return
        while trapdoor_room_pick not in trapdoor_room_options:
            trapdoor_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
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
            print(trapdoor_room_return_opened)
            print(player.__repr__())
            trapdoor_room_pick = input(trapdoor_room_choices_open).strip()
            trapdoor_room_options = ["1", "2"]
            if trapdoor_room_pick.lower() in exit_words:
                return
            while trapdoor_room_pick not in trapdoor_room_options:
                trapdoor_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
            if trapdoor_room_pick == "1":
                pick_base_of_ladder()
            elif trapdoor_room_pick == "2":
                pick_lower_hall()
        else:
            print(trapdoor_room_return_closed)
            print(player.__repr__())
            trapdoor_room_pick = input(trapdoor_room_choices).strip()
            trapdoor_room_options = ["1", "2"]
            if trapdoor_room_pick.lower() in exit_words:
                return
            while trapdoor_room_pick not in trapdoor_room_options:
                trapdoor_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
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
    if sudden_death_scroll in player.visited:
        base_of_ladder_pick = input(base_of_ladder_choices_survivor).strip()
    else:
        base_of_ladder_pick = input(base_of_ladder_choices).strip()
    base_of_ladder_options = ["1", "2", "3"]
    if base_of_ladder_pick.lower() in exit_words:
        return
    while base_of_ladder_pick not in base_of_ladder_options:
        base_of_ladder_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
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
    if treasure_room not in player.visited:
        player.room_visited(treasure_room)
        print(treasure_room)
    else:
        print(treasure_room_return)
    print(player.__repr__())
    treasure_room_pick = input(treasure_room_choices).strip()
    treasure_room_options = ["1", "2"]
    if treasure_room_pick.lower() in exit_words:
        return
    while treasure_room_pick not in treasure_room_options:
        treasure_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
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

def pick_study_room(): 
    if "candle" in player.items:
        print(study_room_return_candle)
        print(player.__repr__())
        study_room_pick = input(study_room_choices_took_candle).strip()
        if study_room_pick.lower() in exit_words:
            return
        while study_room_pick != "1":
            study_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
        if study_room_pick == "1":
            pick_lower_corridor()
    else:
        if study_room not in player.visited:
            player.room_visited(study_room)
            print(study_room)
        else:
            print(study_room_return_no_candle)
        print(player.__repr__())
        study_room_pick = input(study_room_choices).strip()
        study_room_options = ["1", "2"]
        if study_room_pick.lower() in exit_words:
            return
        while study_room_pick not in study_room_options:
            study_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
        if study_room_pick == "1":
            pick_lower_corridor()
        elif study_room_pick == "2":
            print(study_room_candle)
            player.add_item("candle")
            print(player.__repr__())
            study_room_pick = input(study_room_choices_post_candle).strip()
            study_room_options_post_candle = ["1", "2"] 
            if study_room_pick.lower() in exit_words:
                return
            while study_room_pick not in study_room_options_post_candle:
                study_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ").strip()
            if study_room_pick == "1":
                print(check_study_room)
                study_room_pick = input(study_room_choices_post_check).strip()
                if study_room_pick.lower() in exit_words:
                    return
                while study_room_pick != "1":
                    study_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ").strip()
                if study_room_pick == "1":
                    pick_lower_corridor()
            elif study_room_pick == "2":
                pick_lower_corridor()    

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