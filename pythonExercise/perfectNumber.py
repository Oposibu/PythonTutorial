## A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself. For instance, 6 is a perfect number because the divisors of are 1, 2, 3, 6 and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors are 1, 3, 5, 15 and 15 ̸= 1 + 3 + 5. Write a program that finds all four of the perfect numbers that are less than 10000.


n = eval(input("Enter a positive number: "))
for j in range(n):
    sum = 1
    i = 2
    while i * i <= j:
        if j % i == 0:
            sum = sum + i + j/i
        i += 1
    if sum == j and j != 1:
        print(j, end=" ")

