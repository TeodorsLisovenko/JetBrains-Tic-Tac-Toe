spell = "Wingardium Leviosa"

user_input = input()

try:
    print(spell.index(user_input))
except ValueError:
    print(-1)


