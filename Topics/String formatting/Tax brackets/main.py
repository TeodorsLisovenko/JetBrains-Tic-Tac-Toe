user_input = int(input())

if user_input >= 132407:
    print(f"The tax for {user_input} is 28%. That is {round(user_input * 28 / 100)} dollars!")
elif user_input in range(42708, 132407):
    print(f"The tax for {user_input} is 25%. That is {round(user_input * 25 / 100)} dollars!")
elif user_input in range(15528, 42708):
    print(f"The tax for {user_input} is 15%. That is {round(user_input * 15 / 100)} dollars!")
elif user_input <= 15527:
    print(f"The tax for {user_input} is 0%. That is 0 dollars!")
