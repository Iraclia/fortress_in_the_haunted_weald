class Adventurer:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return "The adventurer {0} currently has: {1} in their inventory.".format(self.name, (self.items))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

def welcome():
    positives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "sure", "Sure", "ok", "Ok", "yep", "Yep"]

    print("Welcome to the Fortress in the Haunted Weald. Somewhere in this creepy old building is a priceless treasure - best of luck finding it, don't die on the way! \n")

    rule_check = input("Would you like to read the rules? (Y/N) \n")
    if rule_check in positives:
        print ("\nOkay! This is a text adventure game. As the scenes are described, you will be prompted to make choices, find items, and traverse through the rooms in search of the treasure. Type your response when promted and hit enter to continue to the next step. Have fun! \n\n*** Disclaimer: Lots of reading involved. :) ***")

    user_name = input("\nWhat is your name, adventurer? ")
    user_info = Adventurer(user_name)
    return user_info

#introduces game, establishes player variable for the following story blocks
player = welcome()

# story text and choice blocks for each room:
intro = "\nYou find yourself standing deep in a dark forest. The trees soar overhead, seeming to be impossibly tall, blocking out any hint of sunlight - if indeed it is even day. The air is cool and mist seems to waft between the massive tree trunks. Does it move faster each time you look away from it? You don't really remember how you got here... huh. But you do remember what you're supposed to be doing: retrieving a treasure from an abandoned fortress in the darkest part of the Haunted Weald. No one quite knows what this treasure is, but you know it is vital that you find it. A moldering stone edifice stands before you, something built and then lost, forgotten and never returned to. Moss and creepers almost hide the structure entirely, but a door - oddly pristine amongst all the plants - stands a few paces ahead of you. Something shrieks deeper in the forest - it could be the call of a hunting cat... or maybe what is being hunted. What do you do? \n"

intro_choices = "\n1. Flee! No way I'm going in there! Are you crazy?! \n2. Enter the fortress. Someone has to find the treasure, right? \n"

run_away = "\nYou don't like the sound of the creatures out here, the darkness of the forest, or the shiftiness of the mist out of the corner of your eyes. And you -definitely- don't like the look of this creepy old fortress and its inexplicably inviting door. It doesn't matter how important this mysterious treasure is. Nope, no way. You are outta here! You take off at a run away from the fortress and hopefully back towards town. Or at least some sunlight. Unfortunately for you, whatever was shrieking deeper in the forest was not the only one of its kind. You don't even see what hits you as something drops out of the trees, and you add a shriek of your own to the quiet of the forest before your world goes dark. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of the Haunted Weald. \n\nThe End.\n"

enter_fortress = "\nYou might not remember getting here, but you do know you need to find the treasure. And surely whatever is inside the fortress can't be nearly as bad as whatever that thing was. This ruin has been abandoned for centuries. Everything should be dead in there. ... Right? Before you can think too much harder about that, you urge your feet into moving and step up to the door. It swings open with the barest whisper of sound almost before you touch the handle. Ooookay, then, that's not creepy at all. You step inside and this time the door -definitely- moves without being touched, shutting firmly behind you. Well. \n\nDespite being unable to locate any flames, the inside of the fortress is dimly lit with subtly shifting light. Dark shadows gather in the corners, more thickly than it seems like shadows should. You eye them uncertainly, but nothing lunges forth. All the same, each time you glance away you feel sure something moved just barely out of your line of sight. But the sourceless illumination reveals your surroundings well enough. A sturdy wooden door stands to your left, hanging slightly ajar, though it shows nothing of the room beyond. The corridor you stand in, wide enough for three men to walk abreast, stretches further off into the fortress ahead of you. To your right is a short hallway following the exterior wall of the fortress. By the deepening shadows at the end, it looks like it might lead to a staircase. What do you do? \n" 

enter_fortress_choices = "\n1. Enter the door. You can't quite see what is in the room beyond, and there's only one way to find out. \n2. Continue down the hallway. Maybe it's a good idea to see what else is in here. \n3. Investigate the hallway. You might lose your nerve if you don't tackle looking in the darkest shadows first. \n4. Maybe this was a bad idea... go back outside. \n"

guard_room = "\nYou decide to have a look through the door. You ease up to it, reaching out to push the door slowly open. This time the door does nothing to help you out - it takes more muscle than you thought it might before the door grinds reluctantly open with a raspy scrape of wood over stone. Having decided nothing is going to jump out of the shadows at you, you step further into the room to have a look around. The square room is rather unremarkable all in all. A thin layer of dust softens the stone floor and coats the few items left in the room. Against the back wall a spindly cot has collapsed in upon itself. A couple of stools are gathered around a low table to your left. The table still holds a pitcher and a few wooden cups. One stool has been knocked over and never picked up. To your right you see a weapons rack bolted onto the wall - empty now of the spears it probably held. It looks like maybe this was the guard's room. Not much to see here. As you start to turn back to the door, a faint metallic gleam catches your eye in the corner near the weapons rack. Huh. Looks like a crowbar.What do you do? \n" 

guard_room_choices = "\n1. Grab the crowbar before you head back into the corridor. You never know when that might come in handy. \n2. Leave the room and don't disturb the dust. Who knows what spirits might be attached to that crowbar. \n"

round_hall = "\nYou head down the corridor and deeper into the dim fortress. The stone is pitted and seems to be crumbling to sand in patches. It's almost as if the fortess is slowly rotting away from the inside out. The shiftiness of the dim light and the shadows you would swear won't quite stay still make give a surreal cast to the passage. Maybe this is all a dream. Why are you here getting this treasure anyways? Who is it important to? Questions for afterwards, perhaps. The hallway dumps you out into an expansive, round room. An arched ceiling soars overhead, delicate, twisting columns supporting its weight evenly spaced in a ring a few paces from the wall. Behind the columns there seem to be traces of color on the walls, but whatever art adorned them has long since slid into obscurity with the passage of time. As you walk further in, you notice a domed skylight in the very center - the glass remarkably intact despite the crumbliness of the fortress otherwise. In better times, perhaps sunlight would have streamed through in a solid column, illuminating the swirling mosaic reaching out from the center of the room. Now, though, no light falls through the glass, only the murk of the Weald. Faint motes of dust float in the air like spirits of the once-residents, stirred to a half-life again by the passage of your steps. The quiet begs not to be disturbed in this space and even your breathing seems too loud. \n\nTo your left is an elaborate doorway, stone foliage so realistic you expect it to move decorating the frame of it in vines, leaves and fragile flowers. The overlarge doors are pushed open already, and you can just make out bits of something in the room. Ahead of you in an equally large doorway, though this one is more restrained in its elegance, subtle curves and swirls of stone making the frame of the door appear to loom larger. You can see glints of gilding where it still stubbornly clings to a few patches of stone. One door stands closed, the other seems to have fallen off its hinges and into the room beyond. To your right is a more normal sized doorway, its frame in keeping with the elegance of the space, but nothing to compare with the other two. What do you do? \n" 

round_hall_choices = "\n1. Head to the left. That otherworldly carving begs a closer look. What might be in a room with a door like that? \n2. Go straight across the round room. That looks like a grand doorway, with gold on it no less. Maybe it leads to the treasure room? \n3. Turn right. Sometimes the most interesting things are behind the most unassuming doors. Isn't that how that saying goes? \n4. Return to the hallway behind you. Maybe a different route would be best. \n"

shrine = "\nYou set your steps towards the flowering doorway, trying not to tread too heavily on the way. The closer you get to the doorway, the more convinced you are that those carvings couldn't possibly be stone. They are as thin as real plants, each miniscule detail, each pore on the leaves, each thorn on the roses included. You reach out to touch it, but hesitate. Maybe some mysteries are best left unsolved. If it crumbled beneath your fingers the world would have lost an bit of artistry unlike any other. Once you can tear your eyes away from the flowers, you step through the pale doors, crafted of some wood so pale as to be almost white. The room beyond seems... lighter. Those ever-present darker-than-normal shadows seem to avoid this space. The floor is as pale as the doors, and the dust seems lighter here. The high ceilings above are... are glass again. This time in varying dark hues that seem random until you notice a subtle pattern running through it - one that seems to change each time your attention shifts. You can imagine how stunning it might have been under the sun. Now, as in the previous room, all is dark and dim. \n\nYour attention shifts to the end of the long room and there, standing larger than life size in an alcove is a woman. Or at least the statue of one. But the sculptor must have been the same one who carved the doorway, as you can almost imagine her robes rustling in an unfelt breeze. Her hair seems to float weightlessly around her shoulders. Any moment now she ought to open her eyes and ask who disturbs her final slumber. You move closer until you find yourself standing a scant pace from her. The white marble seems faintly... luminescent. Or maybe it is your imagination. One hand is tucked to her chest, but the other reaches out towards you, a black key loosely clasped in it. She is stunningly beautiful. And almost as eerie. That feeling that she might awaken returns stronger than ever. You feel like you don't belong here. What do you do? \n"

#maybe make it so that you have to trade her an item for the key - based on a riddle/inscription

shrine_choices = "\n1. Take the key before you go. It looks like it could be important. \n2. You decide you should probably leave the key where it is and head back to the round hall. \n"

reception_room = "\nThe huge scale of the doorway ahead of you must mean it's an important room. An important room for an important treasure, you hope? Stepping softly, you creep across the round hall, approaching the half-opened doors. The glint of gold that caught your eye from further away is patterned with silver, gone dark with tarnish, and copper, now a deep green. It must have shone wonderfully when it was kept up, though. The iron bound doors look impressively sturdy, upright or not. You have to wonder how only one of the things came crashing down - what a sound that would have made. Does it... look like it was struck in the middle? You decide not to ponder that for too long and step over the door into the room. It is an imposing space indeed - the ceiling is high, and the space wide... and mostly empty. As you head further into the room, you seem a raised dais. But nothing more. Whatever once graced it is gone. Hopefully it wasn't the treasure you are seeking... The shadows seem darker in this end of the room, creeping further away from the walls and corners, stretching imperceptibly towards that low platform. You shiver and think it might be best to go. What do you do? \n"

reception_room_choices = "\n1. That wasn't nearly as treasure-filled as you had hoped. You glance back at the shadows to make sure they stay put before you head back to the round hall. \n"

room_to_stairs = "\nAlthough the other oversized doors are impressive in their grandeur, it would probably make more sense to hide a treasure somewhere less conspicuous. You carefully leave behind the hushed silence of the round hall, heading to the right and stepping through the more human-sized doorway. What awaits you is not a treasure, sadly. In fact, contrary to your high hopes, this room seems to live up to its door in every way. It is square, bare, and almost entirely uninteresting. Except for the fact that on the opposite side of the room there is the beginning of a set of stairs heading downwards, shrouded in shadows that seem to be untouched by the uncanny illumination of the fortress. Hm. What do you do?\n"

room_to_stairs_choices = "\n1. You're not very fond of the look of those shadows. But you take a breath and steel yourself before starting towards the stairs. \n2. The shadows in the fortress do seem restless and unbound by the usual laws of light and shadow... maybe you won't mess with these ones. Go back to the round hall.\n"

lower_corridor = "\nYou hesitate at the top of the stairs. Now that you are closer to them, the dark shadows really -do- seem to have substance to them. It... it is probably just your imagination. But you think you might have just seen that one breathe. Shadows, you are certain, should not breathe. It takes another second before you rally your flagging nerves and take the first step down, trying to avoid both sides of the corridor, but especially that much too alive shadow. You start down at a slow creep, trying not to disturb the cloying shadows. It feels like they have... substance. Thin, wafting, not much more than mist substance. But substance all the same... \n\nYou bolt down the last handful of steps, bursting out of the shadows and into a corridor. You'd swear something touched your back, but a searching glimpse reveals... stairs. And shadows. But nothing more. You notice there is another set of stairs, equally crowded with overly-present shadows, across from the first and you do your level best to watch them both at once, holding your breath and trying to decide what you would do if something actually -did- come out at you. It is a few moments more before you pull your eyes away from the shadows to the corridor before you. \n\nTo your right is a metal door. Some sort of symbol you don't recognize is carved into the center of it - sharp an angular. Despite the imposing look of the slab of metal, you don't see a lock to keep people out. To your left is a far more unassuming door, standing hald opened. You think you see the back of a chair through the opening. Ahead of you, the corridor continues. The shadows you noticed in the floor above seem a bit more populous here. Their color darker, and they are undoubtedly unsettled. You still can't seem to catch them moving, but they seem... restless. What do you do? \n"

lower_corridor_choices = "\n1. Even if there isn't a lock, a metal door seems sturdy enough to protect a teasure. Maybe you'll check that one out. Head to the right. \n2. Shifty shadows or no, you decide to head further down to corridor to see what else is here. \n3. Go left and check out the plain looking door. \n4. Head upstairs by the right staircase. Try not to let those shadows grab you again! \n5. Head up the left staircase. Preferably quickly. \n"

library = "\nYou step up towards the metal door. Up close, it still looks remarkably intact. There isn't any rust or dust to be seen on it. That strange symbol in the center looks like it has been chiseled into the metal by a steady if not expert hand. You kind of hope that's not a magic sigil set to blow someone up. You decide that would probably be too mean, even for whoever lived in this fortress. Though... you glance briefly back to the stairs with the far-too-tangible shadows. Maybe not. You take a deep breath... and push the door open. No explosions, that's good at least. The room beyond is even dimmer than the hallway you just left. But you can make out rows and rows of shelves, stuffed full of scrolls, books and stacks of loose paper. A library perhaps? You creep past the rows, seeing more of the same down each one. As empty as the rest of the fortress is, it seems like no one has touched the library since it was abandoned. A shimmer of something bright catches your eye in the last row. You hesitate a moment before stepping closer to see what it is. A small scroll, not much longer than your hand, is sitting in a rare empty space on a shelf just below eye level. It seems to gleam with a light of its own, a bubble of air around it shimmering faintly. Tied shut with a blue ribbon, there is also a tiny scrap of paper tucked under it with '{0}' written in flowing script. That... that is unusual. You swallow hard and glance left and right. You are pretty sure there is no one else in here; you would have heard them in this eerie quiet, right? Unless it was one of those shadows... But why is your name on this scroll? What do you do? \n"

library_choices = "\n1. You don't know who left it there or why, but the scroll does have your name on it. You hesitate, but take the scroll before heading back into the corridor. \n2. You don't think any good can come of a scroll left for you in this place. What if it's a curse? With a last glance around, you return to the corridor. \n"

lower_hall = "\nYou head further down the corridor. You steps crunch slightly over bits of stone and rubble scattered through the dust on the floor. The stone down here seems to have suffered a bit more heavily from the passage of age that that of the floor above. Or perhaps it was never as nice to begin with. The corridor empties into a large hall, though this one is rather utilitarian in its design. A few thick, square columns support the roof. The floor is covered with large flagstones, but no artistic flourishes lighten the space. You glance up. The cieling is higher than the corridor, though it certainly doesn't reach the lofty heights you saw upstairs. And it looks like the shadows have taken up residence here, too. Like bats, they scatter over the ceiling, too shifty to be natural. If you hold your breath you think you can almost hear them moving... A shiver runs up your spine and you look away. Maybe they will just be content to leave you be. To your left you see a wooden door standing half open. The room beyond seems rather dark. Ahead is a double-wide opening into another space. And further off to the right you can just see a third door past one of the columns, iron bound and closed tight. What do you do? \n"

lower_hall_choices = "\n1. Head left. Best to see what's through that door since it's already open, right? \n2. Move through the doorway ahead. Maybe there will be less shadows in an open space at least. \n3. Go right. You can't quite avoid the temptation of a closed door. Maybe you'll finally happen upon the treasure. \n4. Head back down the corridor. \n"

barracks = "\nYou head towards the half-open door. It looks sturdy - thick wood bound with iron - but when you push on the door it swings easily open on hinges still silent. You step into the room, and it seems... muffled. Not that there is a lot of sound down in the depths of the fortress, but your steps don't seem as loud in here. There isn't too much to see, though. A lot of tumbled lengths of wood and cloth, mostly. One cot is still standing tremulously under its own weight to the right, and gives you a hint to where you might be. This must have been the barracks once upon a time. You glance to the left and straighten up at the sight of a chest. Could the treasure really be just sitting out on the floor?! You dash down to the chest and tug the lid up. You let out a starteled yell as something black and shadowy explodes out of the chest and straight up into your face. For a second it feels as if you have been dipped in icy water before your vision clears and the sensation fades. You stand frozen where you stumbled back from the chest. Was that... one of the shadows? Does it look like there's one more of the things haunting the walls in here? You scrub a hand over your face trying to forget the sensation of it against your skin. Glancing down you see that the chest - without its shadow - is woefully empty.What do you do? \n"

barracks_choices = "\n1. With a last brush of your face you head back into the hall, keeping an eye out for any more shifty shadows. \n"

mess_hall = "\nYou stride across the hall and towards the open doorway. You feel more confident stepping into a space you can see. With no doors to bar the way, you catch sight of a few rows of long tables as your near. It looks like you have found the mess hall. Low benches are tucked under the tables, though a couple nearest the door have been upset and left lying where they fell. The tables are empty, though, save of a healthy (or not so healthy) layer of dust. There's another door in the far corner - probably the kitchen? The blackness through that doorway seems to be infinite and untouched by the sourceless light of the rest of the fortress. You decide that might be one mystery you don't need to investigate. What do you do? \n"

mess_hall_choices = "\n1. Go back to the lower hall.\n"

#add a sudden death for the kitchen here

trapdoor_room = "\nYou head past the sturdy columns towards the closed door at the far end of the hall. You can't help but glance up now and again as you walk - there is a faint, skittery stirring to the shadows clinging to the ceiling as you get closer to the door. Each time you glance up it seems as if they are crowded more thickly above you... as long as they stay up there. You hope fervently that they do. Luck seems to be on your side, though. Despite the faint noises of them following you, they do seem to have stayed on the ceiling. You glance up one last time before reaching out to try the door. The handle turns, but the door seems to be stuck. You push against it and it slides a reluctant half inch. Another shove convinces it to move an additional quarter of an inch. Great. You take a step back and throw your weight into the wooden barrier and it gives way in a split second, rebounding back against the stone with a ~BANG~ that echoes through the fortress, even as you do an exceedingly elegant almost-faceplant into the floor. \n\nIt doesn't take you long to spring back to your feet, though, gaze fixed on the door your just fell through. More than your newly bruised knees, you worry about the resounding echo still fading too slowly as it reverberates through the stone rooms and halls. And with it comes a no longer subtle skittering of... something... shadows? ... moving through the fortress. You hold your breath, but nothing appears. After the longest few seconds of your life, the sound grows quieter and disappears. It's another minute before you dare to move. Maybe you should hurry up and find the treasure. You thought it would be safer in here than out in the Haunted Weald... but you are less certain of that now. You glance quickly around the room, at first thinking you had risked all that for nothing more than a small, bare chamber. But then you see the trapdoor. Similar to the door, the solid wood is iron bound and set into the very center of the square room. Probably a good place to hide a treasure, right? What do you do? \n"

trapdoor_room_choices = "\n1. You came here looking for a treasure right? So why don't we see what's down there. Open the trapdoor. \n2. After whatever that skittering was, maybe you're not quite ready to head any deeper into this creepy fortress... go back to the lower hall.\n"

base_of_ladder = "\nWhile you are glad to have gotten the door open, your heart almost leaps into your chest at the sound it came with. You decide it is best not to wait and see if the skittering returns, perhaps with something unpleasant to follow, and hurry through the trapdoor. You find a ladder, which creaks alarmingly under your weight, although it seems to be intact, and you quickly make your way down... and down... and down it. You drop to a stone floor, relieved it actually had an end. A glance back up the ladder shows nothing following you down... that's good at least. The odd illumination of the fortress seems to extend down here - if anything it is a little brighter, a cool blue hue suffusing what you see is a stone tunnel. You don't seem to be in the fortress itself anymore, but instead in a path burrowed into the natural stone itself. The tunnel extends in either direction, but you can't see anything other than stone all around you. What do you do? \n"

base_of_ladder_choices = "\n1. With a mental flip of a coin, you decide to head left. It seems as good a direction as the other. \n2. You glance one way and then the other. Why not right? Head that way. \n3. Hm. Deep dark tunnels under an abandoned fortress? Maybe not. Head back up the ladder.\n"

sudden_death_scroll = "\nYou start left down the tunnel. It seems pretty unremarkable for the most part - more stone, the uneven walls of the tunnel unrelieved by any openings or doors. The soft crunch of dirt and grit under your boots accompanied your steps. And then - a crack. You pause. It almost sounds like that first step you take onto lake ice when it isn't quite frozen enough to support your weight. You start to ease your weight back... and then there is another crack. And another. Before you have time to retreat any further, the stone of the floor gives way entirely with the clattering of stone falling against stone and a huge splash as it falls into a rushing underground river scant feet below you. You stare down at the river... finding yourself, improbably, floating mid-air above the gaping hole in the tunnel floor. You drift back over stable stone, before whatever it was drops you back to the ground. And you promptly feel a burning sensation in your pocket which makes you jump before you rapidly fish out the small scroll you picked up earlier... charring into ash before your eyes. You try not to think too hard about what might have happened if you hadn't picked that up... You glance once more into the rushing waters below before you hurry back towards the ladder."

sudden_death_no_scroll = "\nYou start left down the tunnel. It seems pretty unremarkable for the most part - more stone, the uneven walls of the tunnel unrelieved by any openings or doors. The soft crunch of dirt and grit under your boots accompanied your steps. And then - a crack. You pause. It almost sounds like that first step you take onto lake ice when it isn't quite frozen enough to support your weight. You start to ease your weight back... and then there is another crack. And another. Before you have time to retreat any further, the stone of the floor gives way entirely with the clattering of stone falling against stone and a huge splash as it - and you - fall into a rushing underground river running scant feet below the tunnel. You are sucked down below the stone with the waters of the river, but no matter how hard you scrabble to escape the waters, it seems like there is no more air to be found in the dark, watery path. \n\nSadly, there is one less {0} in the world. But it seems unlikely anyone will ever find your unmarked grave in the depths of this underwater river. \n\nThe End. \n"

treasure_room = "\nYou head right down the stone tunnel. For a while there is little to see aside from more stone. Eventually, though, the blue light seems to intensify as you pass twists and turns. With no warning, you are dumped out into a massive cavern. You stop two steps in to stare. The whole cave is covered in shimmering crystals, which seem to be the source of the blue light illuminating the space. The cave is bigger than any of the halls you found in the fortress above, and you can't quite tell how far back it goes... it seems to be a ways. The walls are studded with perfectly shaped crystals, but the most fantastic elements are the sweeping formations of what would have been stone in any other cave and instead here are cast in  beautiful, glittering crystal. Staggeringly large stalactites, elegant ribbon formations, sparkling columns. It's stunning. It's almost enough to distract you from what else is in the room: a chest that would be large anywhere else but it small in comparison to the rest of the cave. Could this finally be the treasure you were sent here for? You head towards the chest, trying not to be distracted by the sights around you. What do you do? \n"

treasure_room_choices = "\n1. Finally! Time to get the treasure and get out of this creepy fortress! Open the chest. \n2. Head back to the base of the ladder. \n"

study_room = "\nYou turn your attention to the left and head to the door there. The darkness of the room beyond makes you hesitate a moment before you ease through the half-open wooden door. Like elsewhere in the fortress, the dust has gathered across the surfaces. In this case... a series of small tables. Huh. You take another step forward and a single candle sitting on the central table springs to life, making you blink and throw up a hand at the sudden gleam of the first real light you have seen since entering the fortress. You drop your hand after a moment, glancing around the room. The omnipresent shadows seem smaller here, in the flickering light of the candle. Unfortunately it doesn't reveal anything more in the room than you could already see. Small tables, each with their own chair. A quill lies abandoned on the furthest one, but other than that... more dust. What do you do? \n"

#add a trying to take the candle route

study_room_choices = "\n1. Well, nothing to see here. Head back into the corridor.\n"

treasure_retrieval = "\nAs you get closer to the chest, you notice that there is a keyhole in the center of the lid. It is oddly similar to something you have seen before... in fact. You pull out the key that was held in the hand of the goddess, and see that the black stone is identical. You fit the key into the lock and turn it. With a gentle click the lid of the chest pops open. Finally! You push the lid open and see... \n\n ...and see a lunchbox. What? Surely this can't be the treasure. And what in the world is a lunchbox doing here of all places? You hesitantly reach down and pick it up. The metal lunchbox is decorated with cartoon super heroes. The bright colors are the most brilliant things you have seen since finding yourself in the forest. You open the lid and see a handwritten note on top of what appears to be a neatly packed lunch. You can't help but notice that the handwriting is the same as that on the scroll you found...\n\n      'My dearest love, \n       I hope that you managed to survive the forest, the kitchen (don't touch my pots again), and the pit (I warned you not to dig yourself too deep). Here's your lunch. I didn't poison anything, though you a little upset stomach probably would be well deserved. \n                Love, \n                Your most beautiful, astounding, patient wife <3' \n\nAs you stare at the note, the glimmering cave around you fades away. It is replaced with a far less resplendent, but far more familiar kitchen. You are standing in front of the open refridgerator holding your lunchbox. Memories are quick to resurface. You had an argument with your wife last night. It definitely started with the dishes (it was hard to remember which pots were the non-stick pots...) and disintegrated from there. Everyone tried to warn you marrying a witch would come with its unique trials... but. At least you survived this time. And you still got lunch! You'd better not touch the pots again, though, if you expect to survive the next argument... \n\n The End. \n"

"produce key - open chest - ta-da! you did it! - don't forget your lunch, if you survived. love your wife - knew marrying a witch was risky - find yourself in the kitchen at the fridge"


def begin_adventuring(player):
    print(intro)
    print(player.__repr__())
    intro_pick = input(intro_choices)
    intro_options = ["1", "2"]
    while intro_pick not in intro_options:
        intro_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if intro_pick == "1":
        print(run_away.format(player.name))
        replay()
    elif intro_pick == "2":
        pick_enter_fortress()

def pick_enter_fortress():
    print(enter_fortress)
    print(player.__repr__())
    enter_fortress_pick = input(enter_fortress_choices)
    enter_fortress_options = ["1", "2", "3", "4"]
    while enter_fortress_pick not in enter_fortress_options:
        enter_fortress_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ")
    if enter_fortress_pick == "1":
        pick_guard_room()
    elif enter_fortress_pick == "2":
        pick_round_hall()
    elif enter_fortress_pick == "3":
        pick_lower_corridor()
    elif enter_fortress_pick == "4":
        begin_adventuring(player)
    
def pick_guard_room():
    print(guard_room)
    print(player.__repr__())
    guard_room_pick = input(guard_room_choices)
    guard_room_options = ["1", "2"]
    while guard_room_pick not in guard_room_options:
        guard_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if guard_room_pick == "1":
        player.add_item("crowbar")
        pick_enter_fortress()
    elif guard_room_pick == "2":
        pick_enter_fortress()

def pick_round_hall():
    print(round_hall)
    print(player.__repr__())
    round_hall_pick = input(round_hall_choices)
    round_hall_options = ["1", "2", "3", "4"]
    while round_hall_pick not in round_hall_options:
        round_hall_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ")
    if round_hall_pick == "1":
        pick_shrine()
    elif round_hall_pick == "2":
        pick_reception_room()
    elif round_hall_pick == "3":
        pick_room_to_stairs()
    elif round_hall_pick == "4":
        pick_enter_fortress()

def pick_shrine():
    print(shrine)
    print(player.__repr__())
    shrine_pick = input(shrine_choices)
    shrine_options = ["1", "2"]
    while shrine_pick not in shrine_options:
        shrine_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if shrine_pick == "1":
        player.add_item("key")
        print("\nHesitantly, with your attention half on the woman's face in case those pale eyes -do- open, you reach out to take the key. It seems to resist just a moment before slipping free of her stone fingers. You beat a hasty retreat out of the statue's field of vision and into the round hall again before you take a breath.\n")
        pick_round_hall()
    elif shrine_pick == "2":
        pick_round_hall()

def pick_reception_room():
    print(reception_room)
    print(player.__repr__())
    reception_room_pick = input(reception_room_choices)
    if reception_room_pick != "1":
        reception_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ")
    elif reception_room_pick == "1":
        pick_round_hall()

def pick_room_to_stairs():
    print(room_to_stairs)
    print(player.__repr__())
    room_to_stairs_pick = input(room_to_stairs_choices)
    room_to_stairs_options = ["1", "2"]
    while room_to_stairs_pick not in room_to_stairs_options:
        room_to_stairs_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if room_to_stairs_pick == "1":
        pick_lower_corridor()
    elif room_to_stairs_pick == "2":
        pick_round_hall()

def pick_lower_corridor():
    print(lower_corridor)
    print(player.__repr__())
    lower_corridor_pick = input(lower_corridor_choices)
    lower_corridor_options = ["1", "2", "3", "4", "5"]
    while lower_corridor_pick not in lower_corridor_options:
        lower_corridor_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3, 4 or 5 to continue. ")
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
    print(library.format(player.name))
    print(player.__repr__())
    library_pick = input(library_choices)
    library_options = ["1", "2"]
    while library_pick not in library_options:
        library_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if library_pick == "1":
        player.add_item("scroll")
        pick_lower_corridor()
    elif library_pick == "2":
        pick_lower_corridor()

def pick_lower_hall():
    print(lower_hall)
    print(player.__repr__())
    lower_hall_pick = input(lower_hall_choices)
    lower_hall_options = ["1", "2", "3", "4"]
    while lower_hall_pick not in lower_hall_options:
        lower_hall_pick = input("Sorry, that is not a valid choice. Please select 1, 2, 3 or 4 to continue. ")
    if lower_hall_pick == "1":
        pick_barracks()
    elif lower_hall_pick == "2":
        pick_mess_hall()
    elif lower_hall_pick == "3":
        pick_trapdoor_room()
    elif lower_hall_pick == "4":
        pick_lower_corridor()

def pick_barracks(): 
    print(barracks)
    print(player.__repr__())
    barracks_pick = input(barracks_choices)
    if barracks_pick != "1":
        barracks_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ")
    elif barracks_pick == "1":
        pick_lower_hall()

def pick_mess_hall(): 
    print(mess_hall)
    print(player.__repr__())
    mess_hall_pick = input(mess_hall_choices)
    if mess_hall_pick != "1":
        mess_hall_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ")
    elif mess_hall_pick == "1":
        pick_lower_hall()

def pick_trapdoor_room():
    print(trapdoor_room)
    print(player.__repr__())
    trapdoor_room_pick = input(trapdoor_room_choices)
    trapdoor_room_options = ["1", "2"]
    while trapdoor_room_pick not in trapdoor_room_options:
        trapdoor_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if trapdoor_room_pick == "1":
        if "crowbar" in player.items:
            print("The trapdoor is stubbornly wedged in place - age doesn't seem to have weakened the wood. If anything it has made the thing more difficult to get through. Luckily, you came prepared. You pull out the crowbar you found upstairs and throw your weight into prying the door open. The trapdoor resists, before it slowly starts to shift with an audible groan of protest. Then, with a thunderous snap and the sharp clatter of metal on stone, the door pops open. Your trusty crowbar, sadly, gave its life for the task. It didn't seem to have aged as well as the trapdoor itself.")
            player.remove_item("crowbar")
            pick_base_of_ladder()
        else:
            print("You push and pull and tug and stomp; you even try politely, and not so politely, asking the thing to open. But the trapdoor absolutely refuses to budge. If it had a face you imagine it would be laughing at your efforts. Maybe you need something to pry it open with... \n\n")
            pick_trapdoor_room()
    elif trapdoor_room_pick == "2":
        pick_lower_hall()

def pick_base_of_ladder(): 
    print(base_of_ladder)
    print(player.__repr__())
    base_of_ladder_pick = input(base_of_ladder_choices)
    base_of_ladder_options = ["1", "2", "3"]
    while base_of_ladder_pick not in base_of_ladder_options:
        base_of_ladder_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if base_of_ladder_pick == "1":
        pick_sudden_death()
    elif base_of_ladder_pick == "2":
        pick_treasure_room()
    elif base_of_ladder_pick == "3":
        pick_trapdoor_room()

def pick_sudden_death():
    if "scroll" in player.items:
        print(sudden_death_scroll)
        player.remove_item("scroll")
        pick_base_of_ladder()
    else:
        print(sudden_death_no_scroll.format(player.name))
        replay()

def pick_treasure_room(): 
    print(treasure_room)
    print(player.__repr__())
    treasure_room_pick = input(treasure_room_choices)
    treasure_room_options = ["1", "2"]
    while treasure_room_pick not in treasure_room_options:
        treasure_room_pick = input("Sorry, that is not a valid choice. Please select 1 or 2 to continue. ")
    if treasure_room_pick == "1":
        if "key" in player.items:
            print(treasure_retrieval)
            player.remove_item("key")
            replay()
        else:
            print("Closer examination of the chest reveals a keyhole in the center of the lid. Maybe you can get it open anyways... it's been down here for ages anyways, right? You push and tug and kick and even try asking it nicely (and not so nicely) to open. Seems like they had immpecable craftsmanship back in the day. Perhaps the key was left behind somewhere in the fortress...\n\n")
            pick_treasure_room()
    elif treasure_room_pick == "2":
        pick_base_of_ladder()

def pick_study_room(): 
    print(study_room)
    print(player.__repr__())
    study_room_pick = input(study_room_choices)
    if study_room_pick != "1":
        study_room_pick = input("Sorry, that is not a valid choice. Please select 1 to continue. ")
    elif study_room_pick == "1":
        pick_lower_corridor()

def replay():
    positives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "sure", "Sure", "ok", "Ok", "yep", "Yep"]

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
- add more ways to die/lose
- add puzzles?
- add a time limit? tracked by number of turns
  - perhaps leading to an earthquake, etc, with warnings at certain thresholds to hint at such

- perhaps you could change the story write-up so that when you revisit a room you get a paired down version of a story? add a list functionality to track rooms visited, if a room visited before use an alternative text?
- perhaps add random endings? write up a few different endings, choose random number to pick which one you get
- add an easter egg ^^
'''