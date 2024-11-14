valid_age = False

while valid_age is False:
    try:
        age = int(input('What is your age? '))
        valid_age = True
    except ValueError:
        print('You typed an invalid number.')

if age > 18:
    print(f'You are an adult by age {age}.')
