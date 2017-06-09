import unittest
from tworzBaze import czytajRece
import os
from collections import OrderedDict
from czytanieAkcji import *


def create_correct_results(folder):
    # used to make correct results in -folder-. Call before changing code to be
    # sure that the answers will indeed be correct
    files = ['testy/PS_NL10_USD_SH_2017_2_24_CYKP-094.txt',
             'testy/PS_NL10_USD_SH_2017_2_24_CYKP-093.txt'
             ]
    for file in files:
        list_of_hands = czytajRece(file)
        dr = 'testy/prawidlowe wyniki/{}/'.format(folder)
        if not os.path.exists(dr):
            os.makedirs(dr)
        for hand in list_of_hands:
            num = hand.get_number()
            with open('{}{}.txt'.format(dr, num), 'w') as files:
                # in the print function write what results you want
                # ex: [str(p) for p in hand.gracze] if you want names of
                # players
                print([(s.nazwa, hand.get_street_action(s.nazwa)) for
                       s in hand.strity], file=files)


class TestReka(unittest.TestCase):
    def _test_help_equal(self, folder, files, test):
        # checks for equality
        # folder = dir with correct answers
        # files = files on which tests are made
        # test = statement that produces the result which you want to get
        # tested. Ex: [str(p) for p in hand.gracze] when you want to test
        # if the list of players is correct
        for file in files:
            list_of_hands = czytajRece(file)
            for hand in list_of_hands:
                num = hand.get_number()
                name = '{}.txt'.format(num)
                with open(folder + name) as data:
                    result = eval(data.read())
                if 'get' in test:
                    print(test, num)
                test1 = eval(test)
                self.assertEqual(test1, result,
                                 msg='Not equal: {} should be: {}; Hand nr: {}'
                                 .format(test1, result, num))

    def test_players(self):
        # folder where are correct anserws
        fold = 'E:/sfera/poker/czytanie_akcji/'
        folder = fold + 'testy/prawidlowe wyniki/players/'
        # files on which tests are made
        files = ['{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-094.txt'.format(fold),
                 '{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-093.txt'.format(fold)
                 ]
        test = '[str(p) for p in hand.gracze]'
        self._test_help_equal(folder, files, test)

    def test_strit_names(self):
        # folder where are correct anserws
        fold = 'E:/sfera/poker/czytanie_akcji/'
        folder = fold + 'testy/prawidlowe wyniki/strit nazwy/'
        # files on which tests are made
        files = ['{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-094.txt'.format(fold),
                 '{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-093.txt'.format(fold)
                 ]
        test = '[s.nazwa for s in hand.strity]'
        self._test_help_equal(folder, files, test)

    def test_actions_street(self):
        # folder where are correct anserws
        fold = 'E:/sfera/poker/czytanie_akcji/'
        folder = fold + 'testy/prawidlowe wyniki/akcja strity/'
        # files on which tests are made
        files = ['{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-094.txt'.format(fold),
                 '{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-093.txt'.format(fold)
                 ]
        for file in files:
            list_of_hands = czytajRece(file)
            for hand in list_of_hands:
                num = hand.get_number()
                name = '{}.txt'.format(num)
                with open(folder + name) as data:
                    result = eval(data.read())
                test = [(s.nazwa, hand.get_street_action(s.nazwa)) for
                        s in hand.strity]
                self.assertEqual(test, result,
                                 msg='Not equal: {} should be: {}; Hand nr: {}'
                                 .format(test, result, num))


class TestPostflop(unittest.TestCase):
    def _test_stats_to_str(self, _class, hand):
        from inspect import signature
        sig = signature(_class.__init__).parameters

        string = ''
        # to jest do sprawdzania kolumn do Postflopa
        metody = [x for x in dir(_class) if not x.startswith('_')]
        for strit in hand.strity:
            if _class == Preflop and strit.nazwa != 'PREFLOP':
                continue
            # print ()
            string += strit.nazwa + '\n'
            gracze = strit.get_players_start()
            for gracz in gracze:
                pleja = str(gracz)
                # print (pleja, gracz.getAkcjaStrit(strit.nazwa))
                if 'strit' in sig:
                    a = _class(hand, strit.nazwa, pleja)
                elif 'gracz' in sig:
                    a = _class(hand, pleja)
                else:
                    a = _class(hand)
                for metoda in metody:
                    met = eval('a.%s()' % metoda)
                    string += str(pleja) + ' \t ' +\
                              str(metoda) + ' \t\t ' + str(met) + '\n'
        return string

    def test_stats_bet(self):
        # folder where are correct anserws
        fold = 'E:/sfera/poker/czytanie_akcji/'
        folder = fold + 'testy/prawidlowe wyniki/bet/'
        # files on which tests are made
        files = ['{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-094.txt'.format(fold),
                 '{}testy/PS_NL10_USD_SH_2017_2_24_CYKP-093.txt'.format(fold)
                 ]
        for file in files:
            list_of_hands = czytajRece(file)
            for hand in list_of_hands:
                num = hand.get_number()
                name = '{}.txt'.format(num)
                with open(folder + name) as data:
                    result = data.read()
                test = self._test_stats_to_str(Bet, hand)
                self.assertEqual(test, result,
                                 msg='Not equal: \n{} should be: \n{};'
                                     ' Hand nr: {}'
                                 .format(test, result, num))


if __name__ == '__main__':
    # create_correct_results('akcja strity')
    unittest.main()
