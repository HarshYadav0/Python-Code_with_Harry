# Write a program to fill in a letter template given below with name and date

letter = '''
    Dear <|Name|>,
        You are selected!
    <|Date|>'''

a= input("Enter Your Name :")
b = input("Enter Date :")

# chaning og replacing
print(letter.replace("<|Name|>", a).replace("<|Date|>",b))