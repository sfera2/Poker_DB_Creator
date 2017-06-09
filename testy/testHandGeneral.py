import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


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

if __name__ == '__main__':
    unittest.main()
