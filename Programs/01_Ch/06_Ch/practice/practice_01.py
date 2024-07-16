# Write a program to find the greatest of four numbers entered by the user  ?

Num1 = int(input("Enter num1 : "))
Num2 = int(input("Enter num2 : "))
Num3 = int(input("Enter num3 : "))
Num4 = int(input("Enter num4 : "))

if(Num1>Num2 and Num1>Num3 and Num4):
    print("Num1 is greater")

elif(Num2>Num1 and Num2>Num3 and Num2>Num4):
    print("Num2 is greater")

elif(Num3>Num1 and Num3>Num2 and Num3>Num4):
    print("Num3 is greater")

else:
    print("Num4 is greater")