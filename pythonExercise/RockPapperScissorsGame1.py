## Write a program that lets the user play Rock-Paper-Scissors against the computer. There should be five rounds, and after those five rounds, your program should print out who won and lost or that there is a tie


from random import randint
import math

c = 0
d = 0
for i in range(5):
    x = randint(1, 3)
    if x == 1:
        x = "r"
    elif x == 2:
        x = "s"
    else:
        x = "p"
    play = input("'Rock(R)', 'Scissor(S)', 'Paper(P)': ")
    play.lower()
    if x == "r" and play == "R":
        print("Draw")
    elif x == "r" and play == "S":
        print("Computer won")
        d += 1
    elif x == "r" and play == "P":
        print("You won")
        c = c + 1
    elif x == "s" and play == "R":
        print("You won!")
        c = c + 1
    elif x == "s" and play == "S":
        print("Draw!")
    elif x == "s" and play == "P":
        print("Computer won!")
        d += 1
    elif x == "p" and play == "R":
        print("Computer won!")
        d += 1
    elif x == "p" and play == "S":
        print("You Won!")
        c = c + 1
    elif x == "p" and play == "P":
        print("Draw!")
if c > d:
    print("Congratulation! You are the winner")
elif d > c:
    print("Sorry, you lost to computer")
else:
    print("It's a tie")

