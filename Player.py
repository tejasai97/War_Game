from Cards import Cards


class Player:
    def __init__(self, cardset=None):
        self.sets = cardset
        self.hand = []
        self.numDrawCards = 4

    def cardsLeft(self):
        if len(self.sets) != 0:
            return True
        return False

    def drawCard(self):
        card = self.sets.pop(0)
        return card

    def addToSet(self, cards):
        self.sets = self.sets + cards

    def resetHand(self):
        self.hand = []

    def startWar(self, card):
        numCards = len(self.sets)
        self.hand.extend([card] + self.sets[-1*self.numDrawCards:])
        self.sets = self.sets[:-1*self.numDrawCards]
        self.sets.append(self.hand.pop())
        return numCards
