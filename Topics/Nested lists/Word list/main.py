text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

user_input = int(input())

new_list = []

for word_group in text:
    for word in word_group:
        if len(word) <= user_input:
            new_list.append(word)
print(new_list)
