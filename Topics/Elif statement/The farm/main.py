user_input = int(input())

if user_input >= 6769:
    if user_input // 6769 == 1:
        print("1 sheep")
    else:
        print(user_input // 6769, "sheep")
elif user_input >= 3848:
    if user_input // 3848 == 1:
        print("1 cow")
    else:
        print(user_input // 3848, "cows")
elif user_input >= 1296:
    if user_input // 1296 == 1:
        print("1 pig")
    else:
        print(user_input // 1296, "pigs")
elif user_input >= 678:
    if user_input // 678 == 1:
        print("1 goat")
    else:
        print(user_input // 678, "goats")
elif user_input >= 23:
    if user_input // 23 == 1:
        print("1 chicken")
    else:
        print(user_input // 23, "chickens")
else:
    print("None")

