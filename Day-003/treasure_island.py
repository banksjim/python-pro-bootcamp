# pylint: disable=C0103, W1401
#
lose_game: bool = False
decision:  str = ""

opening_graphic: str = r"""
*******************************************************************

Welcome to...
 _                                       _     _                 _ 
| |                                     (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___   _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \   / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/   \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|  _|___/_|\__,_|_| |_|\__,_|

*******************************************************************                     
"""

print(f"{opening_graphic}\n")
print("Your objective in Treasure Island is to find the treasure.\n")

print("You've stumbled off the beach and into the dense and dark island jungle.\n")

decision = input("> Do you wish to travel 'left' or 'right'?\n")

if decision.lower() != "left":
    print("\nYou stumble. You try to catch yourself, but you are falling...")
    print("                                       ...into a hidden, deep hole of deadly vipers!")

    lose_game = True

if lose_game is False:
    print("\nYou trip and stumble through the dense jungle darkness.")
    print("Eventually, you arrive at a clearing beside a cool, gently flowing narrow river.")

    print("\nAcross the stream, you see a curious building with three colored doors.")
    print("This building matches the rumors from the pub and you sense the treasure lies inside.")

    print("\nSuddenly, you hear a crashing sound coming from the jungle canopy behind you!\n")

    print("> Do you 'wait' to see what's coming up behind you?")

    decision = input("> Or do you jump in and `swim` across the river to the building?\n")

    if decision.lower() != "wait":
        print("\nYou quickly dive into the narrow river and swim hard towards the other side.")

        print("\nAs you near the opposite shore, you feel a hard tug at your left leg.")

        print("\n...What was that!?")

        print("\nIn the next instant, you are violently pulled under the water.")
        print("Your world goes dark. You can feel yourself entombed in a slimy, smelly, ")
        print("watery coffin as you move along gracefully under the water.")
        print("You've been swallowed by a giant trout!")

        lose_game = True

if lose_game is False:
    print("\nImmediately, you spot the source of the noise behind you.")
    print("A giant tree has given up its rooted anchoring and is falling towards you!")

    print("\n...Reflexively, you dive to the side to avoid being crushed!!!")

    print("\nThe falling tree narrowly misses you. It crashes to the ground shaking the earth.")
    print("When the dust clears, you see that the giant tree has formed a bridge across the river.")
    print("...How convenient! Now you won't get wet...\n")

    print("\nYou climb up on the giant tree trunk and walk easily to the other side of the river.")
    print("Upon approaching the building, you observe it has three colored doors.")
    print("The pub rumors hinted that behind one of the doors lies the island's treasure.")
    print("But the rumors also informed you that behind the wrong door lies death...")

    print("\nYour fate awaits you... Now you must chose!\n")

    decision = input("> Will you open the 'red', 'blue', or 'yellow' door to find the treasure?\n")

    if decision.lower() == "red":
        print("\nYou decide to tempt fate at the red door.")
        print("You grab the doorknob and with a fast twist, turn the knob...")
        print("For a just a split second your brain registers that the knob was burning hot.\n")

        print("KAAAAABOOOOOOOMMMMMM!!!!!")
        print("An explosion blasts out the booby trapped door. It's all over for you.")

        lose_game = True

    elif decision.lower() == "blue":
        print("\nYou push down the latch and excitedly pull open the handle to the blue door.")
        print("From inside the darkness behind the door you hear primal, evil screams and roars!")
        print("You are violently yanked into the black and wickedly devoured by hellion beasts.")

        lose_game = True

    else:
        print("\nYou open the yellow door... A blinding light from within escapes and temporarily ")
        print("disorientates you. You raise your hands to cover your eyes.")

        print("\n...Slowly... you spread your fingers and focus as your eyes adjust to the light.")
        print("Before you piled as large as a boulder are coins, jewels, and golden antiquities!")
        print("You've found the riches of TREASURE ISLAND!!!")

if lose_game is False:
    print("\nYou Win!")
else:
    print("\nGame Over.")
