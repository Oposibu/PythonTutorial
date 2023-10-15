# Task2
from random import randint
list = []
for i in range(20):
    list.append(randint(1, 100))
# A
print(list)

#B
print('Average is ', sum(list)/len(list))

#C 
print('Largest number is', max(list), 'and smallest number is', min(list))

#D
list.sort()
print(list)
print('second largest number is ', list[18], 'and the second lowest number is', list[1])

#E
cnt = 0
for i in range(len(list)):
    if list[i]%2 == 0:
        cnt += 1
print(cnt)

