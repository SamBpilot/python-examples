#!/usr/bin/python3
import unittest
import cards


class CardsTestCase(unittest.TestCase):
    '''All my tests'''
    def test_cardname(self):
        '''Tests for the function cardname'''
        self.assertEqual("Ace of Spades", cards.name("AS"))
        self.assertEqual("9 of Clubs", cards.name("9C"))


if __name__ == '__main__':
    unittest.main()
