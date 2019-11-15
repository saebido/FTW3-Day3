#Prime Number Checker

x = int (input("Enter number to check if prime number:"))

if x > 1:
    for i in range (2, x//2):
        if x % i == 0:
            print (x, "is not a prime number")
            break

    else:
        print (x, "is a prime number")

else:
    print (x, "is not a prime number")