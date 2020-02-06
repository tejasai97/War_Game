from Cards import Cards
from Player import Player


class War:
    def __init__(self):
        playerAcards, playerBcards = Cards().generateSets()
        self.playerA = Player(playerAcards)
        self.playerB = Player(playerBcards)

    def start_game(self):
        round =1
        while self.playerA.cardsLeft() and self.playerB.cardsLeft():
            playerAcard = self.playerA.drawCard()
            playerBcard = self.playerB.drawCard()

            if playerAcard[0] == playerBcard[0]:
                self.playerA.startWar(playerAcard)
                self.playerB.startWar(playerBcard)
            elif playerAcard[0] > playerBcard[0]:

                self.playerA.addToSet()


if __name__ == "__main__":
    game = War()
    print(len(game.playerAcards))
