#  Write a program to find whether a given number is prime or not

n = int(input("Enter Any number : "))

for i in range (1, n):
    if(n%i ==0):
        print("It is not prime", i)

    else:
        print("It is prime", i)