# . Write a program to filter a list of numbers which are divisible by 5.


def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [13,4,5,67,8,9,64,3,2,1,]

f = list(filter(divisible5, a))
print(f)