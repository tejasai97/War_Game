from Cards import Cards


class Player:
    def __init__(self, cardset=None):
        self.sets = cardset
        self.hand = []

    def cardsLeft(self):
        if len(self.sets) != 0:
            return True
        return False

    def drawCard(self):
        card = self.sets.pop()
        return card

    def addToSet(self, cards):
        self.sets + cards

    def startWar(self, card):
        self.hand.extend([card] + self.sets[-2:])
        self.sets = self.sets[:-2]
        self.sets.append(self.hand.pop())
