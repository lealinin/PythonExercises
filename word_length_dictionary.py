# Write a function named word_length_dictionary that takes a list of strings
# named words as a parameter. The function should return a dictionary of key/value pairs
# where every key is a word in words and every value is the length of that word.


def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths


print(word_length_dictionary(["apple", "dog", "cat"]))  # {"apple": 5, "dog": 3, "cat": 3}
print(word_length_dictionary(["a", ""]))  # {"a": 1, "": 0}

