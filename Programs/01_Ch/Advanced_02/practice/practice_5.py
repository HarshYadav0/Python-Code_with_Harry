# Write a program to find the maximum of the numbers in a list using the reduce
# function.

from functools import reduce

l = [13,4,5,67,8,9,64,3,2,1,]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))