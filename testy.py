import unittest
from Hand import *
import klasy


class TestHand(unittest.TestCase):
    def _help(self, results):
        for k in results:
            b, h = klasy.Board(k[:-4].strip()), Hand(k[-4:])
            h.setBoard(b)
            dct = results[k]
            if dct['func'] == 'equal':
                for key in dct:
                    if key == 'func':
                        continue
                    method = 'h.{}'.format(key)
                    self.assertEqual(eval(method), dct[key], msg='Func: {}, Board: {}, Hand: {}'.format(dct['func'], b, h))

            elif dct['func'] == 'not equal':
                for key in dct:
                    if key == 'func':
                        continue
                    method = 'h.{}'.format(key)
                    self.assertNotEqual(eval(method), dct[key],msg='Func: {}, Board: {}, Hand: {}'.format(dct['func'], b, h))

            elif dct['func'] == 'in':
                for key in dct:
                    if key == 'func':
                        continue
                    method = 'h.{}'.format(key)
                    self.assertIn(dct[key], eval(method), msg='Func: {}, Board: {}, Hand: {}'.format(dct['func'], b, h))

            elif dct['func'] == 'not in':
                for key in dct:
                    if key == 'func':
                        continue
                    method = 'h.{}'.format(key)
                    self.assertNotIn(dct[key], eval(method), msg='Func: {}, Board: {}, Hand: {}'.format(dct['func'], b, h))

            elif dct['func'] == 'false':
                for key in dct:
                    if key == 'func':
                        continue
                    method = 'h.{}()'.format(dct[key])
                    self.assertFalse(eval(method), msg='Func: {}, Board: {}, Hand: {}'.format(dct['func'], b, h))

    def test_init(self):
            self.assertEqual(str(Hand('asks')), 'AsKs')
            self.assertIs(type(Hand('asks')), Hand)
            self.assertIs(type(Hand('asks')[0]), klasy.Karta)

    def test_init_hand(self):
        self.assertEqual(str(Hand(Hand('asks'))), 'AsKs')
        self.assertIs(type(Hand(Hand('asks'))), Hand)
        self.assertIs(type(Hand(Hand('asks'))[0]), klasy.Karta)

    def test_set_board(self):
        hand = Hand('asts')
        hand.setBoard(klasy.Board('ad9c9d'))
        self.assertEqual([str(crd) for crd in hand.lst], ['As', 'Ad', 'Ts', '9c', '9d', '0s', '0d'])
        hand = Hand('asts')
        hand.setBoard(klasy.Board('Kd9c9d'))
        self.assertEqual([str(crd) for crd in hand.lst], ['As', 'Kd', 'Ts', '9c', '9d', '0s'])
        hand = Hand('Qsts')
        hand.setBoard(klasy.Board('Kd9c9d'))
        self.assertEqual([str(crd) for crd in hand.lst], ['Kd', 'Qs', 'Ts', '9c', '9d'])

    def test_poker(self):
        '''last 4 letters make the hand. first letters make board'''
        results = {'asksjs tsqs': {'func': 'equal', 'value': 90371293, 'made': True,
                                   'sdv': 'mocne','nazwa': 'poker'},
                    'asksjs qdts': {'func': 'not equal', 'nazwa': 'poker'},
                    'askdjs qsts': {'func': 'not equal', 'nazwa': 'poker'},
                    'asks9s qsts': {'func': 'not equal', 'nazwa': 'poker'},
                    'as2s3s 5s4s': {'func': 'equal', 'nazwa': 'poker'},
                    'as2s3s4s 5sad': {'func': 'equal', 'nazwa': 'poker'},

                    }
        self._help(results)

    def test_quads(self):
        '''last 4 letters make the hand. first letters make board'''
        results = {'asahjs adac': {'func': 'equal', 'nazwa': 'kareta'},
                    'asadac ahts': {'func': 'equal', 'nazwa': 'kareta'},
                    'asahacad qsts': {'func': 'equal', 'nazwa': 'kareta'},
                    'asks9s 9h9d': {'func': 'false', 'nazwa': 'kareta'},

                    }
        self._help(results)

    def test_full(self):
        '''last 4 letters make the hand. first letters make board'''
        results = {'9h9c7c 7h7d': {'func': 'equal', 'nazwa': 'full', 'sdv': 'mocne'},
                    '9h7d7c 9d7h': {'func': 'equal', 'nazwa': 'full', 'sdv': 'mocne'},
                    'tcthtd kskd': {'func': 'equal', 'nazwa': 'full', 'sdv': 'srednie'},
                    'tcthtdts kskd': {'func': 'false', 'nazwa': 'full'},
                    '6d6cqhqc asqs': {'func': 'equal', 'nazwa': 'full', 'sdv': 'mocne'},
                    '6d6cqhqc 6sqs': {'func': 'equal', 'nazwa': 'full', 'sdv': 'mocne'},

                    }
        self._help(results)

    def test_flush(self):
        '''last 4 letters make the hand. first letters make board'''
        results = {'9h8h7h 6h5h': {'func': 'not in', 'nazwa': 'Flush'},
                   '9s9h9c8h7h 6h2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'slabe'},
                   '9s9h8c8h7h 6h2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'slabe'},
                   '9s9c8c8h7h 6h2h': {'func': 'false', 'nazwa': 'kolor'},
                   '9hThAh8h3h 6h2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'slabe'},
                   '9hJhAh8h6h Th2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'srednie'},
                   '9hThAh8h6h Qh2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'mocne'},
                   '9hTcAh8h7h 6h2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'slabe'},
                   '9hJcAh8h6h Th2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'srednie'},
                   '9hTcAh8h6h Qh2h': {'func': 'in', 'nazwa': 'Flush', 'sdv': 'mocne'},

                   }
        self._help(results)

    def test_str8(self):
        '''last 4 letters make the hand. first letters make board'''
        results = {'9h8h7h 6h5h': {'func': 'not in', 'nazwa': 'str8'},
                   '9s8s7s6s adtd': {'func': 'in', 'nazwa': 'str8', 'sdv': 'slabe'},
                   '9s9h8c8h7h jdtd': {'func': 'in', 'nazwa': 'str8', 'sdv': 'slabe'},
                   '9h9s9c8h7h jdtd': {'func': 'in', 'nazwa': 'str8', 'sdv': 'slabe'},
                   '9h9c8h6h ts7d': {'func': 'in', 'nazwa': 'str8', 'sdv': 'slabe'},
                   '9h9c8h6s ts7d': {'func': 'in', 'nazwa': 'str8', 'sdv': 'mocne'},
                   '2h9c8h6h ts7d': {'func': 'in', 'nazwa': 'str8', 'sdv': 'srednie'},
                   'ts9c8h jd7d': {'func': 'in', 'nazwa': 'str8', 'sdv': 'mocne'},

                   }
        self._help(results)

    # def test_trips(self):
    #     '''last 4 letters make the hand. first letters make board'''
    #     results = {'9h8h7h 7s7d': {'func': 'not in', 'nazwa': 'trips'},
    #                '9h8h7h 8s8d': {'func': 'in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                '9s9h8c8h as9h': {'func': 'in', 'nazwa': 'trips', 'sdv': 'slabe'},
    #                '9s9h8c8h ks9h': {'func': 'not in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                '9h9s9c jdtd': {'func': 'in', 'nazwa': 'trips', 'sdv': 'slabe'},
    #                '9hAh8h6h 6c6d': {'func': 'in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                '9hAc8h6h 6c6d': {'func': 'in', 'nazwa': 'set', 'sdv': 'srednie'},
    #                '9hAh8h6hkh 6c6d': {'func': 'in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                'th9s8s6d tstc': {'func': 'in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                'th9s8s7d tstc': {'func': 'in', 'nazwa': 'set', 'sdv': 'slabe'},
    #                'thas8s3d tstc': {'func': 'in', 'nazwa': 'set', 'sdv': 'mocne'},
    #
    #                }
    #     self._help(results)
    #
    # def test_two_pairs(self):
    #     '''last 4 letters make the hand. first letters make board'''
    #     results = {'9h9s2h 7s7d': {'func': 'not in', 'nazwa': '2P'},
    #                '9h9s8h 7s7d': {'func': 'not in', 'nazwa': '2P'},
    #                '9h9s8h tstd': {'func': 'in', 'nazwa': '2P'},
    #                '9h9s8h as8s': {'func': 'not in', 'nazwa': '2P'},
    #                '9h9sah as8s': {'func': 'not in', 'nazwa': '2P'},
    #                '9h9sahkc asks': {'func': 'in', 'nazwa': '2P'},
    #                '9h8sahkc asks': {'func': 'in', 'nazwa': '2P'},
    #                '9h8sahkc 9s8c': {'func': 'in', 'nazwa': '2P'},
    #                '9h8sahkc 7c7s': {'func': 'not in', 'nazwa': '2P'},
    #
    #                }
    #     self._help(results)
    #
    # def test_one_pair(self):
    #     '''last 4 letters make the hand. first letters make board'''
    #     results = {'9h9s2h 7s7d': {'func': 'in', 'nazwa': '1P'},
    #                '9h9s8h 7s7d': {'func': 'in', 'nazwa': '1P'},
    #                '9h9s8h tstd': {'func': 'not in', 'nazwa': '1P'},
    #                '9h9s8h as8s': {'func': 'in', 'nazwa': '1P'},
    #                '9h9sah as8s': {'func': 'in', 'nazwa': '1P'},
    #                '9h9sahkc asks': {'func': 'not in', 'nazwa': '1P'},
    #                '9h8sahkc asks': {'func': 'not in', 'nazwa': '1P'},
    #                '9h8sahkc 7c7s': {'func': 'in', 'nazwa': '1P'},
    #
    #                }
    #     self._help(results)
    #
    # def test_two_oc(self):
    #     '''last 4 letters make the hand. first letters make board'''
    #     results = {'kcqh9c adtd': {'func': 'not in', 'nazwa': '2OC'},
    #                '9h8h7c jsts': {'func': 'not in', 'nazwa': '2OC'},
    #                '6s5c4s tsjd': {'func': 'in', 'nazwa': '2OC'},
    #                '9h9s8h asks': {'func': 'in', 'nazwa': '2OC'},
    #
    #                }
    #     self._help(results)


if __name__ == '__main__':
    unittest.main()
