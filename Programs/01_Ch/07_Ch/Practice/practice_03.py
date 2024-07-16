# Write a program to print multiplication table of a given number using while loop.


n = int(input("en :"))
i=0
while(i<=10):
    # print(n ,"x", i, "=",n*i )
    print(f"{n} x {i} = {n*i}")
    i = i +1

print("While Loop Ended")