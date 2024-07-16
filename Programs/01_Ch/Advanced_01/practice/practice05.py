# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = 5

table = [n*i for i in range(1, 11)]
print(table)

with open("table.txt", "a") as f:
    f.write(f"Table of {str(table)}" + "\n")