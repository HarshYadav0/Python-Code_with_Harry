# factorial 0 = 1
# factorial 1 = 1

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter Any Number : "))
print(f"The factorial of {n} is : {factorial(n)}")
