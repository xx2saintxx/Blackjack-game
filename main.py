import random


# Card Class: 4 Suits with values of 1-14
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


suits = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

player_hand = []
dealer_hand = []
discard_pile = []


# Deal Out 2 Cards to all Hands of participants (Players/Dealer)
def deal():
    player_hand.append(random.randint(1, 14))
    dealer_hand.append(random.randint(1, 14))
    player_hand.append(random.randint(1, 14))
    dealer_hand.append(random.randint(1, 14))
    # player_hand.append(random.randint(1, len(deck)))
    # dealer_hand.append(random.randint(1, len(deck)))
    # player_hand.append(random.randint(1, len(deck)))
    # dealer_hand.append(random.randint(1, len(deck)))


# Deal Out 1 Card to Player that Calls
def call():
    player_hand.append(random.randint(1, 14))
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
        print(hand)
        print("You Lose")
        print("Would You like to Play Again?")

        userinput = input("Hit? Y for Yes N for No: ")
        if userinput == "Y":
            empty_hand(hand, dealer_hand)
            play()
        if userinput == "N":
            quit()

        # TODO Allow Player option to Call or Not (Maybe make this recursive)
    else:
        card1 = hand[0]
        card2 = hand[1]
        d_card1 = dealer_hand[0]
        d_card2 = dealer_hand[1]
        # User Input To Hit or Not
        if len(hand) == 2:
            print("You have a " + str(card1) + " and " + str(card2) + " Totaling " + str(sum(hand)))
            print("Dealer has a " + str(d_card2))
            print("Will you Hit?")
        if len(player_hand) == 3:
            print("You have a " + str(card1) + " and " + str(card2) + " Totaling " + str(sum(hand)))
            print("Dealer has a " + str(d_card2))
            print("Will you Hit?")

        userinput = input("Hit? Y for Yes N for No: ")
        if userinput == "Y":
            call()
            check(hand)
            print(hand)
        if userinput == "N":
            reveal()


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
    if sum(dealer_hand) < sum(player_hand):
        print("Your Hand: "+player_hand +"| Dealer's Hand: "+ dealer_hand)
        print("You Win")
    if sum(dealer_hand) > sum(player_hand):
        print("You Lose")
    if sum(dealer_hand) == sum(player_hand):
        print("Tie")


    empty_hand(player_hand, dealer_hand)
    print("Will you Play again?")
    userinput = input("Hit? Y for Yes N for No: ")
    if userinput == "Y":
        play()
    if userinput == "N":
        quit()


# Deal Cards
def play():
    deal()
    check(player_hand)

    pass


if __name__ == "__main__":
    play()
