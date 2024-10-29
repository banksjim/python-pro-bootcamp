# Modifying Global Scope

enemies = 'Skeleton'

def increase_enemies(current_enemy):
    print(f"starting global scope enemy sent to function call: {current_enemy}")
    if current_enemy == 'Skeleton':
        return 'Zombie'

enemies = increase_enemies(enemies)
print(f"global scope enemy after function call: {enemies}")
