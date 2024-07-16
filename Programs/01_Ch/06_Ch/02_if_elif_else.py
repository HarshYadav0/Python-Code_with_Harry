a = int(input("Enter Your Age :"))

if(a>=18):
    print("You are eligible for voting")

elif(a<0):
    print("Please Enter your valid Age")

elif(a==0):
    print("You entered zero ")

else :
    print("Not eligible for voting")