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


# count = 0
# total_spam_confidence = 0.0

# file_name = input("Enter the file name: ")

# try:
#     with open(file_name, 'r') as file:
#         for line in file:
#             if line.startswith('X-DSPAM-Confidence:'):
#                 spam_confidence = float(line.split(':')[1])
#                 total_spam_confidence += spam_confidence
#                 count += 1

#     if count > 0:
#         average_spam_confidence = total_spam_confidence / count
#         print(f"Average spam confidence: {average_spam_confidence}")
#     else:
#         print("No lines with 'X-DSPAM-Confidence:' found in the file.")

# except FileNotFoundError:
#     print(f"File '{file_name}' not found.")

# except Exception as e:
#     print(f"An error occurred: {str(e)}")


# ====================== new lesson Dicionaries =========================

# eng2uzb = {'one': 'bir', 'two': 'ikki', 'three': 'uch'}
# print(eng2uzb['two'])

# vals = list(eng2uzb.values())
# print(vals)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c, 0) + 1
# print(d)

# counts = {'chuck': 1, "annie": 42, 'jan': 100}

# lst = list(counts.keys())
# print(lst)
# lst.sort()
# for key in lst:
#     print(key, counts[key])
# ['jan', 'chuck', 'annie']
# annie 42
# chuck 1
# jan 100


#  ==================== Lesson tuple ========================

# At the same time while doing for loop we can iterate key, value at the same time in tuple

# t = ("a", "b", "c", "d", "e")
# print(t)
# t = ('A',) + t[1:]
# print(t)

# t = ('C',) + t[3:]
# print(t)

# t = t[:2] + ("C",) + t[3:]
# print(t)

# print((0, 1, 2) < (0, 3, 4))


# txt = "but soft what light in wonder window breaks"
# words = txt.split()
# t = list()

# for word in words:
#     t.append((len(word), words))
# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)
# print(res)


# txt = "but soft what light in wonder window breaks"
# words = txt.split()
# t = list()

# vowels = "aeiou"

# for word in words:
#     if all(char in vowels for char in word):
#         t.append((len(word), word))

# t.sort(reverse=True)

# res = list()
# for _, word in t:
#     res.append(word)
# print(res)


# ============== List Comprehension =========================

# list_of_ints_in_string = ["42", "65", "12"]
# list_of_ints = [int(x) for x in list_of_ints_in_string]
# print(sum(list_of_ints))

# list_of_ints_in_string = ["42", "65", "12"]
# list_of_ints = []
# for x in list_of_ints_in_string:
#     list_of_ints.append(int(x))
# print(sum(list_of_ints))

# ============== List Comprehension =========================
