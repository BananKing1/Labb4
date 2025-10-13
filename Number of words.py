"""
Write a program that counts the number of words in a sentence entered by the user.
"""

word = input("Input a word:")

letters = word.replace(" ", "")

print(letters)

total = len(letters)

print(total)
