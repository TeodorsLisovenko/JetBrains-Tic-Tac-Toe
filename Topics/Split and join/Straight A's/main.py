# put your python code here

user_input = input().split()

total_grades = len(user_input)

how_much_a = 0

for char in user_input:
    if char == "A":
        how_much_a += 1

print(round(how_much_a / total_grades, 2))
