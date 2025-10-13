"""
Implement a class to represent a playing card. Your class should have the following methods:
• __init__(self,rank,suit) rank is an int in the range 1 − 13 indicating the range ace-king, and
suit is a single character “d”,”c”,”h” or “s” indicating the suit (diamonds, clubs, hearts, spades).
Create the corresponding card
• getRank(self) Returns the rank of the card
• getSuit(self) Returns the suit of the card
• value(self) Return the blackjack value of a card. Ace counts as 1, face cards count as 10.
• __str__(self) Returns a string that names the card. For example, “Ace of spade”.
Note: A method named __str__ is special in Python. If asked to convert an object into a string, Python
uses this method, if it’s present. For example:
c = Card(1,"s")
print c
2
will print “Ace of spade”
Test your card class write a program that prints out n randomly generated cards and the associated
Blackjack value where n is a number supplied by the user
"""
import random


class Cards:
    def __init__(self,rank,suit):
        self.rank = rank # 1 − 13
        self.suit = suit # “d”,”c”,”h” or “s”

    def getRank(self):
        if self.rank == 1:
            return "Ace"
        elif self.rank == 11:
            return "Knight"
        elif self.rank == 13:
            return "Queen"
        elif self.rank == 13:
            return "King"
        else:
            return self.rank

    def getSuit(self):
        if self.suit == "d":
            return "diamonds"
        elif self.suit == "c":
            return "cloves"
        elif self.suit == "h":
            return "heart"
        elif self.suit == "s":
            return "spades"

    def value(self):
        return self.rank

    def  __str__(self):
        return (f"Your card is: {self.getRank()} of {self.getSuit()}")

suits = ["d", "c", "h", "s"]


n = int(input("How many cards?: "))


for i in range(n):
    card = Cards(random.randint(1, 13), random.choice(suits))
    print(card)


   





