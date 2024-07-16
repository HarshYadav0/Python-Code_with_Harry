# Write a python function which converts inches to cms.

# inches = int(input("Enter a number for Converting inches to cms : "))

# def converter():
#     c = inches * 2.54 
#     return c

# print(converter())


def converter_cm(inch):
    return  inch * 2.54 

n = int(input("Enter a number for Converting inches to cms : "))


print(converter_cm(n))
    