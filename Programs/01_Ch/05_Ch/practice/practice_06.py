# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.


dict = {}

name = input("Enter Your name : ")
lang = input("Enter Your lang : ")
dict.update({name:lang})

name = input("Enter Your name : ")
lang = input("Enter Your lang : ")
dict.update({name:lang})

name = input("Enter Your name : ")
lang = input("Enter Your lang : ")
dict.update({name:lang})

name = input("Enter Your name : ")
lang = input("Enter Your lang : ")
dict.update({name:lang})

print(dict)
