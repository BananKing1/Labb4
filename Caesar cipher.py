"""
A Caesar cipher is a simple substitution cipher based on the idea of shifting each letter of the plaintext
message by a fixed number (called the key) of positions in the alphabet. For example, if the key value
is 2, the word “Sourpuss” would be encoded as “Uqwtrwuu”. The original message can be recovered
by “reencoding” it using a negative key. Write a program that can encode and decode caesar cipher.
The input of the program will be a string of plaintext and the value of the key. The output will be an
encoded message where each character in the original message is replaced by shifting it key characters
in the Unicode character set. For example, if ch is a character in the the string and key is the amount
to shift, then the character that replaces ch can be calculated as: chr(ord(ch)+key)
"""

def cipher(word, key):
    value = []
    key = int(key)
    word = list(word)

    for i in word:
        value.append(ord(i) + key)

    # print(value)

    new_word = []

    for k in value:
        new_word.append(chr(k))

    for l in new_word:
        print(l, end="")

def decipher(word, key):
    value = []
    key = int(key)
    word = list(word)

    for i in word:
        value.append(ord(i) - key)

    # print(value)

    new_word = []

    for k in value:
        new_word.append(chr(k))

    for l in new_word:
        print(l, end="")

cipher("Sourpuss", 2)
print("")
decipher("Uqwtrwuu", 2)
