## Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is. I Included the count for both correct and the right answers and also calculate the percentage of the correct answers.

from random import randint
import math

correctAnswer = 0
wrongAnswer = 0
for i in range(10):
    x = randint(0, 9)
    y = randint(0, 9)
    p = x * y
    print("Question", i+1, ":", x, "*", y, sep=" ")
    q = eval(input("Answer= "))
    if q == p:
        print("Correct")
        correctAnswer = correctAnswer + 1
    else:
        print("Wrong")
        wrongAnswer = wrongAnswer + 1
print("Correct answer =", correctAnswer)
print("Wrong answers = ", wrongAnswer)
percentage = correctAnswer/10 * 100
print("your percentage =", percentage, "%", sep="")

