import random


class Cards:
    def __init__(self):
        self.numCards = 13
        self.numSuits = 4
        self.deck = []
        for suite in range(self.numSuits):
            for card in range(2, self.numCards + 2):
                self.deck.append(tuple([suite, card]))
        random.shuffle(self.deck)

    def printDeck(self):
        print(self.deck)

    def generateSets(self):
        return self.deck[:int(len(self.deck)/2)], self.deck[int(len(self.deck)/2):]

