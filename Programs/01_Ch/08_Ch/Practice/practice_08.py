# Write a python function to print multiplication table of a given number.


def multiply(n):

    for i in range (1, n+1):
        print(f"{n} x {i} = {n*i}")
        # return n    # See Difference When using return 
       
    

n = int(input("Enter Number : "))
multiply(n)

