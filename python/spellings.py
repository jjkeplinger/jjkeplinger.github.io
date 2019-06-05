words = ["color", "colour", "gray", "grey"]

correct_spelling = ["color", "gray"]

mappings = {
    "colour": "color",
    "grey": "gray"
}

new_list = []

for word in words:
    if word in mappings:
        new_list.append(mappings[word])
    else:
        new_list.append(word)

print(new_list)
