import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestBVsMCbet(unittest.TestCase):
    def test_b_vs_mcb_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCC__T__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_b_vs_mcb(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XXX__T__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_b_vs_mcb_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_enum_b_vs_mcb_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('call', tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)


        file = 'in2gr3r__F__XXBFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_b_vs_mcb_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(True, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(False, tmp.b_vs_mcb_raise_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_enum_b_vs_mcb_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__XBRRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XXX__T__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = BVsMcb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_b_vs_mcb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

if __name__ == '__main__':
    unittest.main()
