# Find the largest number in a list
# numbers = [10, 3, 6, 2]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


numbers = [12, 3, 6, 2]
print(largest_number(numbers))


