"""
Create a deck of cards class. Internally, the deck of cards should use another class, a card class.
Your requirements are:

1)The Deck class should have a deal method to deal a single card from the deck
2)After a card is dealt, it is removed from the deck.
3)There should be a shuffle method which makes sure the deck of cards has all 52 cards
    and then rearranges them randomly.
4)The Card class should have a suit (Hearts, Diamonds, Clubs, Spades)
    and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
"""

import cards_classes as card


def count_cards(obj):
    count = len(obj)
    print(f"\n{count} cards are in the deck.")


# -------------- CREATING DECK OBJECT ----------
deck_1 = card.Deck()

# ----------------SHUFFLING DECK ----------------
deck_1.shuffle_deck()

# --------- CARDS COUNT BEFORE DEALING ----------
count_cards(deck_1.list_of_cards)

# DEALING FIRST CARD AND PRINTING WHAT CARD WAS DEALT
card_picked_1 = deck_1.deal()

# SECOND CARD AND PRINTING WHAT CARD WAS DEALT
card_picked_2 = deck_1.deal()

# CHECKING FOR DEALT CARD IN THE DECK
try:
    if not (card_picked_1 in deck_1.list_of_cards):
        print(f"\"{card_picked_1}\" already dealt, not found in deck.")
    if not (card_picked_2 in deck_1.list_of_cards):
        print(f"\"{card_picked_2}\" already dealt, not found in deck.")
    if not (card_picked_3 in deck_1.list_of_cards):
        print(f"\"{card_picked_3}\" already dealt, not found in deck.")
except NameError:
    print("NO 3rd CARD DEALT, CARDS PRESENT IN DECK")
# ----------PRINTING CARDS IN THE DECK ---------
# for i in deck_1.list_of_cards:
#     print(i)

# --------- CARDS COUNT AFTER DEALING ----------
count_cards(deck_1.list_of_cards)
