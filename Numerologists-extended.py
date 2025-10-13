"""
Expand your solution to the previous exercise to allow the calculation of a complete name such as “John
Marvin Zelle” or “John Jacob Arthur Robert”. The total value is just the sum of the numeric values of
all names.
"""

def value(name):
    
    name = list(name.lower())

    print(name)

    value = 0

    for i in name:
        if i.isalpha():
            value += ord(i) - 96

    return value

print(value("John Marvin Zelle")
print(value("John Jacob Arthur Robert"))
