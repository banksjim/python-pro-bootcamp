import random

flip: int = 0

flip = random.randint(0, 1)

if flip == 0:
    print(f"{flip}Tails")
else:
    print(f"{flip}Heads")
