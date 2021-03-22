class Adventurer:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return 'The adventurer {0} currently has: {1} in their inventory.'.format(self.name, (self.items))

    def add_item(self, item):
        self.items.append(item)

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
intro = "\nYou find yourself standing deep in a dark forest. The trees soar overhead, seeming to be impossibly tall, blocking out any hint of sunlight - if indeed it is even day. The air is cool and mist seems to waft between the massive tree trunks. Does it move faster each time you look away from it? You don't really remember how you got here... huh. But you do remember what you're supposed to be doing: retrieving a treasure from an abandoned fortress in the darkest part of the Haunted Weald. No one quite knows what this treasure is, but you know it is vital that you find it. A moldering stone edifice stands before you, something built and then lost, forgotten and never returned to. Moss and creepers almost hide the structure entirely, but a door - oddly pristine amongst all the plants - stands a few paces ahead of you. Something shrieks deeper in the forest - it could be the call of a hunting cat... or maybe what is being hunted. What do you do? \n\n" + player.__repr__() + "\n\n1. Flee! No way I'm going in there! \n2. Enter the fortress. \n"

choice_1 = "\nYou don't like the sound of the creatures out here, the darkness of the forest, or the shiftiness of the mist out of the corner of your eyes. And you -definitely- don't like the look of this creepy old fortress and its inexplicably inviting door. It doesn't matter how important this mysterious treasure is. Nope, no way. You are outta here! You take off at a run away from the fortress and hopefully back towards town. Or at least some sunlight. Unfortunately for you, whatever was shrieking deeper in the forest was not the only one of its kind. You don't even see what hits you as something drops out of the trees, and you add a shriek of your own to the quiet of the forest before your world goes dark. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of the Haunted Weald. \n\nThe End."

choice_2 = "\nYou might not remember getting here, but you do know you need to find the treasure. And surely whatever is inside the fortress can't be nearly as bad as whatever that thing was. This ruin has been abandoned for centuries. Everything should be dead in there. ... Right? Before you can think too much harder about that, you urge your feet into moving and step up to the door. It swings open with the barest whisper of sound almost before you touch the handle. Ooookay, then, that's not creepy at all. You step inside and this time the door -definitely- moves without being touched, shutting firmly behind you. Well. \nDespite being unable to locate any flames, the inside of the fortress is dimly lit with subtly shifting light. Dark shadows gather in the corners, more thickly than it seems like shadows should. You eye them uncertainly, but nothing lunges forth. All the same, each time you glance away you feel sure something moved just barely out of your line of sight. But the sourceless illumination reveals your surroundings well enough. A sturdy wooden door stands to your left, hanging slightly ajar, though it shows nothing of the room beyond. The corridor you stand in, wide enough for three men to walk abreast, stretches further off into the fortress ahead of you. To your right is a short hallway following the exterior wall of the fortress. By the deepening shadows at the end, it looks like it might lead to a staircase. What do you do? \n\n" + player.__repr__() + "\n\n1. Enter the door. \n2. Continue down the hallway. \n3. Investigate the stairs. \n4. Maybe this was a bad idea... go back outside. \n"

choice_2_a = "You decide to have a look through the door. You ease up to it, reaching out to push the door slowly open. This time the door does nothing to help you out - it takes more muscle than you thought it might before the door grinds reluctantly open with a raspy scrape of wood over stone. Having decided nothing is going to jump out of the shadows at you, you step further into the room to have a look around. The square room is rather unremarkable all in all. A thin layer of dust softens the stone floor and coats the few items left in the room. Against the back wall a spindly cot has collapsed in upon itself. A couple of stools are gathered around a low table to your left. The table still holds a pitcher and a few wooden cups. One stool has been knocked over and never picked up. To your right you see a weapons rack bolted onto the wall - empty now of the spears it probably held. It looks like maybe this was the guard's room. Not much to see here. As you start to turn back to the door, a faint metallic gleam catches your eye in the corner near the weapons rack. Huh. Looks like a crowbar.What do you do? \n\n" + player.__repr__() + "\n\n1. Grab the crowbar before you go. You never know when that might come in handy. \n2. Head back to the hallway and don't disturb the dust. \n"

choice_2_b = "You head down the corridor and deeper into the dim fortress. The stone is pitted and seems to be crumbling to sand in patches. It's almost as if the fortess is slowly rotting away from the inside out. The shiftiness of the dim light and the shadows you would swear won't quite stay still make give a surreal cast to the passage. Maybe this is all a dream. Why are you here getting this treasure anyways? Who is it important to? Questions for afterwards, perhaps.The hallway dumps you out into an expansive, round room. An arched ceiling soars overhead, delicate, twisting columns supporting its weight evenly spaced in a ring a few paces from the wall. Behind the columns there seem to be traces of color on the walls, but whatever art adorned them has long since slid into obscurity with the passage of time. As you walk further in, you notice a domed skylight in the very center - the glass remarkably intact despite the crumbliness of the fortress otherwise. In better times, perhaps sunlight would have streamed through in a solid column, illuminating the swirling mosaic reaching out from the center of the room. Now, though, no light falls through the glass, only the murk of the Weald. Faint motes of dust float in the air like spirits of the once-residents, stirred to a half-life again by the passage of your steps. The quiet begs not to be disturbed in this space and even your breathing seems too loud. To your left is an elaborate doorway, stone foliage so realistic you expect it to move decorating the frame of it in vies, leaves and fragile flowers. The overlarge doors are pushed open already, and you can just make out bits of something in the room. Ahead of you in an equally large doorway, though this one is more restrained in its elegance, subtle curves and swirls of stone making the frame of the door appear to loom larger. You can see glints of gilding where it still stubbornly clings to a few patches of stone. One door stands closed, the other seems to have fallen off its hinges and into the room beyond. To your right is a more normal sized doorway, its frame in keeping with the elegance of the space, but nothing to compare with the other two. What do you do? \n\n" + player.__repr__() + "\n\n1. Head to the left. That otherworldly carving begs a closer look. What might be in a room with a door like that? \n2. Go straight across the room. This looks like a grand doorway, with gold on it no less. Maybe it leads to the treasure room? \n3. Turn right. Sometimes the most interesting things are behind the most unassuming doors, right? \n4. Return to the hallway behind you. \n"

choice_2_b_1 = "left to shrine - statue holding key for treasure chest - pick up key - pick 1 - return to big room choice 2_b"

choice_2_b_2 = "straight to reception room, pick 1 - return to big room choice 2_b"

choice_2_b_3 = "right to empty room, pick 1 - creepy stairs down - use choice 2_c, 2 - back to big room - return to choice 2_b"

choice_2_c = "right to creepy stairs down to downstairs hall - pick 1 - library, 2 - straight along downstairs hall, 3 - room with tables, 4 - back up stairs you came down to choice 2_b_3, 5 - up stairs directly across from you to choice 2"

choice_2_c_1 = "library with sparkly scroll - collect scroll - pick 1 - back to hall - return to 2_c"

choice_2_c_2 = "downstairs hall - pick 1 - barracks, 2 - mess hall, 3 - empty room w/ trapdoor, 4 - back to beginning of hall choice 2_c"

choice_2_c_2_a = "barracks - pick 1 - back to choice 2_c_2"

choice_2_c_2_b = "mess hall - pick 1 - back to choice 2_c_2"

choice_2_c_2_c = "empty room w/ trapdoor - needs crowbar from guard room to open - pick 1 - trapdoor - choice 3, 2 - back to hall, return to choice 2_c_2"

choice_3 = "ladder down to lower tunnel - pick 1 - left to sudden death, 2 - right to glowy cave, 3 - back up ladder - return to choice 2_c_2_c"

choice_3_a_scroll = "sudden death - floor gives way, drown in underground river - unless have sparkly scroll from library, levitates you back to choice 3"

choice_3_a_no_scroll = 'sudden death!'

choice_3_b = "glowy treasure room, 1 -retrieve the treasure - only if you have key from shrine or 2 - back to ladder - choice 3"

choice_2_c_3 = "room with tables, pick 1 - back to hall, return to choice 2_c"

treasure_retrieval = "ta-da! you did it!"


def enter_the_fortress(player):
    intro_pick = input(intro)
    intro_pick_options = ['1', '2']
    while intro_pick not in intro_pick_options:
        intro_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if intro_pick == '1':
        print(choice_1.format(player.name))
        replay()
    elif intro_pick == '2':
        pick_choice_2()

def pick_choice_2():
    choice_2_pick = input(choice_2)
    choice_2_options = ['1', '2', '3', '4']
    while choice_2_pick not in choice_2_options:
        choice_2_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if choice_2_pick == '1':
        pick_choice_2_a()
    elif choice_2_pick == '2':
        pick_choice_2_b()
    elif choice_2_pick == '3':
        pick_choice_2_c()
    elif choice_2_pick == '4':
        enter_the_fortress(player)
    
def pick_choice_2_a():
    choice_2_a_pick = input(choice_2_a)
    choice_2_a_options = ['1', '2']
    while choice_2_a_pick not in choice_2_a_options:
        choice_2_a_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_2_a_pick == '1':
        player.add_item('crowbar')
        pick_choice_2()
    elif choice_2_a_pick == '2':
        pick_choice_2()

def pick_choice_2_b():
    choice_2_b_pick = input(choice_2_b)
    choice_2_b_options = ['1', '2', '3', '4']
    while choice_2_b_pick not in choice_2_b_options:
        choice_2_b_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if choice_2_b_pick == '1':
        pick_choice_2_b_1()
    elif choice_2_b_pick == '2':
        pick_choice_2_b_2()
    elif choice_2_b_pick == '3':
        pick_choice_2_b_3()
    elif choice_2_b_pick == '4':
        pick_choice_2()

def pick_choice_2_b_1():
    choice_2_b_1_pick = input(choice_2_b_1)
    choice_2_b_1_options = ['1', '2']
    while choice_2_b_1_pick not in choice_2_b_1_options:
        choice_2_b_1_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_2_b_1_pick == '1':
        player.add_item('key')
        pick_choice_2_b()
    elif choice_2_b_1_pick == '2':
        pick_choice_2_b()

def pick_choice_2_b_2():
    choice_2_b_2_pick = input(choice_2_b_2)
    if choice_2_b_2_pick != '1':
        choice_2_b_2_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif choice_2_b_2_pick == '1':
        pick_choice_2_b()

def pick_choice_2_b_3():
    choice_2_b_3_pick = input(choice_2_b_3)
    choice_2_b_3_options = ['1', '2']
    while choice_2_b_3_pick not in choice_2_b_3_options:
        choice_2_b_3_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_2_b_3_pick == '1':
        pick_choice_2_c()
    elif choice_2_b_3_pick == '2':
        pick_choice_2_b()

def pick_choice_2_c():
    choice_2_c_pick = input(choice_2_c)
    choice_2_c_options = ['1', '2', '3', '4', '5']
    while choice_2_c_pick not in choice_2_c_options:
        choice_2_c_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3, 4 or 5 to continue. ')
    if choice_2_c_pick == '1':
        pick_choice_2_c_1()
    elif choice_2_c_pick == '2':
        pick_choice_2_c_2()
    elif choice_2_c_pick == '3':
        pick_choice_2_c_3()
    elif choice_2_c_pick == '4':
        pick_choice_2_b_3()
    elif choice_2_c_pick == '5':
        pick_choice_2()

def pick_choice_2_c_1():
    choice_2_c_1_pick = input(choice_2_c_1)
    choice_2_c_1_options = ['1', '2']
    while choice_2_c_1_pick not in choice_2_c_1_options:
        choice_2_c_1_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_2_c_1_pick == '1':
        player.add_item('scroll')
        pick_choice_2_c()
    elif choice_2_c_1_pick == '2':
        pick_choice_2_c()

def pick_choice_2_c_2():
    choice_2_c_2_pick = input(choice_2_c_2)
    choice_2_c_2_options = ['1', '2', '3', '4']
    while choice_2_c_2_pick not in choice_2_c_2_options:
        choice_2_c_2_pick = input('Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ')
    if choice_2_c_2_pick == '1':
        pick_choice_2_c_2_a()
    elif choice_2_c_2_pick == '2':
        pick_choice_2_c_2_b()
    elif choice_2_c_2_pick == '3':
        pick_choice_2_c_2_c()
    elif choice_2_c_2_pick == '4':
        pick_choice_2_c()

def pick_choice_2_c_2_a(): 
    choice_2_c_2_a_pick = input(choice_2_c_2_a)
    if choice_2_c_2_a_pick != '1':
        choice_2_c_2_a_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif choice_2_c_2_a_pick == '1':
        pick_choice_2_c_2()

def pick_choice_2_c_2_b(): 
    choice_2_c_2_b_pick = input(choice_2_c_2_b)
    if choice_2_c_2_b_pick != '1':
        choice_2_c_2_b_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif choice_2_c_2_b_pick == '1':
        pick_choice_2_c_2()

def pick_choice_2_c_2_c():
    choice_2_c_2_c_pick = input(choice_2_c_2_c)
    choice_2_c_2_c_options = ['1', '2']
    while choice_2_c_2_c_pick not in choice_2_c_2_c_options:
        choice_2_c_2_c_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_2_c_2_c_pick == '1':
        if 'crowbar' in player.items:
            pick_choice_3()
        else:
            print('You push and pull and tug and stomp, but the trapdoor absolutely refuses to budge. If it had a face you imagine it would be laughing at your efforts. Maybe you need something to pry it open with... \n\n')
            choice_2_c_2_c_pick = input(choice_2_c_2_c)
    elif choice_2_c_2_c_pick == '2':
        pick_choice_2_c_2()

def pick_choice_3(): 
    choice_3_pick = input(choice_3)
    choice_3_options = ['1', '2', '3']
    while choice_3_pick not in choice_3_options:
        choice_3_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_3_pick == '1':
        pick_choice_3_a()
    elif choice_3_pick == '2':
        pick_choice_3_b()
    elif choice_3_pick == '3':
        pick_choice_2_c_2_c()

def pick_choice_3_a():
    if 'scroll' in player.items:
        print(choice_3_a_scroll)
        pick_choice_3()
    else:
        print(choice_3_a_no_scroll)
        replay()

def pick_choice_3_b(): #check for key - play again after win?
    choice_3_b_pick = input(choice_3_b)
    choice_3_b_options = ['1', '2']
    while choice_3_b_pick not in choice_3_b_options:
        choice_3_b_pick = input('Sorry, that is not a valid choice. Please select 1 or 2 to continue. ')
    if choice_3_b_pick == '1':
        if 'key' in player.items:
            print(treasure_retrieval)
            replay()
        else:
            print("Closer examination of the chest reveals a keyhole in the center of the lid. Maybe you can get it open anyways... it's been down here for ages anyways, right? You push and tug and kick and even try asking it nicely (and not so nicely) to open. Seems like they had immpecable craftsmanship back in the day. Perhaps the key was left behind somewhere in the fortress...\n\n")
            pick_choice_3_b()
    elif choice_3_b_pick == '2':
        pick_choice_3()

def pick_choice_2_c_3(): #1 choices
    choice_2_c_3_pick = input(choice_2_c_3)
    if choice_2_c_3_pick != '1':
        choice_2_c_3_pick = input('Sorry, that is not a valid choice. Please select 1 to continue. ')
    elif choice_2_c_3_pick == '1':
        pick_choice_2_c()

def replay():
    positives = ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah', 'sure', 'Sure', 'ok', 'Ok', 'yep', 'Yep']

    restart = input("\n\n\nWould you like to play again? (Y/N) ")
    if restart in positives:
        enter_the_fortress(player)
    

enter_the_fortress(player)




''' In the future, if we wanted to build out additional functionality:
- add additional rooms, etc
- and/or additional interaction within rooms - opening cupboards, looking around/under things, etc
  - maybe add a 'search' method to the adventurer class to do so?
- add more items
- add more needed keys/items/etc
- add puzzles?
- add a time limit? tracked by number of turns
  - perhaps leading to an earthquake, etc, with warnings at certain thresholds to hint at such
'''