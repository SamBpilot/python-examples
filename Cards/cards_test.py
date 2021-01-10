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

    def test_value(self):
        '''Tests for the function value'''
        self.assertEqual(9, cards.value("9S"))
        self.assertEqual(10, cards.value("0S"))
        self.assertEqual(8, cards.value("8S"))
        self.assertEqual(7, cards.value("7S"))
        self.assertEqual(6, cards.value("6S"))
        self.assertEqual(5, cards.value("5S"))
        self.assertEqual(4, cards.value("4S"))
        self.assertEqual(3, cards.value("3S"))
        self.assertEqual(2, cards.value("2S"))
        self.assertEqual(1, cards.value("1S"))
        self.assertEqual(10, cards.value("JS"))
        self.assertEqual(10, cards.value("QS"))
        self.assertEqual(10, cards.value("KS"))
        self.assertEqual(11, cards.value("AS"))

    def test_handscore(self):
        '''Tests for the function handscore which will find the score of someone's hand'''
        self.assertEqual(21, cards.handscore(["AS", "8C", "2D"]))
        self.assertEqual(15, cards.handscore(["KS", "2C", "3D"]))
        self.assertEqual(22, cards.handscore(["JS", "5C", "7D"]))
        self.assertEqual(15, cards.handscore(["QS", "3C", "2D"]))
        self.assertEqual(25, cards.handscore(["0S", "9C", "6D"]))
        self.assertEqual(18, cards.handscore(["3S", "6C", "9D"]))


if __name__ == '__main__':
    unittest.main()
