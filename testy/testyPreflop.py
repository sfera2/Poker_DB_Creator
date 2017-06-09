import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestPreflop(unittest.TestCase):
    def test_open_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFLIFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)

        file = '__P__FFFLFIF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(), msg=file + ' ' + player)

        file = '__P__FFRFRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)

        file = '__P__FFFOFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_opp(),
                         msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_opp(),
                         msg=file + ' ' + player)

    def test_open_(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFLIFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)

        file = '__P__FFRFRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)

        file = '__P__FFFOFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.open_(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.open_(), msg=file + ' ' + player)

    def test_izo_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFLFIF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)

        file = '__P__FLFIFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)

        file = '__P__LLFIFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)

        file = '__P__LLIFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)

        file = '__P__FOFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo_opp(),
                         msg=file + ' ' + player)

    def test_izo(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFLFIF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo(), msg=file + ' ' + player)

        file = '__P__FLFIFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo(), msg=file + ' ' + player)

        file = '__P__LLFIFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo(), msg=file + ' ' + player)

        file = '__P__LLIFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.izo(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)

        file = '__P__FOFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.izo(), msg=file + ' ' + player)

    def test_three_bet_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)

        file = '__P__LICFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_opp(), msg=file + ' ' + player)

    def test_three_bet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)

        file = '__P__LIFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet(), msg=file + ' ' + player)

        file = '__P__LICFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet(), msg=file + ' ' + player)

    def test_three_bet_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOFRFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOFRFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.three_bet_def_opp(), msg=file + ' ' + player)

    def test_enum_three_bet_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__FOFRFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('call 3bet', tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__FOFRFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('4bet', tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__LIFRFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('4bet', tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__LIFRFFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('call 3bet', tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__LIFRFFCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

        file = '__P__LIFRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_three_bet_def(), msg=file + ' ' + player)

    def test_four_bet_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOFRFFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.four_bet_def_opp(), msg=file + ' ' + player)

    def test_enum_four_bet_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOFRFFRC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('call 4bet', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('5bet', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('5bet', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual('call 4bet', tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFRCF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_four_bet_def(), msg=file + ' ' + player)

    def test_cold_four_bet_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__ORFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_opp(), msg=file + ' ' + player)

        file = '__P__ORCRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)

        file = '__P__ORCCFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_opp(), msg=file + ' ' + player)

    def test_cold_four_bet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__ORFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet(), msg=file + ' ' + player)

        file = '__P__ORCRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)

        file = '__P__ORCCFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet(), msg=file + ' ' + player)

    def test_cold_four_bet_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__ORRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__ORRFFFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__ORRFFFCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.cold_four_bet_def_opp(), msg=file + ' ' + player)

    def test_enum_cold_four_bet_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__ORRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)

        file = '__P__ORRFFFFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('call 4bet', tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)

        file = '__P__ORRFFFCC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_cold_four_bet_def(), msg=file + ' ' + player)

    def test_flat_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__OFCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat_opp(), msg=file + ' ' + player)

        file = '__P__FOFCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat_opp(), msg=file + ' ' + player)

    def test_flat(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__OFCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)

        file = '__P__FOFCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.flat(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.flat(), msg=file + ' ' + player)

    def test_sqz_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_opp(), msg=file + ' ' + player)

        file = '__P__FOCCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_opp(), msg=file + ' ' + player)

        file = '__P__LIFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)

        file = '__P__LICFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_opp(), msg=file + ' ' + player)

        file = '__P__LICRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_opp(), msg=file + ' ' + player)

    def test_sqz(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)

        file = '__P__FOCRFFRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz(), msg=file + ' ' + player)

        file = '__P__FOCCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)

        file = '__P__LIFRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)

        file = '__P__LICFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)

        file = '__P__LICRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz(), msg=file + ' ' + player)

    def test_sqz_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

        file = '__P__LICRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

        file = '__P__LICRFFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

        file = '__P__LICRFFCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.sqz_def_opp(), msg=file + ' ' + player)

    def test_enum_sqz_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

        file = '__P__FOCRFFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual('4bet', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

        file = '__P__LICRFFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

        file = '__P__LICRFFFFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual('4bet', tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

        file = '__P__LICRFFCFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_sqz_def(), msg=file + ' ' + player)

    def test_steal_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFFOF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)

        file = '__P__FFLFIFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_opp(), msg=file + ' ' + player)

    def test_steal(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFFOF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)

        file = '__P__FFLFIFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal(), msg=file + ' ' + player)

    def test_steal_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFOFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_def_opp(), msg=file + ' ' + player)

        file = '__P__FFFOFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.steal_def_opp(), msg=file + ' ' + player)

        file = '__P__FOFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_def_opp(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.steal_def_opp(), msg=file + ' ' + player)

    def test_enum_steal_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FFFOFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_steal_def(), msg=file + ' ' + player)

        file = '__P__FFFOFRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual('3bet', tmp.enum_steal_def(), msg=file + ' ' + player)

        file = '__P__FOFFFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g5'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_steal_def(), msg=file + ' ' + player)
        player = 'g6'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_steal_def(), msg=file + ' ' + player)

    def test_five_bet_def_opp(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)

        file = '__P__FOCRFFRCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual(True, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(False, tmp.five_bet_def_opp(), msg=file + ' ' + player)

    def test_enum_five_bet_def(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = '__P__FOFRFFRRF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('fold', tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)

        file = '__P__FOCRFFRRFC.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('call 5bet', tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)

        file = '__P__FOCRFFRCRFF.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g2'
        tmp = Preflop(hand, player)
        self.assertEqual('6bet', tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g3'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)
        player = 'g4'
        tmp = Preflop(hand, player)
        self.assertEqual(None, tmp.enum_five_bet_def(),
                         msg=file + ' ' + player)

if __name__ == '__main__':
    unittest.main()
