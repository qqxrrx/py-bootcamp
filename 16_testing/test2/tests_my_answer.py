from card import Card
from deck import Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card(value="K", suit="Spades")

    def test_repr(self):
        self.assertEqual(repr(self.card), "K of Spades")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")

    def test__deal_no_cards(self):
        self.deck.cards.clear()
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test__deal_with_cards(self):
        self.assertEqual(len(self.deck._deal(10)), 10)

    def test_count(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_card(self):
        self.assertIsNotNone(self.deck.deal_card())

    def test_deal_hand(self):
        self.assertEqual(len(self.deck.deal_hand(40)), 40)

    def test_shuffle_missing_card(self):
        self.deck.cards.pop()
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_shuffle_complete_card(self):
        self.assertIsInstance(self.deck.shuffle(), Deck)


if __name__ == "__main__":
    unittest.main()
