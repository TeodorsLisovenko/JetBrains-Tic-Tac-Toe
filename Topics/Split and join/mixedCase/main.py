user_input = input()

lowerCamelCase = ""

there_is_space = False

if ' ' in user_input:

    for char in user_input:
        if char == ' ':
            there_is_space = True
        else:
            if there_is_space:
                lowerCamelCase += char.upper()
                there_is_space = False
            else:
                lowerCamelCase += char
else:
    print(user_input)

print(lowerCamelCase)
