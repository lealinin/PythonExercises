# Create a function named unique_values that takes a dictionary named
# my_dictionary as a parameter. The function should return the number
# of unique values in the dictionary.


def unique_values(my_dictionary):
    found_values = []
    for value in my_dictionary.values():
        if value not in found_values:
            found_values.append(value)
    return len(found_values)


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))  # 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))  # 1

