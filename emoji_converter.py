message = input("> ")
words = message.split(" ")
# ctrl cmd space to pull up emojis
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
