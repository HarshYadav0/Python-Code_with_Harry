# Write a program to calculate the factorial of a given number using for loop
# Factorial Means --> 5! = 1 x 2 x 3 x 4 x 5

n = int(input("Enter the Number : "))

# i =1
product = 1

for i in range(1, n+1):
    product = product*i

print(f"Factorial of {n} is {product}")