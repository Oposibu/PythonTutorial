"""A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string."""

count = 1
sentence = 'When there is life there is hope don\'t give up'
for w in range(len(sentence) - 1):
    if sentence[w] == ' ' and w > 0:
        count = count + 1
print(count)

