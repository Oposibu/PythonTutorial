## An integer is called squarefree if it is not divisible by any perfect squaresother than 1. For instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is divisible by 9, which is a perfect square. Write a program that asks the user for an integer and tells them if it is squarefree or not.

n = eval(input("Enter a positive integer: "))
i = 2
flag = 0
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    if i*i < n and n % (i*i) == 0 or (i * i) == n:
        flag = 1
    i += 1
if flag == 1:
    print("--", n, "is not a squareFree number")
elif flag != 1:
    print("--", n, "is a squareFree number")

