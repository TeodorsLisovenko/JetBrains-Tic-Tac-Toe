user_input = input()

snake_case = ""

if user_input.islower():
    print(user_input)
else:
    for char in user_input:
        if not char.islower() and char == user_input[0]:
            snake_case += char.lower()
        elif not char.islower():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

print(snake_case)
