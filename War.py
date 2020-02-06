from Cards import Cards
from Player import Player


class War:
    def __init__(self):
        """
        initialize the players and set default parameters
        """
        playerAcards, playerBcards = Cards().generateSets()
        self.playerA = Player(playerAcards)
        self.playerB = Player(playerBcards)
        self.numDrawCards = self.playerA.numDrawCards
        self.numMapping = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        # self.playerA.sets = [(5,1)]
        # self.playerB.sets = [(5, 0), (7, 2)]

    def start_game(self):
        """
        this function contains the logic of war game

        Rules:
        1. the game continues until both players have card left with them
        2. the player who looses his cards first wins
        3. each player draws one card, who ever has bigger value gets both cards
        4. if the value of the cards drawn are same, war starts
        5. In war, each player puts 3 cards down from their decks and another face-up (to speed up the game)
        6. if the values on the face-up cards are same, war continues, else who ever has larger value gets all cards
        7. if the player doesn't have enough cards to start war, he looses

        Assumptions:
        1. if both players have less than 4 cards i.e 3 face-down and one face-up, its a draw
        2. since the order in which the loosing player puts cards under the desk is not mentioned, I used my own order
           i.e cards used by player for war(face-down) -> cards used by other user for war -> card player has recently
           drawn -> card other player has recently drawn

        :return: None
        """
        round = 1  # represents the round players are at right now
        while self.playerA.cardsLeft() and self.playerB.cardsLeft():
            print("XXXXXXXX round - " + str(round) + " XXXXXXXX")
            playerAcard = self.playerA.drawCard()
            playerBcard = self.playerB.drawCard()
            numA = playerAcard[0]
            numB = playerBcard[0]
            if numA > 10:  # change the name of card value
                numA = self.numMapping[numA]
            if numB > 10:  # change the name of card value
                numB = self.numMapping[numB]
            print("player A draws " + str(numA) + " of " + playerAcard[1])
            print("player B draws " + str(numB) + " of " + playerBcard[1])
            if playerAcard[0] == playerBcard[0]:  # this is the draw scenario when the war starts
                print("both cars are equal, war starts")
                numA = self.playerA.startWar(playerAcard)
                numB = self.playerB.startWar(playerBcard)
                if numB < self.numDrawCards and numA < self.numDrawCards:  # assumption number 1
                    print("game Draw")
                    return
                if numB < self.numDrawCards:  # rule number 7
                    print("Player B doesn't have enough cards to start war, Player A wins")
                    return
                if numA < self.numDrawCards:  # rule number 7
                    print("Player A doesn't have enough cards to start war, Player B wins")
                    return
            elif playerAcard[0] > playerBcard[0]:  # rule number 3
                print("player B has lesser card, wins this round")
                cards = self.playerA.hand + self.playerB.hand + [playerAcard, playerBcard]  # cards acquired by player A
                # after loosing (Assumption 2)
                self.playerA.addToSet(cards)  # add acquired cards at the bottom of player A stack
                self.playerA.resetHand()  # clear cards used for war
                self.playerB.resetHand()  # clear cards used for war
            elif playerBcard[0] > playerAcard[0]:  # rule number 3
                print("player A has lesser card, wins this round")
                cards = self.playerB.hand + self.playerA.hand + [playerBcard, playerAcard]  # cards acquired by player B
                # after loosing (Assumption 2)
                self.playerB.addToSet(cards)  # add acquired cards at the bottom of player B stack
                self.playerA.resetHand()  # clear cards used for war
                self.playerB.resetHand()  # clear cards used for war
            # after each round, show number of cards left with each player
            print("Player A left with: " + str(len(self.playerA.sets)) + " left")
            print("Player B left with: " + str(len(self.playerB.sets)) + " left")
            if len(self.playerB.sets) is 0:  # rule number 2
                print("player B wins")
            if len(self.playerA.sets) is 0:  # rule number 2
                print("player A wins")
            round += 1  # go to the next round


if __name__ == "__main__":
    game = War()
    game.start_game()
