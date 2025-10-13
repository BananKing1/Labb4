"""
Numerologists claim to be able to determine a person’s character traits based on the “numeric value” of
a name. The value of a name is determined by summing up the values of the letters of the name where
“a” is 1, “b” is 2, “c” is 3, up to “z” being 26. For example, the name “Zelle” would have the value
26+5+12+12+5=60. Write a program that calculates the numeric value of a single name provided as
input.
"""


def value():
    name = input("Your name: ")

    name = list(name.lower())

    print(name)

    value = 0

    for i in name:
        value += ord(i) - 96

    return value

print(value())
