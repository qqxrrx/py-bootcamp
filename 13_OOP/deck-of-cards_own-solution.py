# my own solution of 'deck of cards' exercise
import random as rd


class Card:
    allowed_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    allowed_value = ['A', '2', '3', '4', '5',
                     '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value):
        suit = str(suit).strip().lower()
        suit = suit[0].upper() + suit[1:]

        value = str(value).strip().lower()
        value = value.upper()

        if suit not in Card.allowed_suit:
            raise ValueError(
                f"suit should be between: {', '.join(Card.allowed_suit)}")
        if value not in Card.allowed_value:
            raise ValueError(
                f"value should be between: {', '.join(Card.allowed_value)}")

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        self.cards = [Card(suit, value)
                      for suit in Card.allowed_suit for value in Card.allowed_value]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        card_count = len(self.cards)
        if card_count == 0 or card_count < num:
            raise ValueError("All cards have been dealt")

        # random.sample() = pick random non-repeating item from unique list depending on value of k
        dealt = rd.sample(self.cards, k=num)
        for card in dealt:
            self.cards.remove(card)
        return dealt

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        rd.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
