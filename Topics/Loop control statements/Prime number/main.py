num = int(input())

if num > 1:

    for i in range(2, int(num / 2) + 1):

        if (num % i) == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")

else:
    print("This number is not prime")
