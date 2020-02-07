# War_Game
 Intel coding challenge
 
 # Prerequisites and installations

* You can clone this project by using the command ```git clone https://github.com/tejasai97/War_Game.git```
* The application runs on ```python 3.7``` which can be downloaded from [here](https://www.python.org/downloads/)

# Running the Application
 * you can run the application by typing the following command in the project directory ```python War.py```

# Expected Output

The sample output would look as follows:

```
XXXXXXXXXXXXXXXXXXXXXXXX round - 1 XXXXXXXXXXXXXXXXXXXXXXXX
player A draws 8 of Clubs
player B draws 9 of Spades
player A has lesser card, wins this round
Player A left with: 25 cards
Player B left with: 27 cards
XXXXXXXXXXXXXXXXXXXXXXXX round - 2 XXXXXXXXXXXXXXXXXXXXXXXX
player A draws 7 of Hearts
player B draws 5 of Clubs
player B has lesser card, wins this round
Player A left with: 26 cards
Player B left with: 26 cards
XXXXXXXXXXXXXXXXXXXXXXXX round - 3 XXXXXXXXXXXXXXXXXXXXXXXX
player A draws Queen of Spades
player B draws 7 of Diamonds
player B has lesser card, wins this round
Player A left with: 27 cards
Player B left with: 25 cards
```

# Game rules

These are the game rules I followed:

1. the game continues until both players have a card left with them
2. the player who loses his cards first wins
3. each player draws one card, whoever has bigger value gets both cards
4. if the value of the cards drawn are the same, war starts
5. In war, each player puts 3 cards down from their decks and another face-up (to speed up the game, I choose 3)
6. if the values on the face-up cards are the same, the war continues, else who ever has larger value gets all cards
7. if the player doesn't have enough cards to start a war, he looses

# Assumptions

These are the assumptions I have made for the game:

1. if both players have less than 4 cards i.e 3 face-down and one face-up, its a draw
2. since the order in which the losing player puts cards under the desk is not mentioned, I used my own order
  i.e cards used by the player for war(face-down) -> cards used by other user for war -> card player has recently
  drawn -> card other player has recently drawn

# Class Structures

1. **Cards**: The cards' class deals with generating a deck and shuffling it and giving it to the players
2. **Player**: The player class interacts with the card's class and does various operations such as storing the cards, adding new cards to the deck and drawing a card
3. **War**: The war class interacts with the player class and based on the game rules, it instructs the player objects to perform various operations

# Test Cases

You can run different scenarios by uncommenting the following code in the python file **War.py**
```
        # test cases (uncomment below lines for testing different scenarios)
        # 1. start war and win with lesser value card
        # self.playerA.sets = [(5, "Spades"), (2, "Hearts"), (3, "Clubs"), (4, "Diamonds"), (6, "Spades")]
        # self.playerB.sets = [(5, "Diamonds"), (7, "Hearts"), (2, "Clubs"), (3, "Hearts"), (5, "Clubs")]
        # 2. start war and draw
        # self.playerA.sets = [(5, "Spades"), (2, "Hearts"), (3, "Clubs"), (4, "Diamonds"), (6, "Spades")]
        # self.playerB.sets = [(5, "Diamonds"), (7, "Hearts"), (2, "Clubs"), (3, "Hearts"), (6, "Clubs")]
        # 3. start war and loss due to lack of cards
        # self.playerA.sets = [(5, "Spades"), (2, "Hearts"), (3, "Clubs"), (4, "Diamonds"), (6, "Spades")]
        # self.playerB.sets = [(5, "Diamonds"), (7, "Hearts"), (2, "Clubs"), (3, "Hearts")]
        # 4. win due to greater value
        # self.playerA.sets = [(4, "Spades"), (2, "Hearts"), (3, "Clubs"), (4, "Diamonds"), (6, "Spades")]
        # self.playerB.sets = [(5, "Diamonds"), (7, "Hearts"), (2, "Clubs"), (3, "Hearts"), (9, "Clubs")]
```

# Future Work

If I had more time, I could have worked on:

1. providing the user with the ability to modify different parameters such as Number of cards and suits available, number of cards to draw when a war starts
2. Provide a Graphical user interface for the game
