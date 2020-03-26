# Write a function named frequency_dictionary that takes a list of elements
# named words as a parameter. The function should return a dictionary
# containing the frequency of each element in words.


def frequency_dictionary(words):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
    word_freq[word] += 1
    return word_freq


print(frequency_dictionary(["apple", "apple", "cat", 1]))  # {"apple": 2, "cat": 1, 1: 1}
print(frequency_dictionary([0, 0, 0, 0, 0]))  # {0: 5}

