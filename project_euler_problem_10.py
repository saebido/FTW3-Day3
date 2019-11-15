#Project Euler Problem 10
#The sum of the primes below 10 is 2+3+5+7=17. Find the sum of all the primes below two million

def Prime(x):

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if Prime(i):
        sum += i

print (sum)