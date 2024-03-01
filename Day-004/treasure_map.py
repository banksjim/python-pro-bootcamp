# Declare variables and lists
x_coord:       int = 0
y_coord:       int = 0

position:      str = ""

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
treasure_map   = [line1, line2, line3]

# Input the area of the map to hide the treasure
position = input("Where do you want to put the treasure (XY)? " )

# Calculation logic
x_values = ["A", "B", "C"]
letter = position[0].upper()
y_coord = x_values.index(letter)

x_coord = int(position[1]) - 1

treasure_map[x_coord][y_coord] = "X"

# Output
print("Hiding your treasure! X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
