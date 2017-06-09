import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestAggression(unittest.TestCase):
    def test_call(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'bug_ai.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'fidas1972'
        tmp = Aggression(hand, street, player)
        self.assertEqual(-1, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr2r__F__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(0, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__BRCRCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(0, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__XXBRCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(0, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(2, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr'
        tmp = Aggression(hand, street, player)
        self.assertEqual(0, tmp.call(),
                         msg=file + ' ' + street + ' ' + player)

    def test_aggr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'bug_ai.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'fidas1972'
        tmp = Aggression(hand, street, player)
        self.assertEqual(-1, tmp.aggr(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr2r__F__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.aggr(), msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.aggr(), msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__BRCRCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(2, tmp.aggr(), msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.aggr(), msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.aggr(), msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__XXBRCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = Aggression(hand, street, player)
        self.assertEqual(1, tmp.aggr(), msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'zw'
        tmp = Aggression(hand, street, player)
        self.assertEqual(0, tmp.aggr(), msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr'
        tmp = Aggression(hand, street, player)
        self.assertEqual(2, tmp.aggr(), msg=file + ' ' + street + ' ' + player)

if __name__ == '__main__':
    unittest.main()
