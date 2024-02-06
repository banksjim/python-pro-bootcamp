num_char = len(input("What is your name? "))

# Type function shows the variable
print("num_char is type " + str(type(num_char)))

# Type casting
string_num_char = str(num_char)
print("Your name has " + string_num_char + " characters in it.")

print("str_num_char is type " + str(type(string_num_char)))

# Other conversions
a = 123
print(type(a))

b = str(123)
print(type(b))

c = float(123)
print(type(c))
