# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter Any NUmber : "))

i = 1
sum = 0

while(i<=n):
    sum = sum + i
    i = i + 1
    print("while sum = ",sum)

print(sum)
    