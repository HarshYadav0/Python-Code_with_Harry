# Write a program to read the text from a given file ‘poems.txt’ and find out
# # whether it contains the word ‘twinkle’.

f = open("poems.txt")
content = f.read()

if("twinkle" in content):
    print("present")
else:
    print("not present")

f.close()