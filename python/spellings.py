words = ["color", "colour", "gray", "grey"]

correct_spelling = ["color", "gray"]

mappings = {
    "colour": "color",
    "grey": "gray"
}

new_list = []

for word in words:
    if word in mappings:
        corrected_word = mappings [word]
        new_list.append(corrected_word)
    else:
        new_list.append(word)

print(new_list)
