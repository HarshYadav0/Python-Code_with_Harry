# Write a program using functions to find greatest of three numbers

def greatnum(a,b,c):
    if(a>b and a>c):
        print("a is greater : ")
    elif(b>a and b>c):
        print("b is a greater : ")
    else:
        print("c is greater : ")


greatnum(3,14,5)
greatnum(3,1,5)
greatnum(33,14,5)
