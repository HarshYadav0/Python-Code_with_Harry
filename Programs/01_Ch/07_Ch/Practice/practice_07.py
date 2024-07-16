# Write a program to print the following star pattern.
#  *
# ***
#***** for n = 3

i = 1
k = 1

while (i<=3):
    
    
    b=1
    while(b<=3-i): # for space 
        print(" ", end='')
        b=b+1
    
    j=1
    while(j<=k):
        print("*", end='')
        j = j + 1
    
    k = k +2
    print()
    i = i +1


 