import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestFacingOpp(unittest.TestCase):
    def test_self_better(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in3gr3r__F__XXX__T__XBFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual(None, tmp._better(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('zw', tmp._better(),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_raiser(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual(None, tmp._raiser(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('zw', tmp._raiser(),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_dbetter(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual(None, tmp._dbetter(),
                         msg=file + ' ' + street + ' ' + player)
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._dbetter(),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_cbetter(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in2gr3r__F__XXBCC__T__BRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual(None, tmp._cbetter(street),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__BRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._cbetter(street),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in1gr3r__F__BCF__T__BC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._cbetter(street),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_vs_mcb_better(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr3r__F__XXBCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('kr', tmp._vs_mcb_better(),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in2gr3r__F__XXX__T__BRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._vs_mcb_better(),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_floater(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__BC__T__XBC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'turn', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('zw', tmp._floater(street),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in2gr3r__F__XBFC__T__XX__R__BRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'river', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._floater(street),
                         msg=file + ' ' + street + ' ' + player)

    def test_self_plr_missed_cbet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'in1gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'flop', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual('sf', tmp._plr_missed_cbet(street),
                         msg=file + ' ' + street + ' ' + player)

        file = 'in0gr2r__F__XX.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        street, player = 'river', 'sf'
        tmp = FacingOpp(hand, street, player)
        self.assertEqual(None, tmp._plr_missed_cbet(street),
                         msg=file + ' ' + street + ' ' + player)

if __name__ == '__main__':
    unittest.main()
