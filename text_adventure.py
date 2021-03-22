class Adventurer:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return 'The adventurer {0} currently has: {1} in their inventory.'.format(self.name, (self.items))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

def welcome():
    positives = ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah', 'sure', 'Sure', 'ok', 'Ok', 'yep', 'Yep']

    print('Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, don\'t die on the way! \n')

    rule_check = input('Would you like to read the rules? (Y/N) \n')
    if rule_check in positives:
        print ('\nOkay! This is a text adventure game. As the scenes are described, you will be prompted to make choices, find items, and traverse through the rooms in search of the treasure. Type your response when promted and hit enter to continue to the next step. Have fun! \n\n*** Disclaimer: Lots of reading involved. :) ***')

    user_name = input('\nWhat is your name, adventurer? ')
    user_info = Adventurer(user_name)
    return user_info

#introduces game, establishes player variable for the following story blocks
player = welcome()

# story choice text blocks:
intro = "\nYou find yourself standing deep in a dark forest. The trees soar overhead, seeming to be impossibly tall, blocking out any hint of sunlight - if indeed it is even day. The air is cool and mist seems to waft between the massive tree trunks. Does it move faster each time you look away from it? You don't really remember how you got here... huh. But you do remember what you're supposed to be doing: retrieving a treasure from an abandoned fortress in the darkest part of the Haunted Weald. No one quite knows what this treasure is, but you know it is vital that you find it. A moldering stone edifice stands before you, something built and then lost, forgotten and never returned to. Moss and creepers almost hide the structure entirely, but a door - oddly pristine amongst all the plants - stands a few paces ahead of you. Something shrieks deeper in the forest - it could be the call of a hunting cat... or maybe what is being hunted. What do you do? \n"

intro_choices = "\n1. Flee! No way I'm going in there! \n2. Enter the fortress. \n"

#was choice_1 - now run_away
run_away = "\nYou don't like the sound of the creatures out here, the darkness of the forest, or the shiftiness of the mist out of the corner of your eyes. And you -definitely- don't like the look of this creepy old fortress and its inexplicably inviting door. It doesn't matter how important this mysterious treasure is. Nope, no way. You are outta here! You take off at a run away from the fortress and hopefully back towards town. Or at least some sunlight. Unfortunately for you, whatever was shrieking deeper in the forest was not the only one of its kind. You don't even see what hits you as something drops out of the trees, and you add a shriek of your own to the quiet of the forest before your world goes dark. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of the Haunted Weald. \n\nThe End."

#was choice_2 - now enter_fortress
enter_fortress = "\nYou might not remember getting here, but you do know you need to find the treasure. And surely whatever is inside the fortress can't be nearly as bad as whatever that thing was. This ruin has been abandoned for centuries. Everything should be dead in there. ... Right? Before you can think too much harder about that, you urge your feet into moving and step up to the door. It swings open with the barest whisper of sound almost before you touch the handle. Ooookay, then, that's not creepy at all. You step inside and this time the door -definitely- moves without being touched, shutting firmly behind you. Well. \nDespite being unable to locate any flames, the inside of the fortress is dimly lit with subtly shifting light. Dark shadows gather in the corners, more thickly than it seems like shadows should. You eye them uncertainly, but nothing lunges forth. All the same, each time you glance away you feel sure something moved just barely out of your line of sight. But the sourceless illumination reveals your surroundings well enough. A sturdy wooden door stands to your left, hanging slightly ajar, though it shows nothing of the room beyond. The corridor you stand in, wide enough for three men to walk abreast, stretches further off into the fortress ahead of you. To your right is a short hallway following the exterior wall of the fortress. By the deepening shadows at the end, it looks like it might lead to a staircase. What do you do? \n" 

enter_fortress_choices = "\n1. Enter the door. \n2. Continue down the hallway. \n3. Investigate the stairs. \n4. Maybe this was a bad idea... go back outside. \n"

#was choice_2_a - now guard_room
guard_room = "You decide to have a look through the door. You ease up to it, reaching out to push the door slowly open. This time the door does nothing to help you out - it takes more muscle than you thought it might before the door grinds reluctantly open with a raspy scrape of wood over stone. Having decided nothing is going to jump out of the shadows at you, you step further into the room to have a look around. The square room is rather unremarkable all in all. A thin layer of dust softens the stone floor and coats the few items left in the room. Against the back wall a spindly cot has collapsed in upon itself. A couple of stools are gathered around a low table to your left. The table still holds a pitcher and a few wooden cups. One stool has been knocked over and never picked up. To your right you see a weapons rack bolted onto the wall - empty now of the spears it probably held. It looks like maybe this was the guard's room. Not much to see here. As you start to turn back to the door, a faint metallic gleam catches your eye in the corner near the weapons rack. Huh. Looks like a crowbar.What do you do? \n" 

guard_room_choices = "\n1. Grab the crowbar before you go. You never know when that might come in handy. \n2. Head back to the hallway and don't disturb the dust. \n"

#was choice_2_b - now round_hall
round_hall = "You head down the corridor and deeper into the dim fortress. The stone is pitted and seems to be crumbling to sand in patches. It's almost as if the fortess is slowly rotting away from the inside out. The shiftiness of the dim light and the shadows you would swear won't quite stay still make give a surreal cast to the passage. Maybe this is all a dream. Why are you here getting this treasure anyways? Who is it important to? Questions for afterwards, perhaps.The hallway dumps you out into an expansive, round room. An arched ceiling soars overhead, delicate, twisting columns supporting its weight evenly spaced in a ring a few paces from the wall. Behind the columns there seem to be traces of color on the walls, but whatever art adorned them has long since slid into obscurity with the passage of time. As you walk further in, you notice a domed skylight in the very center - the glass remarkably intact despite the crumbliness of the fortress otherwise. In better times, perhaps sunlight would have streamed through in a solid column, illuminating the swirling mosaic reaching out from the center of the room. Now, though, no light falls through the glass, only the murk of the Weald. Faint motes of dust float in the air like spirits of the once-residents, stirred to a half-life again by the passage of your steps. The quiet begs not to be disturbed in this space and even your breathing seems too loud. To your left is an elaborate doorway, stone foliage so realistic you expect it to move decorating the frame of it in vies, leaves and fragile flowers. The overlarge doors are pushed open already, and you can just make out bits of something in the room. Ahead of you in an equally large doorway, though this one is more restrained in its elegance, subtle curves and swirls of stone making the frame of the door appear to loom larger. You can see glints of gilding where it still stubbornly clings to a few patches of stone. One door stands closed, the other seems to have fallen off its hinges and into the room beyond. To your right is a more normal sized doorway, its frame in keeping with the elegance of the space, but nothing to compare with the other two. What do you do? \n" 

round_hall_choices = "\n1. Head to the left. That otherworldly carving begs a closer look. What might be in a room with a door like that? \n2. Go straight across the room. This looks like a grand doorway, with gold on it no less. Maybe it leads to the treasure room? \n3. Turn right. Sometimes the most interesting things are behind the most unassuming doors, right? \n4. Return to the hallway behind you. \n"

#was choice_2_b_1 - now shrine
shrine = "left to shrine - statue holding key for treasure chest - pick up key - pick 1 - return to big room choice 2_b"

shrine_choices = ""

#was choice_2_b_2 - now reception_room
reception_room = "straight to reception room, pick 1 - return to big room choice 2_b"

reception_room_choices = ""

#was choice_2_b_3 - now room_to_stairs
room_to_stairs = "right to empty room, pick 1 - creepy stairs down - use choice 2_c, 2 - back to big room - return to choice 2_b"

room_to_stairs_choices = ""

#was choice_2_c - now lower_corridor
lower_corridor = "right to creepy stairs down to downstairs hall - pick 1 - library, 2 - straight along downstairs hall, 3 - room with tables, 4 - back up stairs you came down to choice 2_b_3, 5 - up stairs directly across from you to choice 2"

lower_corridor_choices = ""

#was choice_2_c_1 - now library
library = "library with sparkly scroll - collect scroll - pick 1 - back to hall - return to 2_c"

library_choices = ""

#was_choice_2_c_2 - now lower_hall
lower_hall = "downstairs hall/big open room - pick 1 - barracks, 2 - mess hall, 3 - empty room w/ trapdoor, 4 - back to beginning of hall choice 2_c"

lower_hall_choices = ""

#was choice_2_c_2_a - now barracks
barracks = "barracks - pick 1 - back to choice 2_c_2"

barracks_choices = ""

#was choice_2_c_2_b - now mess_hall
mess_hall = "mess hall - pick 1 - back to choice 2_c_2"

mess_hall_choices = ""

#was choice_2_c_2_c - now trapdoor_room
trapdoor_room = "empty room w/ trapdoor - needs crowbar from guard room to open - break crowbar opening it - remove item - pick 1 - trapdoor - choice 3, 2 - back to hall, return to choice 2_c_2"

trapdoor_room_choices = ""

#was choice_3 - now base_of_ladder
base_of_ladder = "ladder down to lower tunnel - pick 1 - left to sudden death, 2 - right to glowy cave, 3 - back up ladder - return to choice 2_c_2_c"

base_of_ladder_choices = ""

#was choice_3_a_scroll - now sudden_death_scroll
sudden_death_scroll = "sudden death - floor gives way, drown in underground river - unless have sparkly scroll from library, levitates you back to choice 3" - "one time use scroll, remove item after one use"

#was choice_3_a_no_scroll - now sudden_death_no_scroll
sudden_death_no_scroll = 'sudden death!'

#was choice_3_b - treasure_room
treasure_room = "glowy treasure room, 1 -retrieve the treasure - only if you have key from shrine or 2 - back to ladder - choice 3"

treasure_room_choices = ""

#was choice_2_c_3 - now study_room
study_room = "room with tables, pick 1 - back to hall, return to choice 2_c"

study_room_choices = ""

treasure_retrieval = "ta-da! you did it!" - "don't forget your lunch, if you survived. love your wife - knew marrying a witch was risky - find yourself in the kitchen at the fridge"


def begin_adventuring(player):
    print(intro)
    print(player.__repr__())
    intro_pick = input(intro_choices)
    intro_options = ['1', '2']
    while intro_pick not in intro_options:
        intro_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if intro_pick == '1':
        print(run_away.format(player.name))
        replay()
    elif intro_pick == '2':
        pick_enter_fortress()

def pick_enter_fortress():
    print(enter_fortress)
    print(player.__repr__())
    enter_fortress_pick = input(enter_fortress_choices)
    enter_fortress_options = ['1', '2', '3', '4']
    while enter_fortress_pick not in enter_fortress_options:
        enter_fortress_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if enter_fortress_pick == '1':
        pick_guard_room()
    elif enter_fortress_pick == '2':
        pick_round_hall()
    elif enter_fortress_pick == '3':
        pick_lower_corridor()
    elif enter_fortress_pick == '4':
        begin_adventuring(player)
    
def pick_guard_room():
    print(guard_room)
    print(player.__repr__())
    guard_room_pick = input(guard_room_choices)
    guard_room_options = ['1', '2']
    while guard_room_pick not in guard_room_options:
        guard_room_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if guard_room_pick == '1':
        player.add_item('crowbar')
        pick_enter_fortress()
    elif guard_room_pick == '2':
        pick_enter_fortress()

def pick_round_hall():
    print(round_hall)
    print(player.__repr__())
    round_hall_pick = input(round_hall_choices)
    round_hall_options = ['1', '2', '3', '4']
    while round_hall_pick not in round_hall_options:
        round_hall_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if round_hall_pick == '1':
        pick_shrine()
    elif round_hall_pick == '2':
        pick_reception_room()
    elif round_hall_pick == '3':
        pick_room_to_stairs()
    elif round_hall_pick == '4':
        pick_enter_fortress()

def pick_shrine():
    print(shrine)
    print(player.__repr__())
    shrine_pick = input(shrine_choices)
    shrine_options = ['1', '2']
    while shrine_pick not in shrine_options:
        shrine_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if shrine_pick == '1':
        player.add_item('key')
        pick_round_hall()
    elif shrine_pick == '2':
        pick_round_hall()

def pick_reception_room():
    print(reception_room)
    print(player.__repr__())
    reception_room_pick = input(reception_room_choices)
    if reception_room_pick != '1':
        reception_room_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif reception_room_pick == '1':
        pick_round_hall()

def pick_room_to_stairs():
    print(room_to_stairs)
    print(player.__repr__())
    room_to_stairs_pick = input(room_to_stairs_choices)
    room_to_stairs_options = ['1', '2']
    while room_to_stairs_pick not in room_to_stairs_options:
        room_to_stairs_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if room_to_stairs_pick == '1':
        pick_lower_corridor()
    elif room_to_stairs_pick == '2':
        pick_round_hall()

def pick_lower_corridor():
    print(lower_corridor)
    print(player.__repr__())
    lower_corridor_pick = input(lower_corridor_choices)
    lower_corridor_options = ['1', '2', '3', '4', '5']
    while lower_corridor_pick not in lower_corridor_options:
        lower_corridor_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3, 4 or 5 to continue. ')
    if lower_corridor_pick == '1':
        pick_library()
    elif lower_corridor_pick == '2':
        pick_lower_hall()
    elif lower_corridor_pick == '3':
        pick_study_room()
    elif lower_corridor_pick == '4':
        pick_room_to_stairs()
    elif lower_corridor_pick == '5':
        pick_enter_fortress()
        
def pick_library():
    print(library)
    print(player.__repr__())
    library_pick = input(library_choices)
    library_options = ['1', '2']
    while library_pick not in library_options:
        library_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if library_pick == '1':
        player.add_item('scroll')
        pick_lower_corridor()
    elif library_pick == '2':
        pick_lower_corridor()

def pick_lower_hall():
    print(lower_hall)
    print(player.__repr__())
    lower_hall_pick = input(lower_hall_choices)
    lower_hall_options = ['1', '2', '3', '4']
    while lower_hall_pick not in lower_hall_options:
        lower_hall_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if lower_hall_pick == '1':
        pick_barracks()
    elif lower_hall_pick == '2':
        pick_mess_hall()
    elif lower_hall_pick == '3':
        pick_trapdoor_room()
    elif lower_hall_pick == '4':
        pick_lower_corridor()

def pick_barracks(): 
    print(barracks)
    print(player.__repr__())
    barracks_pick = input(barracks_choices)
    if barracks_pick != '1':
        barracks_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif barracks_pick == '1':
        pick_lower_hall()

def pick_mess_hall(): 
    print(mess_hall)
    print(player.__repr__())
    mess_hall_pick = input(mess_hall_choices)
    if mess_hall_pick != '1':
        mess_hall_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif mess_hall_pick == '1':
        pick_lower_hall()

def pick_trapdoor_room():
    print(trapdoor_room)
    print(player.__repr__())
    trapdoor_room_pick = input(trapdoor_room_choices)
    trapdoor_room_options = ['1', '2']
    while trapdoor_room_pick not in trapdoor_room_options:
        trapdoor_room_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if trapdoor_room_pick == '1':
        if 'crowbar' in player.items:
            print("The trapdoor is stubbornly wedged in place - age doesn't seem to have weakened the wood. If anything it has made the thing more difficult to get through. Luckily you came prepared. You pull out that handy crowbar you picked up and throw your weight into prying the door open. The trapdoor resists, before it slowly starts to shift with an audible groan of protest. Then, with a thunderous snap and a the sharp clatter of metal on stone, the door pops open. Your trusty crowbar, sadly, gave its life for the task. It didn't seem to have aged as well as the trapdoor itself.")
            player.remove_item('crowbar')
            pick_base_of_ladder()
        else:
            print('You push and pull and tug and stomp, but the trapdoor absolutely refuses to budge. If it had a face you imagine it would be laughing at your efforts. Maybe you need something to pry it open with... \n\n')
            pick_trapdoor_room()
    elif trapdoor_room_pick == '2':
        pick_lower_hall()

def pick_base_of_ladder(): 
    print(base_of_ladder)
    print(player.__repr__())
    base_of_ladder_pick = input(base_of_ladder_choices)
    base_of_ladder_options = ['1', '2', '3']
    while base_of_ladder_pick not in base_of_ladder_options:
        base_of_ladder_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if base_of_ladder_pick == '1':
        pick_sudden_death()
    elif base_of_ladder_pick == '2':
        pick_treasure_room()
    elif base_of_ladder_pick == '3':
        pick_trapdoor_room()

def pick_sudden_death():
    if 'scroll' in player.items:
        print(sudden_death_scroll)
        player.remove_item('scroll')
        pick_base_of_ladder()
    else:
        print(sudden_death_no_scroll)
        replay()

def pick_treasure_room(): 
    print(treasure_room)
    print(player.__repr__())
    treasure_room_pick = input(treasure_room_choices)
    treasure_room_options = ['1', '2']
    while treasure_room_pick not in treasure_room_options:
        treasure_room_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if treasure_room_pick == '1':
        if 'key' in player.items:
            print(treasure_retrieval)
            replay()
        else:
            print("Closer examination of the chest reveals a keyhole in the center of the lid. Maybe you can get it open anyways... it's been down here for ages anyways, right? You push and tug and kick and even try asking it nicely (and not so nicely) to open. Seems like they had immpecable craftsmanship back in the day. Perhaps the key was left behind somewhere in the fortress...\n\n")
            pick_treasure_room()
    elif treasure_room_pick == '2':
        pick_base_of_ladder()

def pick_study_room(): 
    print(study_room)
    print(player.__repr__())
    study_room_pick = input(study_room_choices)
    if study_room_pick != '1':
        study_room_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif study_room_pick == '1':
        pick_lower_corridor()

def replay():
    positives = ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah', 'sure', 'Sure', 'ok', 'Ok', 'yep', 'Yep']

    restart = input("\n\nWould you like to play again? (Y/N) ")
    if restart in positives:
        begin_adventuring(player)
    

begin_adventuring(player)




''' In the future, if going to build out additional functionality:
- add additional rooms, etc
- and/or additional interaction within rooms - opening cupboards, looking around/under things, etc
  - maybe add a 'search' method to the adventurer class to do so?
- add more items
- add more needed keys/items/etc
- add puzzles?
- add a time limit? tracked by number of turns
  - perhaps leading to an earthquake, etc, with warnings at certain thresholds to hint at such
'''