# Find the largest number in a list
# numbers = [10, 3, 6, 2]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


def largest_number(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


print(largest_number([11, 3, 6, 2]))


