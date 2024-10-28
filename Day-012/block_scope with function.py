game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

create_enemy()
print(new_enemy) # new_enemy is out of scope for the mainline level b/c it is local scope to the create_enemy() function
