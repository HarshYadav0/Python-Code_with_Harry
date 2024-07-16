# Project Snake , Water , Gun 
import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, 0, -1])


youstr = input("Enter your choice ('s' : 'w' : 'g') : ")
youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

reverseDict = {1 : 'Snake' , -1 : 'Water' , 0 : 'Gun'}

you = youDict[youstr]

# We Have 2 Numbers (Variables), You and Computer  : 

print(f"Computer Choose : {reverseDict[computer]} \n  You Choose : {reverseDict[you]}")

if(computer == you):
    print("It's a Draw ! ")

else :
    if(computer == -1 and you == 1):
        print("You Win !")

    elif(computer == -1 and you == 0):
        print("You Lose !")

    elif(computer == 1 and you == -1):
        print("You Lose !")

    elif(computer == 1 and you == 0 ):
        print("You Win !")

    elif(computer == 0 and you == -1 ):
        print("You Win !")

    elif(computer == 0 and you == 1 ):
        print("You Lose !")

    else:
        print("Something went wrong")   