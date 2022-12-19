## Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect cubes, or perfect fifth powers.

n = eval(input("Enter a positive number: "))
for j in range(1, n):
    i = 2
    a = n
    while i <= j:
        if (i ** 2) < j or (i ** 2) == j:
            a -= 1
        i += 1
sum = a
for j in range(1, n):
    i = 2
    b = n
    while i <= j:
        if (i ** 3) < j or (i ** 3) == j:
            b -= 1
        i += 1
sum = sum + b
for j in range(1, n):
    i = 2
    c = n
    while i <= j:
        if (i ** 5) < j or (i ** 5) == j:
            c -= 1
        i += 1
sum = sum + c
print(sum)

