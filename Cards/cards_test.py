#!/usr/bin/python3
import unittest
import cards


class CardsTestCase(unittest.TestCase):
    '''All my tests'''
    def test_cardname(self):
        '''Tests for the function cardname'''
        self.assertEqual("Ace of Spades", cards.name("AS"))
        self.assertEqual("9 of Clubs", cards.name("9C"))
        self.assertEqual("Jack of Hearts", cards.name("JH"))
        self.assertEqual("King of Diamonds", cards.name("KD"))
        self.assertEqual("7 of Spades", cards.name("7S"))
        self.assertEqual("10 of Hearts", cards.name("0H"))
        self.assertEqual("2 of Clubs", cards.name("2C"))
        self.assertEqual("2 of Diamonds", cards.name("2D"))
        self.assertEqual("Queen of Diamonds", cards.name("QD"))


if __name__ == '__main__':
    unittest.main()
