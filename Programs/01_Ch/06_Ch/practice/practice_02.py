# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

sub1 = int(input("Enter the marks of sub1 : "))
sub2 = int(input("Enter the marks of sub2 : "))
sub3 = int(input("Enter the marks of sub3 : "))


# Total Percentage
total_percentage = (100*(sub1 + sub2 + sub3)/300)

# Total  Subject 40%
if(total_percentage >= 40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Pass ", total_percentage)

else:
    print("fail", total_percentage)



