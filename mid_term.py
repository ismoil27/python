# question number 1

def count_char(string1, character):
    count = 0
    for char in string1:
        if char == character:
            count += 1
    return count


result = count_char("Hello, world!", "l")
print(result)  # This will print 3, as 'l' appears 3 times in the string.


# question number 7

def is_anagram(string_1, string_2):
    string_1 = string_1.replace(" ", "").lower()
    string_2 = string_2.replace(" ", "").lower()

    return sorted(string_1) == sorted(string_2)


print(is_anagram("Listen", "silent"))  # True
print(is_anagram("aab", "aba"))  # True
print(is_anagram("aaab", "bbaaa"))  # False
print(is_anagram("Hello", "World"))  # False


# question number 8
def find_next_smallest_after_zero(lst):
    if lst is None or len(lst) == 0:
        return 0

    zero_index = -1
    for i, num in enumerate(lst):
        if num == 0:
            zero_index = i
            break

    if zero_index == -1:
        return None

    positive_integers_after_zero = [
        num for num in lst[zero_index + 1:] if num > 0]

    if not positive_integers_after_zero:
        return None

    positive_integers_after_zero.sort()
    return positive_integers_after_zero[1]


print(find_next_smallest_after_zero([3, 0, 5, -1, 2, 7]))
print(find_next_smallest_after_zero([-1, 0, -5, -2, -7]))
print(find_next_smallest_after_zero([0, 4, 1, 3, 1, 0]))
