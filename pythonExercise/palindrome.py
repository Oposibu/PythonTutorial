""" Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards"""

word = input("Enter text: ")
if word[::-1] == word:
    print("Word is palindrome")
else:
    print('word is not a palindrome')


