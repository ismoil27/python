# x = 15

# if x < 10:
#     print('Smaller')

# if x > 20:
#     print('Bigger')


# if x > 10 and x < 20:
#     print('Average')


# print('==================')
# print('Finished the task')


# n = 5
# while n > 0:
#     print(n)
#     n = n - 1

# print('Blastoff!')


'''
x = input('Please enter the number?\n')
a = int(x)
print(type(a))

'''
# ==================


# hours = input('Enter hours?:\n')
# rate = input('Enter Rate:\n')
# print(hours)
# print(rate)
# convert_hours_to_int = int(hours)
# convert_rate_to_float = float(rate)
# total = convert_hours_to_int * convert_rate_to_float
# print(total)

# celsius = input('Write temperature in celsius:')
# convert_into_float = int(celsius)

# # print(celsius)

# if type(convert_into_float) != int:
#     celsius = input('Oops! We ask you to enter intiger:')
# elif type(convert_into_float) == int:
#     convert_into_float = float(celsius)
#     fahrenheit = convert_into_float * 1.8000 + 32.00
#     print("Your entered temperature in fahrenheit is:", fahrenheit)
# else:
#     print('Your time is up!')


# ====================== Into to Programming. Lesson 3 ===========================
# Rule 1: Always make 'comment' if your code is nested or

# print(3 == 3)

# if(17 and True):
#     print('hello')

# if(-17 or False):
#     print('17 is converted to Bool')
# else:
#     print('Not converted')


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()


# inp = input('Enter Fahrenheit Temperature:')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 0
#     print(cel)
# except Exception as e:
#     print(e)


# number_to_guess = 42
# max_attempts = 6
# attempts = 0

# print("Welcome to the Guess the Number game!")
# print(f"Guess the number between 0 and 100. You have {max_attempts} attempts.")


# while attempts < max_attempts:
#     try:
#         guess = int(input("Enter your guess: "))
#     except Exception as e:
#         print("Invalid input. Please enter a number.")
#         continue

#     if guess < 0 or guess > 100:
#         print("Please enter a number between 0 and 100.")
#         continue

#     attempts += 1

#     if guess < number_to_guess:
#         print("Too low. Try again.")
#     elif guess > number_to_guess:
#         print("Too high. Try again.")
#     else:
#         print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
#         break

# else:
#     print(f"Sorry, you've reached the maximum number of attempts. The correct number was {number_to_guess}.")


# def my_function():
#     print('Hello world!')

# my_function()

# print(max('Hello World'))
# print(min('HelloWorld'))
# print(len('Hello World'))
