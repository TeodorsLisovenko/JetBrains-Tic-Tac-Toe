# put your python code here

is_first_passed = False

num = []

while True:
    user_input = int(input())

    num.append(user_input)

    if sum(num, 0) == 0:
        total = 0

        for x in num:
            total += x**2
        print(total)
        break
