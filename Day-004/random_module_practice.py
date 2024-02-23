import random
import my_module

# Random integer generation practice
for counter in range(1, 10):
    random_integer = random.randint(1, 10)
    print(random_integer)

print("\n")

# Random floating point generation practice
for counter in range(1, 10):
    random_float = random.random()
    print(random_float)

print("\n")

# Method 1 - Random floating point number between 0 and 5
for counter in range(1, 10):
    random_integer = random.randint(0, 4)
    random_float = random.random()
    random_final = random_integer + random_float
    print(random_final)

print("\n")

# Method 2 - Random floating point number between 0 and 5
for counter in range(1, 10):
    random_float = random.random() * 5
    print(random_float)

print("\n")

# Module practice
print(my_module.pi)
