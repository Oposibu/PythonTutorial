"""People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses."""

count = 0
formula = input('Enter a formula: ')
for c in formula:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
if count == 0:
    print("Formula has equal opening and closing parenthesis")
else:
    print("Formula has unequal opening and closing parenthesis")

