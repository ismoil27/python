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


# ====================== TEXT files and Lines, Strings. Lesson 7 ===========================

# fhand = open('mbox-short.txt')

# count = 0

# for line in fhand:
#     print('Line Count:', line.upper())
# ===========================================
# inp = fhand.read()
# print(inp[-100: len(inp)-1])
# ===========================================
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)
# ===========================================
# for line in fhand:
#     line = line.rstrip()
#     if line.find('From:') == -1:
#         continue
#     print(line)
# ===========================================
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)
# ===========================================
# fout = open('output.txt', 'w')
# line1 = "This here's the wattle, \n"
# fout.write(line1)
# line2 = "This here's the wattle again, \n"
# fout.write(line2)
# fout.close()


count = 0
total_spam_confidence = 0.0

# Prompt the user for the file name
file_name = input("Enter the file name: ")

try:
    # Attempt to open the file
    with open(file_name, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the line starts with 'X-DSPAM-Confidence:'
            if line.startswith('X-DSPAM-Confidence:'):
                # Split the line to extract the floating-point number
                spam_confidence = float(line.split(':')[1])
                # Add the spam confidence to the total
                total_spam_confidence += spam_confidence
                # Increment the count
                count += 1

    if count > 0:
        average_spam_confidence = total_spam_confidence / count
        print(f"Average spam confidence: {average_spam_confidence}")
    else:
        print("No lines with 'X-DSPAM-Confidence:' found in the file.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
