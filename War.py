from Cards import Cards
from Player import Player


class War:
    def __init__(self):
        playerAcards, playerBcards = Cards().generateSets()
        self.playerA = Player(playerAcards)
        self.playerB = Player(playerBcards)
        self.numDrawCards = self.playerA.numDrawCards
        # self.playerA.sets = [(5,1)]
        # self.playerB.sets = [(5, 0), (7, 2)]

    def start_game(self):
        round = 1
        print(self.playerA.sets[0][0])
        print(self.playerB.sets[0][0])
        while self.playerA.cardsLeft() and self.playerB.cardsLeft():
            print("XXXXXXXX round - " + str(round) + " XXXXXXXX")
            playerAcard = self.playerA.drawCard()
            playerBcard = self.playerB.drawCard()
            print("player A draws " + str(playerAcard[0]))
            print("player B draws " + str(playerBcard[0]))
            if playerAcard[0] == playerBcard[0]:
                print("both cars are equal, war starts")
                numA = self.playerA.startWar(playerAcard)
                numB = self.playerB.startWar(playerBcard)
                if numB < self.numDrawCards and numA < self.numDrawCards:
                    print("game Draw")
                    return
                if numB < self.numDrawCards:
                    print("Player B doesn't have enough cards to start war, Player A wins")
                    return
                if numA < self.numDrawCards:
                    print("Player A doesn't have enough cards to start war, Player B wins")
                    return
            elif playerAcard[0] > playerBcard[0]:
                print("player B has lesser card, wins this round")
                cards = self.playerA.hand + self.playerB.hand + [playerAcard, playerBcard]
                self.playerA.addToSet(cards)
                self.playerA.resetHand()
                self.playerB.resetHand()
            elif playerBcard[0] > playerAcard[0]:
                print("player A has lesser card, wins this round")
                cards = [playerAcard, playerBcard] + self.playerA.hand + self.playerB.hand
                self.playerB.addToSet(cards)
                self.playerA.resetHand()
                self.playerB.resetHand()
            # print(str(len(self.playerB.sets)))
            print("Player A left with: "+str(len(self.playerA.sets))+" left")
            print("Player B left with: " + str(len(self.playerB.sets)) + " left")
            if len(self.playerB.sets) is 0:
                print("player B wins")
            if len(self.playerA.sets) is 0:
                print("player A wins")
            round += 1


if __name__ == "__main__":
    game = War()
    game.start_game()
