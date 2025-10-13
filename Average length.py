"""
Write a program that calculates the average word length in a sentence entered by the user.
"""

def total(word):

    letters = word.replace(" ", "")

    total = len(letters)

    return total


sentence = input("input a sentece: ")
words = sentence.split() 
print(words)

value = 0
for i in words:
    value += total(i)

print(value/len(words))

