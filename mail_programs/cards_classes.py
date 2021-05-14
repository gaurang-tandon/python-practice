import random


class Card:
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = {
        "Hearts": cards,
        "Diamonds": cards,
        "Clubs": cards,
        "Spades": cards
    }


class Deck(Card):
    def __init__(self):
        list_of_cards = []
        for i, x in self.suit.items():
            for j in range(0, len(x)):
                list_of_cards.append(f"{x[j]} of {i}")
        self.list_of_cards = list_of_cards

    def shuffle_deck(self):
        random.shuffle(self.list_of_cards)

    def deal(self):
        card_picked = random.choice(self.list_of_cards)
        print(f"{card_picked.upper()} card was picked at Random")
        self.list_of_cards.remove(card_picked)
        return card_picked

    def print_cards(self):
        for i in self.list_of_cards:
            print(i)