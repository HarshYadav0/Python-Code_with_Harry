# Example :-

def avg(): #() paranthize
    a = int(input("Enter Your Number : "))
    b = int(input("Enter Your Number : "))
    c = int(input("Enter Your Number : "))

    average = (a+b+c)/3
    print(average)

# Example 2 :-
n = int(input("Enter Your Opinoin 1 or 2 : "))
if(n == 1):
    print(avg())  #avg() :: " Function Call "

else:
    print("Not for you")