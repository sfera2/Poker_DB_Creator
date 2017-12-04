from Action import *
import copy
import re


class HandHud(object):
    def __init__(self, hand):
        self.hand = hand
        self._hands()
        self._players()
        self._hands_info()
        self._player_hand()
        self._hud()

    @staticmethod
    def methods():
        return ['hands', 'players', 'hands_info', 'player_hand', 'hud']

    def _hands(self):
        dct = dict()
        keys = ['number', 'txt']
        for k in keys:
            if k == 'number':
                dct[k] = self.hand.get_number()
            else:
                txt = str(self.hand)
                dct[k] = txt
        self.hands = dct

    def _players(self):
        # returns dct1: ex: {1: {'name' : pl1}, 2: {'name" : pl2}}
        characters = ['\\', '%', '@', '&']
        dct1 = dict()
        dct2 = dict()
        i = 1
        for player in self.hand.get_players():
            pl = str(player)
            for ch in characters:
                pl = pl.replace(ch, '\\' + ch)
            pl = pl.replace("'", "''")
            pl = "E" + "'" + pl + "'"
            dct2['name'] = pl
            dct1[i] = copy.copy(dct2)
            i += 1
        self.players = dct1

    def _hands_info(self):
        dct = dict()
        tmp = HandGeneral.hud_types().keys()
        for k in tmp:
            tmp1 = eval('HandGeneral(self.hand).%s()' % k)
            tmp1 = 'None' if tmp1 is None else tmp1
            dct[k] = tmp1
        self.hands_info = dct

    def _player_hand(self):
        # returns dict where players are keys and values are dicts in which
        # columns/methods are keys and results are values
        # ex: {'player1': {'ai': None, 'st': True, ....}, 'player2': {...}}
        dct2 = dict()
        tmp = PlayerGeneral.hud_types().keys()
        plrs = [str(pl) for pl in self.hand.get_players()]
        for pl in plrs:
            dct1 = dict()
            plr = pl.replace('"', '\\"')
            for k in tmp:
                tmp1 = eval('PlayerGeneral(self.hand, "%s").%s()' % (plr, k))
                tmp1 = 'None' if tmp1 is None else tmp1
                dct1[k] = tmp1
            pl = pl.replace("'", "''")
            dct2[pl] = dct1
        self.player_hand = dct2

    def _hud(self):
        # returns dict where players are keys and values are dicts in which
        # columns/methods are keys and results are values
        # ex: {'player1': {'ai': None, 'st': True, ....}, 'player2': {...}}
        pat = re.compile(r'^\w+(_f|_t|_r)$')
        dct_tmp = Postflop(self.hand).evaluate()

        dct1 = dict()
        for k, v in dct_tmp.items():
            tmp = dict()
            for k1, v1 in v.items():
                sufix = pat.search(k1).group(1)
                for k2, v2 in v1.items():
                    tmp[k2 + sufix] = v2
            k = k.replace("'", "''")
            dct1[k] = tmp

        dct2 = PreflopEvaluate(self.hand).evaluate()
        for k, v in dct1.items():
            k = k.replace("''", "'")
            for k1, v1 in dct2[k].items():
                v[k1] = v1
        self.hud = dct1

    def get_hand(self):
        return self.hand

    def get_number(self):
        return self.hand.get_number()
