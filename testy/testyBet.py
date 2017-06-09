import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestBet(unittest.TestCase):
    def test_better(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'river.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a1-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.better,
                         msg=file + ' ' + street + ' ' + player)

    def test_raiser(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'a1-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Zwidawurzn', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('kr123445', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('Sfera2', tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

        file = 'river.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.raiser,
                         msg=file + ' ' + street + ' ' + player)

    def test_b_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'
        file = '__bug1.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'AIONCMA1988'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = '__bug3.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'turn', 'Smitty03300'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)

        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'
        file = 'river.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'Sfera2'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'Sfera2'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'Zwidawurzn'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'Sfera2'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'Zwidawurzn'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'ai.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'Chodemuncher'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(True, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'Krumi1703'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'Chodemuncher'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'Krumi1703'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'Chodemuncher'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'Krumi1703'
        tmp = Bet(hand, strt, plr)
        self.assertEqual(False, tmp.b_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_b(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'
        file = 'river.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = Bet(hand, 'flop', 'Sfera2')
        self.assertEqual(False, tmp.b(), msg=file)
        tmp = Bet(hand, 'flop', 'Zwidawurzn')
        self.assertEqual(False, tmp.b(), msg=file)
        tmp = Bet(hand, 'turn', 'Sfera2')
        self.assertEqual(False, tmp.b(), msg=file)
        tmp = Bet(hand, 'turn', 'Zwidawurzn')
        self.assertEqual(False, tmp.b(), msg=file)
        tmp = Bet(hand, 'river', 'Sfera2')
        self.assertEqual(True, tmp.b(), msg=file)
        tmp = Bet(hand, 'river', 'Zwidawurzn')
        self.assertEqual(False, tmp.b(), msg=file)

        file = 'f2.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = Bet(hand, 'flop', 'kr123445')
        self.assertEqual(True, tmp.b(), msg=file)
        tmp = Bet(hand, 'flop', 'Zwidawurzn')
        self.assertEqual(False, tmp.b(), msg=file)
        tmp = Bet(hand, 'flop', 'Sfera2')
        self.assertEqual(False, tmp.b(), msg=file)

    def test_b_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'
        file = 'river.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'river', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'river', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'f1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'f12.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-7.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

    def test_enum_b_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'
        file = 'river.txt'

        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'river', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'river', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('call', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'f1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('2bet', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'f12.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('call', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('call', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('2bet', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('call', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'r1-7.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('2bet', tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_def(),
                         msg=file + ' ' + street + ' ' + player)

    def test_b_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'bug_b_raise_def_opp.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'OceanBlue100'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = '__bug5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'river', 'Action_Gibi'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'a1-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a1-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a1-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.b_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

    def test_enum_b_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'a1-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a1-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('call 2bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a1-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('3bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a2-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('3bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('call 2bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a3-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a4-6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('call 2bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a5-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('3bet', tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'a6-3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_b_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

    def test_raise_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__bug4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Mimimimi77'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'b1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b7.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b8.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b9.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b10.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b11.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(True, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(False, tmp.raise_raise_def_opp(),
                         msg=file + ' ' + street + ' ' + player)

    def test_enum_raise_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/bet/'

        file = 'b1.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('4bet', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b2.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b3.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b4.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b5.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b6.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b7.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual('call 3bet', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b8.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('call 3bet', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b9.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual('4bet', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b10.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'b11.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'Sfera2'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'Zwidawurzn'
        tmp = Bet(hand, street, player)
        self.assertEqual('fold', tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'flop', 'kr123445'
        tmp = Bet(hand, street, player)
        self.assertEqual(None, tmp.enum_raise_raise_def(),
                         msg=file + ' ' + street + ' ' + player)

if __name__ == '__main__':
    unittest.main()
