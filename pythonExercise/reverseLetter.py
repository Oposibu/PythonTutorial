'''
Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy

'''

alp = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alp)):
      print(alp[i:] + alp[:i])

