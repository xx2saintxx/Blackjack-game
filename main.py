import random


# Card Class: 4 Suits with values of 1-14
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


suit = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, suit) for value in range(1, 14) for suit in suit]

player_hand = []
dealer_hand = []
discard_pile = []


# Deal Out 2 Cards to all Hands of participants (Players/Dealer)
def deal():
    player_hand.append(random.randint(1, len(deck)))
    dealer_hand.append(random.randint(1, len(deck)))
    player_hand.append(random.randint(1, len(deck)))
    dealer_hand.append(random.randint(1, len(deck)))


# Deal Out 1 Card to Player that Calls
def call():
    player_hand.append(random.randint(1, len(deck)))
    pass


# Deal Out 1 Card to Dealer
def call_dealer():
    player_hand.append(random.randint(1, len(deck)))
    pass


# Checks Hand for Win-Lose Condition
# If Hand = 21 Win, < 21 Option to continue playing, > 21 Lose
def check(hand):
    if sum(hand) == 21:
        print("You Win")
    if sum(hand) > 21:
        print("You Lose")
        # TODO Allow Player option to Call or Not (Maybe make this recursive)
    else:

        pass


# Empties the Hand of all Players and the Dealer, Discarding the used cards into a separate pile
def empty_hand(hand, d_hand):
    discard_pile.append(hand)
    discard_pile.append(d_hand)
    hand.clear()
    d_hand.clear()


# Compares Player's Hands to the Dealer's hand
def reveal():
    if sum(dealer_hand) < 17:
        call_dealer()
        reveal()
    else:
        if sum(dealer_hand) > sum(player_hand):
            print("You Lose")
            empty_hand(player_hand,dealer_hand)
        if sum(dealer_hand) == sum(player_hand):
            print("Tie")
            empty_hand(player_hand,dealer_hand)

    


def play():
    pass
