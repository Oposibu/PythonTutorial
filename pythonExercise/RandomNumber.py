from random import randint
HowMany = eval(input('How many random number: '))

for i in range(HowMany):
    RandomNumber = randint(3, 6)
    print(RandomNumber)

