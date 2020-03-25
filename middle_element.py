# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return
# the middle element. If there are an even number of elements, the function
# should return the average of the middle two elements.


def middle_element(lst):
    if len(lst) % 2 == 0:
        middle_element1 = lst[len(lst) // 2]
        middle_element2 = lst[(len(lst) // 2) - 1]
        average = (middle_element1 + middle_element2) / 2
        return average
    else:
        return lst[len(lst) // 2]


print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -10, -4, 4]))

