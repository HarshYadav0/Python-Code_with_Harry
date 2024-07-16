f = open("file.txt")

print(f.read())
f.close()

# The Same can be written using 'with' statement :

with open("file.text") as f:
    print(f.read())

# Not necessary to close the file