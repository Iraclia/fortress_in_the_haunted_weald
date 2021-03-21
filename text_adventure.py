class Adventurer:
    def __init__(self, name, items = []):
        self.name = name
        self.items = []

    def __repr__(self):
        return 'The adventurer {0} currently has: {1} in their inventory.'.format(self.name, self.items)

    def add_item(self, item):
        self.items.append(item)

def welcome():
    positives = ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah', 'sure', 'Sure', 'ok', 'Ok', 'yep', 'Yep']
    negatives = ['n', 'N', 'no', 'No', 'nah', 'Nah', 'nope', 'Nope']
    exit_words = ['exit', 'Exit', 'stop', 'Stop', 'end', 'End']

    print('Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, don\'t die on the way! \n')

    rule_check = input('Would you like to read the rules? (Y/N) \n')
    if rule_check in positives:
        print ('\nOkay! This is a text adventure game. As the scenes are described, you will be prompted to make choices, find items, and traverse through the rooms in search of the treasure. Type your response when promted and hit enter to continue to the next step. Have fun!')

    user_name = input('\nWhat is your name, adventurer? ')
    user_info = Adventurer(user_name)
    return user_info

player = welcome()

# story choice text blocks:
intro = "\nYou find yourself standing deep in a dark forest. The trees soar overhead, seeming to be impossibly tall, blocking out any hint of sunlight - if indeed it is even day. The air is cool and mist seems to waft between the massive tree trunks. Does it move faster each time you look away from it? You don't really remember how you got here... huh. But you do remember what you're supposed to be doing: retrieving a treasure from an abandoned fortress in the darkest part of the Haunted Weald. No one quite knows what this treasure is, but you know it is vital that you find it. A moldering stone edifice stands before you, something built and then lost, forgotten and never returned to. Moss and creepers almost hide the structure entirely, but a door - oddly pristine amongst all the plants - stands a few paces ahead of you. Something shrieks deeper in the forest - it could be the call of a hunting cat... or maybe what is being hunted. What do you do? \n\n" + player.__repr__() + "\n\n1. Flee! No way I'm going in there! \n2. Enter the fortress. \n"

choice_1 = "\nYou don't like the sound of the creatures out here, the darkness of the forest, or the shiftiness of the mist out of the corner of your eyes. And you -definitely- don't like the look of this creepy old fortress and its inexplicably inviting door. It doesn't matter how important this mysterious treasure is. Nope, no way. You are outta here! You take off at a run away from the fortress and hopefully back towards town. Or at least some sunlight. Unfortunately for you, whatever was shrieking deeper in the forest was not the only one of its kind. You don't even see what hits you as something drops out of the trees, and you add a shriek of your own to the quiet of the forest before your world goes dark. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of the Haunted Weald. \n\nThe End."

choice_2 = "\nYou might not remember getting here, but you do know you need to find the treasure. And surely whatever is inside the fortress can't be nearly as bad as whatever that thing was. This ruin has been abandoned for centuries. Everything should be dead in there. ... Right? Before you can think too much harder about that, you urge your feet into moving and step up to the door. It swings open with the barest whisper of sound almost before you touch the handle. Ooookay, then, that's not creepy at all. You step inside and this time the door -definitely- moves without being touched, shutting firmly behind you. Well. \nDespite being unable to locate any flames, the inside of the fortress is dimly lit with subtly shifting light. Dark shadows gather in the corners, more thickly than it seems like shadows should. You eye them uncertainly, but nothing lunges forth. All the same, each time you glance away you feel sure something moved just barely out of your line of sight. But the sourceless illumination reveals your surroundings well enough. A sturdy wooden door stands to your left, hanging slightly ajar, though it shows nothing of the room beyond. The corridor you stand in, wide enough for three men to walk abreast, stretches further off into the fortress ahead of you. To your right is a short hallway following the exterior wall of the fortress. By the deepening shadows at the end, it looks like it might lead to a staircase. What do you do? \n\n" + player.__repr__() + "\n\n1. Enter the door. \n2. Continue down the hallway. \n3. Investigate the stairs. \n4. Maybe this was a bad idea... go back outside. \n"

choice_2_a = "left door to guard room - crowbar in corner, take crowbar, pick 1 - return to hall - choice 2"

choice_2_b = "straight down the hall - pick 1 - shrine, 2 - larder, 3 - empty room, 4 - back down hall - return to choice 2"

choice_2_b_1 = "left to shrine - statue holding key for treasure chest - pick up key - pick 1 - return to big room choice 2_b"

choice_2_b_2 = "straight to larder, pick 1 - return to big room choice 2_b"

choice_2_b_3 = "right to empty room, pick 1 - creepy stairs down - use choice 2_c, 2 - back to big room - return to choice 2_b"

choice_2_c = "right to creepy stairs down to downstairs hall - pick 1 - library, 2 - straight along downstairs hall, 3 - room with tables, 4 - back up stairs to choice 2"

choice_2_c_1 = "library with sparkly scroll - collect scroll - pick 1 - back to hall - return to 2_c"

choice_2_c_2 = "downstairs hall - pick 1 - barracks, 2 - mess hall, 3 - empty room w/ trapdoor, 4 - back to beginning of hall choice 2_c"

choice_2_c_2_a = "barracks - pick 1 - back to choice 2_c_2"

choice_2_c_2_b = "mess hall - pick 1 - back to choice 2_c_2"

choice_2_c_2_c = "empty room w/ trapdoor - needs crowbar from guard room to open - pick 1 - trapdoor - choice 3, 2 - back to hall, return to choice 2_c_2"

choice_3 = "ladder down to lower tunnel - pick 1 - left to sudden death, 2 - right to glowy cave, 3 - back up ladder - return to choice 2_c_2_c"

choice_3_a = "sudden death - floor gives way, drown in underground river - unless have sparkly scroll from library, levitates you back to choice 3"

choice_3_b = "retrieve the treasure - only if you have key from shrine"

choice_2_c_3 = "room with tables, pick 1 - back to hall, return to choice 2_c"


def enter_the_fortress(player):
    intro_pick = input(intro)
    intro_pick_options = ['1', '2']
    while intro_pick not in intro_pick_options:
        intro_pick = input('Sorry, that is not a valid choice. Please pick 1 or 2 to continue. ')
    if intro_pick == '1':
        print(choice_1.format(player.name))
        return
    elif intro_pick == '2':
        pick_choice_2()

def pick_choice_2():
    choice_2_pick = input(choice_2)
    choice_2_options = ['1', '2', '3', '4']
    while choice_2_pick not in choice_2_options:
        choice_2_pick = input('Sorry, that is not a valid choice. Please pick 1, 2, 3 or 4 to continue. ')
    if choice_2_pick == '1':
        pick_choice_2_a()
    if choice_2_pick == '2':
        pick_choice_2_b()
    if choice_2_pick == '3':
        pick_choice_2_c
    if choice_2_pick == '4':
        enter_the_fortress(player)
    
def pick_choice_2_a():
    pass

def pick_choice_2_b():
    pass

def pick_choice_2_c():
    pass


enter_the_fortress(player)