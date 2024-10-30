# Modifying Global Scope

enemies = 'Skeleton'

def increase_enemies():
    # enemies = 'Zombie' # Without the 'global' keyword this statement will
                         # create a new variable called 'enemies' with
                         # a local scope to `increase_enemies()`
    global enemies # Declaring this variable will use the global scope variable of the same name.
                   # Use of 'global' is not a good practice.
    enemies = 'Zombie'
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
