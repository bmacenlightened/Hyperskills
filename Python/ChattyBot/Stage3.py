print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
rem3 = input()
rem5 = input()
rem7 = input()
your_age = (int(rem3) * 70 + int(rem5) * 21 + int(rem7) * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")