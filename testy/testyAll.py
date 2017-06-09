import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


class TestReka(unittest.TestCase):
    def test_ai(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/rece/'

        file = 'bug_ai.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        self.assertEqual('FLOP', hand.get_ai_street(), msg=file)
        plrs = [str(p) for p in hand.get_players_ai_street('preflop')]
        self.assertEqual(['fidas1972'], plrs,
                         msg=file)
        plrs = [str(p) for p in hand.get_players_ai_street('flop')]
        self.assertEqual(sorted(['fidas1972', 'Eddys Edge']), sorted(plrs),
                         msg=file)
        plrs = [str(p) for p in hand.get_players_ai_street('turn')]
        self.assertEqual(sorted(['Eddys Edge', 'fidas1972']), sorted(plrs),
                         msg=file)

        file = 'ai.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        self.assertEqual('FLOP', hand.get_ai_street(), msg=file)
        plrs = [str(p) for p in hand.get_players_ai()]
        self.assertEqual(sorted(['Chodemuncher', 'Krumi1703']), sorted(plrs),
                         msg=file)

        file = 'caip.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        self.assertEqual('PREFLOP', hand.get_ai_street(), msg=file)
        plrs = [str(p) for p in hand.get_players_ai()]
        self.assertEqual(sorted(['zambow20', 'fmljegvinder']), sorted(plrs),
                         msg=file)


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


class TestHandGeneral(unittest.TestCase):
    def test_sd(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.sd(), msg=file)

        file = 'f.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.sd(), msg=file)

    def test_sf(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.sf(), msg=file)

        file = 'f.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.sf(), msg=file)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.sf(), msg=file)

    def test_st(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.st(), msg=file)

        file = 'f.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.st(), msg=file)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.st(), msg=file)

    def test_sr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.sr(), msg=file)

        file = 'f.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.sr(), msg=file)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.sr(), msg=file)

    def test_ai(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'p-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual('PREFLOP', tmp.ai(), msg=file)

        file = 'p-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(None, tmp.ai(), msg=file)

        file = 'f-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual('FLOP', tmp.ai(), msg=file)

        file = 'f-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(None, tmp.ai(), msg=file)

        file = 't-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual('TURN', tmp.ai(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(None, tmp.ai(), msg=file)

        file = 'r-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual('RIVER', tmp.ai(), msg=file)

        file = 'r-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(None, tmp.ai(), msg=file)

    def test_pot_2bet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_2bet(), msg=file)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.pot_2bet(), msg=file)

        file = '4b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_2bet(), msg=file)

    def test_pot_3bet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_3bet(), msg=file)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_3bet(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.pot_3bet(), msg=file)

        file = '4b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_3bet(), msg=file)

    def test_pot_4bet(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_4bet(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_4bet(), msg=file)

        file = '4b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.pot_4bet(), msg=file)

        file = '5b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_4bet(), msg=file)

    def test_pot_5bet_plus(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_5bet_plus(), msg=file)

        file = '4b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(False, tmp.pot_5bet_plus(), msg=file)

        file = '5b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.pot_5bet_plus(), msg=file)

        file = '6b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(True, tmp.pot_5bet_plus(), msg=file)

    def test_open_pos_nr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(-1, tmp.open_pos_nr(), msg=file)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(1, tmp.open_pos_nr(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(4, tmp.open_pos_nr(), msg=file)

        file = 'izo.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(4, tmp.open_pos_nr(), msg=file)

    def test_three_bet_pos_nr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(-1, tmp.three_bet_pos_nr(), msg=file)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(-1, tmp.three_bet_pos_nr(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(1, tmp.three_bet_pos_nr(), msg=file)

        file = 'izo.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(1, tmp.three_bet_pos_nr(), msg=file)

    def test_four_bet_pos_nr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(-1, tmp.four_bet_pos_nr(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(-1, tmp.four_bet_pos_nr(), msg=file)

        file = '4b.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(3, tmp.four_bet_pos_nr(), msg=file)

    def test_nr_of_players(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 't.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(6, tmp.nr_of_players(), msg=file)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(6, tmp.nr_of_players(), msg=file)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        tmp = HandGeneral(hand)
        self.assertEqual(5, tmp.nr_of_players(), msg=file)


class TestPlayerGeneral(unittest.TestCase):
    def test_sd(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sd(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sd(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sd(), msg=file + ' ' + player)

        file = 'r.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Vovchique'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sd(), msg=file + ' ' + player)
        player = '+Kolobok_AJ'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sd(), msg=file + ' ' + player)
        player = 'wyzh250'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sd(), msg=file + ' ' + player)

    def test_wsd(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.wsd(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.wsd(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.wsd(), msg=file + ' ' + player)

        file = 'r.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Vovchique'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.wsd(), msg=file + ' ' + player)
        player = '+Kolobok_AJ'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.wsd(), msg=file + ' ' + player)
        player = 'wyzh250'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.wsd(), msg=file + ' ' + player)

    def test_sf(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sf(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sf(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sf(), msg=file + ' ' + player)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sf(), msg=file + ' ' + player)
        player = 'g2'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sf(), msg=file + ' ' + player)

    def test_st(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.st(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.st(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.st(), msg=file + ' ' + player)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.st(), msg=file + ' ' + player)
        player = 'g2'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.st(), msg=file + ' ' + player)

    def test_sr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sr(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(True, tmp.sr(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sr(), msg=file + ' ' + player)

        file = 'p.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'g1'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sr(), msg=file + ' ' + player)
        player = 'g2'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(False, tmp.sr(), msg=file + ' ' + player)

    def test_ai(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'p-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Vovchique'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('PREFLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'Sashabur'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 'p-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Vovchique'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('PREFLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'Sashabur'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('PREFLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'DayaShip'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 'f-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Ivo.S06'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('FLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'lagun777'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 'f-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'LarryTheStar'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('FLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'tumedico.com'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('FLOP', tmp.ai(), msg=file + ' ' + player)
        player = 'asdEmo'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 't-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'shenglongdou'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('TURN', tmp.ai(), msg=file + ' ' + player)
        player = 'DayaShip'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 't-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'pokerdogg45'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('TURN', tmp.ai(), msg=file + ' ' + player)
        player = 'titanik80'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('TURN', tmp.ai(), msg=file + ' ' + player)
        player = 'SVMono'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 'r-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Juliutzzz'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('RIVER', tmp.ai(), msg=file + ' ' + player)
        player = 'Oscaryynn'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

        file = 'r-ai sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'SanikQ3'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('RIVER', tmp.ai(), msg=file + ' ' + player)
        player = 'alexsile84'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual('RIVER', tmp.ai(), msg=file + ' ' + player)
        player = 'cinfinite23'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(None, tmp.ai(), msg=file + ' ' + player)

    def test_pos_nr(self):
        # folder where are correct anserws
        folder = 'E:/sfera/poker/czytanie_akcji/testy/hand/'

        file = 'p-ai nosd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'Vovchique'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(4, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'Sashabur'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(1, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'DayaShip'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(6, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'markgr111'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(5, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'LarryTheStar'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(3, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'Andy Wolf'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(2, tmp.pos_nr(), msg=file + ' ' + player)

        file = 'sd.txt'
        with open(folder + file) as data:
            hand = Reka(data.readlines())
        player = 'zxcvbnm577'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(2, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'satisfied04'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(5, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'neamtzul82'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(4, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'gaHy_HaXeP'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(1, tmp.pos_nr(), msg=file + ' ' + player)
        player = 'P308mnlt'
        tmp = PlayerGeneral(hand, player)
        self.assertEqual(3, tmp.pos_nr(), msg=file + ' ' + player)


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
