# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

i = 1

while (i<=5):
    j = 1
    while(j<=i):
        print("*" , end="") # it stops to move next line
        j= j+1
    print() # for move to the next line
    
    i  = i+1
