import random


class Cards:
    def __init__(self):
        """
        initializing a deck with 4 suits of 13 cards each and shuffiling them
        :return: None
        """
        self.numCards = 13
        self.numSuits = 4
        self.deck = []
        self.mapping = {0: "Hearts", 1: "Spades", 2: "Clubs", 3: "Diamonds"}
        # adding all cards to the deck
        for suite in range(self.numSuits):
            for card in range(2, self.numCards + 2):
                self.deck.append(tuple([card, self.mapping[suite]]))
        random.shuffle(self.deck)

    def printDeck(self):
        """
        utility method to check if deck is generated properly
        :return: None
        """
        print(self.deck)

    def generateSets(self):
        """
        creates two sets from desk for the players
        :returns list of cards where card is a tuple of number and suit
        """
        return self.deck[:int(len(self.deck) / 2)], self.deck[int(len(self.deck) / 2):]
