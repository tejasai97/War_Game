from Cards import Cards


class Player:
    def __init__(self, cardset=None):
        """
        give cards to the player and set default number of cards to turn during war
        :param cardset: lis of cards with the player will use
        """
        self.sets = cardset
        self.hand = []
        self.numDrawCards = 4

    def cardsLeft(self):
        """
        checking if the player has any cards left
        :return: boolean value of any cards left
        """
        if len(self.sets) != 0:
            return True
        return False

    def drawCard(self):
        """
        draw a card which player will use for comparision
        :return: a card which is a tuple of number and suit
        """
        card = self.sets.pop(0)
        return card

    def addToSet(self, cards):
        """

        :param cards: set of cards needed to be added to players deck
        :return: None
        """
        self.sets = self.sets + cards

    def resetHand(self):
        """
        clears the cards used during the war after a player wins
        :return: None
        """
        self.hand = []

    def startWar(self, card):
        """
        start the war after each player has draw a card with same value
        :param card: card which the player has drawn which led to the draw
        :return: number of cards player has before the war starts
        """
        numCards = len(self.sets)
        self.hand.extend([card] + self.sets[-1 * self.numDrawCards:])  # remove cards from bottom of player stack and
        # use for war
        self.sets = self.sets[:-1 * self.numDrawCards]  # remove turn-down cards from stack
        self.sets.insert(0, self.hand.pop())  # add turn-up card on top which will be used in next round
        return numCards
