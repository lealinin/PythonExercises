# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.


def values_that_are_keys(my_dictionary):
    values_list = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            values_list.append(value)
    return values_list


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))  # should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))  # should print ["a"]

