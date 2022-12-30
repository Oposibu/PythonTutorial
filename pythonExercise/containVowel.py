"""Write a program that asks the user to enter a word and prints out whether that word contains any vowels."""

word = input("Enter a word: ")
v = 'aeiou'
vow = ''
flag = 0
for c in range(len(word)):
    if word[c] in v:
        vow = vow + word[c]
if len(vow) > 0:
    print("Your Word contain vowel")
else:
    print('Your word contain no vowel')

