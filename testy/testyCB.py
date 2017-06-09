import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestCBet(unittest.TestCase):
    def test_cb_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XX__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XX__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_cb(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb(), msg=file + ' ' + strt + ' ' + plr)

    def test_cb_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_def_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_cb_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(True, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCRFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBRCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBRRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(False, tmp.cb_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_enum_cb_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('call', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_def(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_enum_cb_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('3bet', tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCRFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBRCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBRRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Cb(hand, strt, plr)
        self.assertEqual(None, tmp.enum_cb_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

if __name__ == '__main__':
    unittest.main()
