# =========================== LESSON 4 =====================

import random
# import math
# print(dir(math))


# for i in range(10):
#     x = random.random()
#     print(x)


# def print_lyrics():
#     print('I am Ismoil, So What is your name?')
#     print('I am Qudratbek, Nice to meet you!')


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()


# repeat_lyrics()


def computgrade(a):
    if (a >= 0.9):
        print('A')
    elif (a >= 0.8):
        print('B')
    elif (a >= 0.7):
        print('C')
    elif (a >= 0.6):
        print('D')
    else:
        print('F')


computgrade(0.5)


def pay_comp(hours, rate):
    total = hours * rate
    print(total)


pay_comp(40, 10)
