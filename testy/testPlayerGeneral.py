import unittest
import sys
sys.path.append('E:/sfera/poker/czytanie_akcji/')
from czytanieAkcji import *


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

if __name__ == '__main__':
    unittest.main()
