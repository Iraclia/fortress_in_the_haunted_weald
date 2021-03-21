class Adventurer:
    def __init__(self, name, items = []):
        self.name = name
        self.items = []

    def __repr__(self):
        return 'The adventurer {0} currently has: {1} in their inventory.'.format(self.name, self.items)

    def add_item(self, item):
        self.items.append(item)

global user
user = Adventurer('Stranger')

def welcome():
    positives = ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah', 'sure', 'Sure', 'ok', 'Ok', 'yep', 'Yep']
    negatives = ['n', 'N', 'no', 'No', 'nah', 'Nah', 'nope', 'Nope']
    exit_words = ['exit', 'Exit', 'stop', 'Stop', 'end', 'End']

    print('Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, don\'t die on the way! \n')

    rule_check = input('Would you like to read the rules? (Y/N) \n')
    if rule_check in positives:
        print ('\nOkay! This is a text adventure game. As the scenes are described, you will be prompted to make choices, find items, and traverse through the rooms in search of the treasure. Type your response when promted and hit enter to continue to the next step. Have fun!')

    user_name = input('\nWhat is your name, adventurer? ')
    global user
    user = Adventurer(user_name)
    return user

# story choice text blocks:
intro = "\nYou find yourself standing deep in a dark forest. The trees soar overhead, seeming to be impossibly tall, blocking out any hint of sunlight - if indeed it is even day. The air is cool and mist seems to waft between the massive tree trunks. Does it move faster each time you look away from it? You don't really remember how you got here... huh. But you do remember what you're supposed to be doing: retrieving the treasure from an abandoned fortress in the darkest part of the Haunted Weald. No one quite knows what it is, but you know it is important that you find it. A moldering stone edifice stands before you, something built and then lost, forgotten and never returned to. Moss and creepers almost hide the structure entirely, but a door - oddly pristine amongst all the plants - stands a few paces ahead of you. Something shrieks deeper in the forest - it could be the call of a hunting cat... or maybe what is being hunted. What do you do? \n 1. Flee! No way I'm going in there! \n 2. Enter the fortress. \n"

choice_1 = "\nYou don't like the sound of the creatures out here, the darkness of the forest, or the shiftiness of the mist out of the corner of your eyes. And you -definitely- don't like the look of this creepy old fortress and its mysteriously inviting door. It doesn't matter how important this mysterious treasure is. Nope, no way. You are outta here! You take off at a run away from the fortress and hopefully back towards town. Or at least some sunlight. Unfortunately for you, whatever was shrieking deeper in the forest was not the only one of its kind. You don't even see what hits you as something drops out of the trees, and you add a shriek of your own to the forest before your world goes dark. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of the Haunted Weald. \n\nThe End.".format(user.name)

choice_2 = "enter dungeon - pick 1 - gaurd room, 2 - more hall, 3 - stairs, 4 - go back outside - return to intro"

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


def enter_the_fortress():
    intro_pick = input(intro)
    while (intro_pick != '1') and (intro_pick != '2'):
        intro_pick = input('Sorry, that is not a valid choice. Please pick 1 or 2 to continue. ')
    if intro_pick == '1':
        print(choice_1)
        return
    elif intro_pick == '2':
        choice_2_pick = input(choice_2)
    

welcome()
enter_the_fortress()