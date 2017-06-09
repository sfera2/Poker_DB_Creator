import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestFloat(unittest.TestCase):
    def test_float_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_opp(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_float(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float(), msg=file + ' ' + strt + ' ' + plr)

    def test_float_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_def_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_enum_float_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual('call', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual('call', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual('2bet', tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_def(),
                         msg=file + ' ' + strt + ' ' + plr)

    def test_float_raise_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(True, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(False, tmp.float_raise_def_opp(), msg=file + ' ' + strt + ' ' + plr)

    def test_enum_float_raise_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in0gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in0gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr2r__F__BC__T__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCC__T__XXBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in1gr3r__F__BCF__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__BCF__T__XBRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCC__T__XXX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual('fold', tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__BF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBFC__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XBRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr3r__F__XBCF__T__XX__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'kr'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XX__R__BRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual('call 2bet', tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

        file = 'in2gr2r__F__XBC__T__XBC__R__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        strt, plr = 'flop', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'flop', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'turn', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'sf'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)
        strt, plr = 'river', 'zw'
        tmp = Float(hand, strt, plr)
        self.assertEqual(None, tmp.enum_float_raise_def(), msg=file + ' ' + strt + ' ' + plr)

if __name__ == '__main__':
    unittest.main()
