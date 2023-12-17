# print('What is your favorite color?')
# data = input()
# print('You said ' + data)

# name = 'snow'

# if name == 'Arya Stark':
#     print('You are Arya')
# elif name == 'jon snow':
#     print('You are Jon Snow')
# else:
#     print('Carry on')


# animal = input('What is favorite animal?')

# if animal:
#     print(animal + ' is my favorite too!')
# else:
#     print("YOU DID NOT SAY ANYTHING NIGGA!")

# city = input('Where do you live? \n')

# if city == 'los angeles' or city == 'san francisco' or 'california':
#     print('YOU LIVE IN CALIFORNIA!')
# else:
#     print("You live somewhere else!")


# for char in 'hello':
#     print(char)

# for number in range(1, 9):
#     print(number * number)

# times = input('How many times should I tell you? ')
# times = int(times)
# cleaningRoom = 'Clean Up Your Room!'

# for repeat in range(times):
#     print(cleaningRoom)
# for numb in range(1, 21):
#     if numb == 4 or numb == 13:
#         print(f"{numb} is unlucky")
#     elif numb % 2 == 0:
#         print(f"{numb} is even")
#     else:
#         print(f"{numb} is odd")


# for numb in range(1, 21):
#     if numb == 4 or numb == 13:
#         state = 'unlucky'
#     elif numb % 2 == 0:
#         state = 'even'
#     else:
#         state = 'odd'
#     print(f"{numb} is {state}")


# msg = input('what is the password?')
# while msg != 'banana':
#     print('WRONG!')
#     msg = input('What is the secret password?')
# print('CORRECT!')


# for num in range(1, 11):
#     print(num)

# num = 1
# while num <= 11:
#     print(num)
#     num += 1
# for num in range(1, 11):
#     print("\U0001f600" * num)


# times = 1
# while times <= 11:
#     print("\U0001f600" * times)
#     times += 1


# times = 1
# while times < 10:
#     spaces = " " * (10 - times)
#     emojis = "\U0001f600" * times
#     print(spaces + emojis)
#     times += 2

# ===================================
# msg = input('Hey how is it going? ')
# while msg != 'stop copying me':
#     print(msg)
#     msg = input()
# print('UGH FINE YOU WIN!')
# ===================================


# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == 'exit'):
#         break


# times = int(input('How many times do I have to tell you? '))

# for time in range(times):
#     print('Clean up your room!')
#     if time >= 3:
#         print('do you even listen to me? ')
#         break

# import random
# random_number = random.randint(1, 10)
# guess = None

# while True:
#     guess = int(input('Pick a number from 1 to 10: '))
#     if guess < random_number:
#         print('too low!')
#     elif guess > random_number:
#         print('too high!')
#     else:
#         print('You won!')
#         play_again = input('Do you want to play again? (y/n) ')
#         if play_again == 'y':
#             random_number = random.randint(1, 10)
#             guess = None
#         else:
#             print('Thank you for playing!')
#             break


# colors = ['purple', 'black', 'gray', 'red', 'white']

# index = 0

# while index < len(colors):
#     print(f"{index}: {colors[index]}")
#     index += 1
# for color in colors:
#     print(color)


numbers = [1, 2, 4, 5, 2, 1, 2]
# print(numbers)

# numbers.extend([5, 6, 7])

# print(numbers)

# print(numbers.count(2))

colors = ['red', 'blue', 'gray', 'black', 'indigo', 'green']

print(colors[0][::-1])
