# Exercise 7

#number 1
list = eval(input('enter a list: '))
#A
print('number in list =', len(list))

#B
print('last item in list is', list[-1])

#C
print('list in reverse', list[::-1])
list.reverse()
print(list)

#D
if 5 in list:
    print('yes, it contain 5')
else:
    print('No it has no 5')

#E
print('It contains ', list.count(5), '5s')

#F
new_list = list[1:-1]
new_list.sort()
print('new sorted list is ', new_list)

#G
cnt = 0
for i in range(len(list)):
    if list[i] < 5:
        cnt += 1
print('the number of item less than 5 is ', cnt)
