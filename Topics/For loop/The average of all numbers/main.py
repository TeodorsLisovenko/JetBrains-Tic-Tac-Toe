# put your python code here

a = int(input())

b = int(input())

mean = 0

counter_of_dividers = 0

for i in range(a, b+1):
    if i % 3 == 0:
        mean += i
        counter_of_dividers += 1

print(mean / counter_of_dividers)
