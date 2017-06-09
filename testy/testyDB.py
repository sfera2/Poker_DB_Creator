import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestDonkBet(unittest.TestCase):
    def test_db_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__XXBFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__XBCRFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_db(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__XBRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__XBFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db(), msg=file + ' ' + strt + ' ' + plr)

    def test_db_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_def_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_db_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in2gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(True, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(False, tmp.db_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_enum_db_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_db_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual('call', tmp.enum_db_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_db_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_db_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_db_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BCRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in3gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_def(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_enum_db_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in2gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Db(hand, strt, plr)
        self.assertEqual(None, tmp.enum_db_raise_def(),
                         msg=file + ' ' + strt + ' ' + plr)

if __name__ == '__main__':
    unittest.main()
