#Palindrome Checker

x = int (input("Enter number to check if palindrome:"))
temp = x
y = 0
while (x > 0):
    z = x%10
    y = y*10+z
    x = x//10

if (temp == y):
    print ("It is a palindrome")

else:
    print ("It is not a palindrome")
