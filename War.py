from Cards import Cards


class War:
    def __init__(self):
        self.playerAcards, self.playerBcards = Cards().generateSets()


if __name__ == "__main__":
    game = War()
    print(len(game.playerAcards))
