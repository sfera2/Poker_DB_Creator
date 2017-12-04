import re
from collections import deque
import collections
import copy


class Reka(object):
    # whole hand from hand history
    def __init__(self, hand):
        self._initiative = {}
        self.hand = hand
        self._playas()
        self.bu = self._button()
        self._players_positions()
        self._streets()
        self._acts()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i == len(self.hand):
            raise StopIteration
        self.i += 1
        return self.hand[self.i - 1]

    def __str__(self):
        return ''.join(self.hand)

    def _playas(self):
        # returns tuple(int, Gracz) for eveyr player in hand, where int is
        # his seat
        self.players = list()
        wzor = re.compile(r'Seat (\d): (.*) \(\$\d+(.\d+)? in chips\)')
        for i, line in enumerate(self.hand):
            line = line.strip()
            nick = wzor.search(line)
            if nick is not None:
                self.players.append(
                    (int(nick.group(1)), Player(nick.group(2))))
            if i == 13:
                break

    def _button(self):
        # returns 4 if button was on Seat 4
        pat = re.compile(r'Seat #(\d) is the button')
        for line in self.hand:
            line = line.strip()
            bu = pat.search(line)
            if bu is not None:
                return int(bu.group(1))

    def _players_positions(self):
        # gives position to every player
        plrs_num = len(self.players)
        nr = None
        for el in self.players:
            if el[0] == self.bu:
                nr = self.players.index(el)
                break

        lst = deque([x[1] for x in self.players])
        lst.rotate(-nr)
        tmp = list(lst)
        if plrs_num == 6:
            positions = ['bu', 'sb', 'bb', 'utg', 'mp', 'co']
        elif plrs_num == 5:
            positions = ['bu', 'sb', 'bb', 'mp', 'co']
        elif plrs_num == 4:
            positions = ['bu', 'sb', 'bb', 'co']
        elif plrs_num == 3:
            positions = ['bu', 'sb', 'bb']
        else:
            # in HU dealer is on smallblind, moves first pre and last post
            positions = ['bu', 'bb']

        self.players = collections.OrderedDict()
        for i in range(len(tmp)):
            plr = tmp[i]
            plr.set_position(positions[i])
            self.players[str(plr)] = plr

    def _acts(self):
        self.actions = collections.OrderedDict()
        for name, street in self.streets.items():
            self.actions[name] = street.action_

    def _streets(self):
        ai = re.compile(r'.* is all-in')
        sd = re.compile(r'\*\*\* (FIRST |SECOND )?SHOW DOWN \*\*\*')
        preflop = re.compile(r'\*\*\* HOLE CARDS \*\*\*.*')
        flop = re.compile(r'\*\*\* (FIRST |SECOND )?FLOP \*\*\*.*')
        turn = re.compile(r'\*\*\* (FIRST |SECOND )?TURN \*\*\*.*')
        river = re.compile(r'\*\*\* (FIRST |SECOND )?RIVER \*\*\*.*')
        summary = re.compile(r'\*\*\* SUMMARY \*\*\*.*')
        patterns = [ai, preflop, flop, turn, river, sd, summary]
        pattern_names = ['AI', 'preflop', 'flop', 'turn', 'river', 'SD',
                         'summary']

        inds = collections.OrderedDict()
        for i, line in enumerate(self.hand):
            for ind, pattern in enumerate(patterns):
                if pattern.match(line):
                    # can be two SD; i want only line nr of the first
                    if pattern == sd and 'SD' in inds:
                        continue
                    inds[pattern_names[ind]] = i
                    break

        self.checker_sd = 'SD' in inds
        keys = [k for k in inds.keys()]
        self.street_ai = keys[keys.index(
            'AI') - 1].upper() if 'AI' in keys and self.checker_sd else None
        if 'AI' in keys:
            keys.remove('AI')

        st_len = collections.OrderedDict()
        for i, el in enumerate(keys[1:], 1):
            st_len[keys[i - 1]] = inds[el] - inds[keys[i - 1]]

        players = dict(self.players)
        self.streets, self.rest = dict(), []
        tmp = ['preflop', 'flop', 'turn', 'river']
        for k, v in st_len.items():
            if k not in tmp:
                ind1, ind2 = inds[k], inds[keys[keys.index(k) + 1]]
                self.rest.append(self.hand[ind1:ind2])
            else:
                if v == 1:
                    self.streets[k.upper()] = Street(k + ' AI', players)
                    self.streets[k.upper()].action()
                else:
                    ind1, ind2 = inds[k], inds[keys[keys.index(k) + 1]]
                    self.streets[k.upper()] = Street(self.hand[ind1:ind2],
                                                     players)
                    self.streets[k.upper()].action()
                    players = self.streets[k.upper()].get_players_end()

    def initiative(self):
        for name, street in self.streets.items():
            if street + 1 is not None:
                self._initiative[street + 1] = street._get_initiative()
        return self._initiative

    def get_action(self):
        return self.actions

    def get_init_street(self, street_name):
        return self._initiative.get(street_name.upper(), None)

    def get_street(self, street_name):
        return self.streets.get(street_name.upper(), None)

    def get_players(self):
        return self.players

    def get_actions(self):
        return self.actions

    def get_street_action(self, street_name):
        # returns dict containing action from every player in order in which
        #  it happened
        return self.actions.get(street_name.upper(), {})

    def get_street_bool(self, street_name):
        # returns True if there was given street in the hand
        return street_name.upper() in self.streets.keys()

    def get_sd_bool(self):
        # True if there was SD
        return self.checker_sd

    def get_street_players(self, street_name):
        # returns players present on a given street
        if not self.get_street_bool(street_name):
            return None
        else:
            return self.get_street(street_name).get_players_start()

    def get_ai_street(self):
        for street in ['PREFLOP', 'FLOP', 'TURN', 'RIVER']:
            if street in self.streets.keys():
                if self.streets[street].ended_in_ai():
                    return street

    def get_players_ai(self):
        tmp = self.get_ai_street()
        if tmp is not None:
            return self.get_street(tmp).get_players_end()
        return None

    def get_players_ai_street(self, street_name):
        # players which were or went AI on the street
        return self.get_street(street_name).players_ai()

    def get_number(self):
        # returns hand number from hand history
        pat = re.compile(r'^PokerStars Hand #(\d+):.*')
        tmp = pat.search(self.hand[0])
        return tmp.group(1)

    def get_nr_of_players(self):
        return len(self.players)


class Act(object):
    def __init__(self, move):
        self.move = move
        self._set_type()

    def __str__(self):
        return self.move

    def _set_type(self):
        pat_aggr = re.compile(r'^(\d)?bet')
        pat_call = re.compile(r'call(.*)?')
        if self.move == 'fold':
            self.type = 'fold'
        elif self.move == 'check' or pat_call.match(self.move):
            self.type = 'passive'
        elif 'raise' in self.move or pat_aggr.match(self.move):
            self.type = 'aggr'
        else:
            # np. ktos sie dosiadl do stolika w trakcie reki
            self.type = 'none'

    def get_name(self, street_name, how_many_agro):
        # returns the name of the action depending on how many agro actions
        # were made before, and the street we're in
        # Ex: self.typ == 'pasywne', preflop, how_many_agro=1 => flat
        # EX: self.typ =='pasywne', flop, how_many_agro=1 => call
        if self.type == 'fold' or self.type == 'none':
            return self.move
        if street_name == 'PREFLOP':
            if self.type == 'passive':
                if how_many_agro == 0:
                    tmp = 'limp'
                elif how_many_agro == 1:
                    tmp = 'flat'
                else:
                    tmp = 'call {}bet'.format(how_many_agro + 1)
            elif self.type == 'aggr':
                if how_many_agro == 0:
                    tmp = 'open'
                else:
                    tmp = '{}bet'.format(how_many_agro + 2)
        else:
            if self.type == 'passive':
                if how_many_agro == 0:
                    tmp = 'check'
                elif how_many_agro == 1:
                    tmp = 'call'
                else:
                    tmp = 'call {}bet'.format(how_many_agro)
            elif self.type == 'aggr':
                if how_many_agro == 0:
                    tmp = 'bet'
                else:
                    tmp = '{}bet'.format(how_many_agro + 1)
        if 'AI' in self.move:
            tmp += ' AI'
        return tmp

    def get_type(self):
        return self.type


class Player(object):
    def __init__(self, player):
        self.action = {}
        self.player = player
        self.street_ai = None

    def __str__(self):
        return self.player

    def __eq__(self, other):
        return self.player == other.player

    def _set_street(self, street):
        # flop, turn, river
        self.street = street

    def set_position(self, position):
        self.position = position.upper()

    def get_position(self):
        return self.position

    def set_street_ai(self, street_name):
        self.street_ai = street_name

    def get_street_ai(self):
        return self.street_ai

    def get_street_ai_bool(self, street_name, before=False):
        # True if he was AI on that street
        lst = ['PREFLOP', 'FLOP', 'TURN', 'RIVER']
        if self.street_ai is None:
            return False
        if not before:
            return lst.index(self.street_ai) <= lst.index(street_name.upper())
        return lst.index(self.street_ai) < lst.index(street_name.upper())

    def set_action(self, street, action):
        self._set_street(street)
        if self.action.get(self.street) is not None:
            self.action[self.street].append(action)
        else:
            lst = list()
            lst.append(action)
            self.action[self.street] = lst

    def get_action(self):
        return self.action

    def get_street_action(self, street):
        return self.action.get(street.upper())

    def rel_pos_post_bool(self, other):
        # returns true if self.player has postion post over other player
        lst = ['SB', 'BB', 'UTG', 'MP', 'CO', 'BU']
        return lst.index(self.get_position()) > lst.index(other.get_position())

    def rel_pos_pre_bool(self, other):
        # returns true if self.player has postion pre over other player
        lst = ['UTG', 'MP', 'CO', 'BU', 'SB', 'BB']
        return lst.index(self.get_position()) > lst.index(other.get_position())

    def position_number(self, street):
        if street.upper() == 'PREFLOP':
            lst = ['UTG', 'MP', 'CO', 'BU', 'SB', 'BB']
        else:
            lst = ['SB', 'BB', 'UTG', 'MP', 'CO', 'BU']
        return lst.index(self.get_position())

    def hud_position_nr(self):
        lst = ['BU', 'BB', 'SB', 'CO', 'MP', 'UTG']
        return lst.index(self.get_position()) + 1


class Street(object):
    def __init__(self, street, players):
        self.street = street  # text from hand history
        self._initiative = None
        self.players = players
        self._name()
        self.action_flg = False
        self.players_ai_ = {}

    def __sub__(self, nr):
        lst = ['PREFLOP', 'FLOP', 'TURN', 'RIVER']
        nr = lst.index(self.name) - nr
        if nr < 0 or nr > 3:
            return None
        else:
            return lst[nr]

    def __add__(self, nr):
        lst = ['PREFLOP', 'FLOP', 'TURN', 'RIVER']
        nr = lst.index(self.name) + nr
        if nr < 0 or nr > 3:
            return None
        else:
            return lst[nr]

    def __str__(self):
        return ''.join(self.street)

    def _name(self):
        # sets self.name
        lst = []
        if type(self.street) is not list:
            lst.append(self.street)
            self.street = lst

        pat = re.compile(r'\*\*\* (\w+) \*\*\* .*')
        pat1 = re.compile(r'(\w+) AI.*')
        if 'AI' in self.street[0]:
            tmp = pat1.search(self.street[0])
        else:
            tmp = pat.search(self.street[0])
        if tmp is None:
            self.name = 'PREFLOP'
        else:
            self.name = tmp.group(1).upper()

    def _action(self):
        # sets self.action attribute which is an OrderedDict in which players
        # and their actions are saved in order they were made
        _raise = re.compile(r'(?P<player>.+): (?P<act>raise)s'
             r' (\$\d+(\.\d+)? to \$\d+(\.\d+)?)(?P<ai> and is all-in)?')
        _check = re.compile(r'(?P<player>.+): (?P<act>check)s')
        # _leave = re.compile(r'(?P<player>.+) (?P<act>leave)s.*')
        _fold = re.compile(r'(?P<player>.+): (?P<act>fold)s')
        _call = re.compile(r'(?P<player>.+):'
                           r' (?P<act>call)s'
                           r' \$(\d+(\.\d+)?)(?P<ai> and is all-in)?')
        _bet = re.compile(r'(?P<player>.+):'
                          r' (?P<act>bet)s'
                          r' \$(\d+(\.\d+)?)(?P<ai> and is all-in)?')
        _walk = re.compile(r'(?P<player>.*) collected .*')

        patterns = [_fold, _raise, _check, _call, _bet, _walk]
        # patterns = [_fold, _raise, _check, _call, _bet, _leave, _walk]
        patterns1 = [_raise, _call, _bet]

        self.action_ = {}
        walk_checking_list = []
        for i, line in enumerate(self.street):
            for pattern in patterns:
                if pattern == _walk and self.name != 'PREFLOP':
                    continue
                tmp = pattern.search(line)
                if tmp is not None:
                    if pattern in patterns1:
                        gracz, zagranie = tmp.group('player'), tmp.group('act')
                        ai = tmp.group('ai')
                        if ai is not None:
                            zagranie += ' AI'
                    else:
                        if pattern == _walk:
                            gracz, zagranie = tmp.group(1), 'walk'
                        else:
                            gracz = tmp.group('player')
                            zagranie = tmp.group('act')
                    if zagranie == 'walk':
                        if gracz in walk_checking_list:
                            pass
                        else:
                            self.action_[i] = {gracz: Act(zagranie)}
                    else:
                        walk_checking_list.append(gracz)
                        self.action_[i] = {gracz: Act(zagranie)}
                    break

    def _action2(self):
        # naming actions and setting initiative and all-in players
        self.how_many_aggr = 0
        self.players_end_ = dict(self.players)
        tmp_plrs, plrs_ai = dict(), list()
        for key, dct in self.action_.items():
            k, v = tuple(dct.items())[0]
            dct[k] = v.get_name(self.name, self.how_many_aggr)
            if v.get_type() == 'aggr':
                self._initiative = k
                self.how_many_aggr += 1
                tmp_plrs.clear()
                if 'AI' not in str(v):
                    tmp_plrs[k] = 1
                else:
                    plrs_ai.append(k)
            elif v.get_type() == 'passive':
                if 'AI' not in str(v):
                    tmp_plrs[k] = 1
                else:
                    plrs_ai.append(k)
            elif v.get_type() == 'fold':
                self.players_end_.pop(k)
                try:
                    tmp_plrs.pop(k)
                except KeyError:
                    pass

        # setting actions for players
        for key, dct in self.action_.items():
            plr, action = tuple(dct.items())[0]
            if action == 'leave':
                pass
            else:
                self.players[plr].set_action(self.name, action)

        return list(tmp_plrs.keys()), plrs_ai

    def _players_ai(self, plrs, plrs_ai):
        # setting players being ai
        if len(plrs) > 1:
            pass
        else:

            for plr in plrs:
                self.players[plr].set_street_ai(self.name)
        for plr in plrs_ai:
            self.players[plr].set_street_ai(self.name)

    def _get_initiative(self):
        try:
            player \
            = [pl for pl in self.players if
                      str(pl) == self._initiative][0]
        except IndexError:
            player = None
        _initiative = player
        return _initiative

    def get_players_start(self):
        return self.players

    def get_players_end(self):
        self.action()
        return self.players_end_

    def action(self):
        if not self.action_flg:
            self._action()
            plrs, plrs_ai = self._action2()
            self._players_ai(plrs, plrs_ai)
            self.action_flg = True
        return self.action_

    def action_possible(self):
        return 'AI' not in self.street[0]

    def ended_in_ai(self):
        # if everybody that leaves street is ai and it didn't end on this strt
        cnt = 0
        for name, player in self.get_players_end().items():
            if not player.get_street_ai_bool(self.name):
                return False
            else:
                cnt += 1
        return cnt > 1

    def players_ai(self):
        for name, player in self.get_players_start().items():
            if player.get_street_ai_bool(self.name):
                self.players_ai_[name] = player
        return self.players_ai_


class FacingOpp(object):
    def __init__(self, hand, street, player):
        self.hand = hand
        self.street_name = street.upper()
        self.street = hand.get_street(street)
        self.player = player
        self.players = hand.get_street_players(street)
        self.action = hand.actions[self.street_name]
        self.better = -1
        self.raiser = -1

    def _better(self):
        self.better = None
        self.better_ai = None
        pat = re.compile(r'^bet')
        pat_ai = re.compile(r'^bet AI')
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if pat.match(act):
                self.better = plr
                if pat_ai.match(act):
                    self.better_ai = plr
                break
        return self.better

    def _raiser(self):
        self.raiser = None
        self.raiser_ai = None
        pat = re.compile(r'^2bet')
        pat_ai = re.compile(r'^2bet AI')
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if pat.match(act):
                self.raiser = plr
                if pat_ai.match(act):
                    self.raiser_ai = plr
                break
        return self.raiser

    def _initiator(self):
        try:
            self.initiator = str(self.hand.initiative()[self.street_name])
            self.initiator = None if self.initiator == 'None' \
                else self.initiator
        except KeyError:
            self.initiator = None

    def _preflop_initiator(self):
        self.pre_initiator = str(self.hand.initiative()['FLOP'])
        self.pre_initiator = None if self.pre_initiator == 'None' \
            else self.pre_initiator

    def _dbetter(self):
        self.dbetter = None
        for plr in self.players:
            dbet = Db(self.hand, self.street_name, plr)
            if dbet.db():
                self.dbetter = plr
                break
        return self.dbetter

    def _cbetter(self, street_name):
        self.cbetter = None
        for plr in self.players:
            cbet = Cb(self.hand, street_name, plr)
            if cbet.cb():
                self.cbetter = plr
                break
        return self.cbetter

    def _vs_mcb_better(self):
        self.vs_mcb_better = None
        for plr in self.players:
            bet = BVsMcb(self.hand, self.street_name, plr)
            if bet.b_vs_mcb():
                self.vs_mcb_better = plr
                break
        return self.vs_mcb_better

    def _floater(self, street_name):
        self.floater = None
        for plr in self.players:
            float = Float(self.hand, street_name, plr)
            if float.float():
                self.floater = plr
                break
        return self.floater

    def _plr_missed_cbet(self, street_name):
        # returns player who could cbet but didn't on street_name (or None)
        plr1 = None
        for plr in self.players:
            cbet = Cb(self.hand, street_name, plr)
            if cbet.cb_opp() and not cbet.cb():
                plr1 = plr
                break
        return plr1

    def has_relative_position(self, plr, plr2):
        return self.players[plr].rel_pos_post_bool(self.players[plr2])


class Bet(FacingOpp):
    def __init__(self, hand, strit, player):
        FacingOpp.__init__(self, hand, strit, player)
        self.attrs = {}
        self._better()
        self._raiser()
        self.b_opp_flg = False
        self.b_raise_def_opp_flg = False
        self.b_def_opp_flg = False
        self.raise_raise_def_opp_flg = False

    def _go_to_action(self, action_name):
        # leaves only actions after the action_name
        pat = re.compile(r'^{}'.format(action_name))
        action = dict(self.action)
        ks = sorted(action.keys())
        for k in ks:
            plr, act = tuple(self.action[k].items())[0]
            if pat.match(act):
                action.pop(k)
                break
            action.pop(k)
        if not action:
            return None
        return action

    @staticmethod
    def hud_types():
        dct = {}
        dct['b_opp'] = 'BOOL'
        dct['b'] = 'BOOL'
        dct['b_def_opp'] = 'BOOL'
        dct['enum_b_def'] = 'VARCHAR(13)'
        dct['b_raise_def_opp'] = 'BOOL'
        dct['enum_b_raise_def'] = 'VARCHAR(13)'
        dct['raise_raise_def_opp'] = 'BOOL'
        dct['enum_raise_raise_def'] = 'VARCHAR(13)'
        return dct

    def b_opp(self):
        # mogl betowac
        if self.b_opp_flg:
            return self.attrs['b_opp']
        self.b_opp_flg = True

        pattern = re.compile(r'^bet')
        if self.players[self.player].get_street_ai_bool(self.street_name,
                                                        before=True):
            self.attrs['b_opp'] = False
            self.attrs['b'] = False
            return self.attrs['b_opp']

        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if plr == self.player:
                self.attrs['b_opp'] = True
                self.attrs['b'] = True if pattern.match(act) else False
                return self.attrs['b_opp']
            else:
                if 'bet' in act:
                    self.attrs['b_opp'] = False
                    self.attrs['b'] = False
                    return self.attrs['b_opp']
        else:
            # very rare occasion when everybody open folded before self.player
            self.attrs['b_opp'] = False
            self.attrs['b'] = False
            return self.attrs['b_opp']

    def b(self):
        # czy betowal
        try:
            return self.attrs['b']
        except KeyError:
            self.b_opp()
            return self.attrs['b']

    def b_def_opp(self):
        # czy mial okazje bronic sie przed betem
        if self.b_def_opp_flg:
            return self.attrs['b_def_opp']
        self.b_def_opp_flg = True

        if self.better is None or self.better == self.player:
            self.attrs['b_def_opp'] = False
            self.attrs['enum_b_def'] = None
            return self.attrs['b_def_opp']

        action = self._go_to_action('bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['b_def_opp'] = True
                    self.attrs['enum_b_def'] = act
                    return self.attrs['b_def_opp']
                if 'fold' not in act:
                    self.attrs['b_def_opp'] = False
                    self.attrs['enum_b_def'] = None
                    return self.attrs['b_def_opp']
        self.attrs['b_def_opp'] = False
        self.attrs['enum_b_def'] = None
        return self.attrs['b_def_opp']

    def enum_b_def(self):
        try:
            return self.attrs['enum_b_def']
        except KeyError:
            self.b_def_opp()
            return self.attrs['enum_b_def']

    def b_raise_def_opp(self):
        # if had opportunity to defend bet against 2bet
        if self.b_raise_def_opp_flg:
            return self.attrs['b_raise_def_opp']
        self.b_raise_def_opp_flg = True

        if self.better != self.player or self.raiser is None or\
                        self.better_ai is not None:
            self.attrs['b_raise_def_opp'] = False
            self.attrs['enum_b_raise_def'] = None
            return self.attrs['b_raise_def_opp']

        # players between bettor and raiser folded, and players between
        # raiser and bettor folded (= there can be only 2 players after this
        # action)
        action1 = self._go_to_action('bet')
        action2 = self._go_to_action('2bet')
        for k, v in action1.items():
            plr, act = tuple(v.items())[0]
            if plr == self.raiser:
                break
            if 'fold' not in act:
                self.attrs['b_raise_def_opp'] = False
                self.attrs['enum_b_raise_def'] = None
                return self.attrs['b_raise_def_opp']
        for k, v in action2.items():
            plr, act = tuple(v.items())[0]
            if plr == self.player:
                self.attrs['b_raise_def_opp'] = True
                self.attrs['enum_b_raise_def'] = act
                return self.attrs['b_raise_def_opp']
            if 'fold' not in act:
                self.attrs['b_raise_def_opp'] = False
                self.attrs['enum_b_raise_def'] = None
                return self.attrs['b_raise_def_opp']

    def enum_b_raise_def(self):
        try:
            return self.attrs['enum_b_raise_def']
        except KeyError:
            self.b_raise_def_opp()
            return self.attrs['enum_b_raise_def']

    def raise_raise_def_opp(self):
        # czy mial okazje bronic swojego raisa przeciwko raisowi
        if self.raise_raise_def_opp_flg:
            return self.attrs['raise_raise_def_opp']
        self.raise_raise_def_opp_flg = True

        if self.raiser != self.player or self.raiser_ai is not None:
            self.attrs['raise_raise_def_opp'] = False
            self.attrs['enum_raise_raise_def'] = None
            return self.attrs['raise_raise_def_opp']

        action2 = self._go_to_action('3bet')
        if action2 is None:
            self.attrs['raise_raise_def_opp'] = False
            self.attrs['enum_raise_raise_def'] = None
            return self.attrs['raise_raise_def_opp']

        action1 = self._go_to_action('2bet')
        for k, v in action1.items():
            plr, act = tuple(v.items())[0]
            if '3bet' in act:
                break
            if 'fold' not in act:
                self.attrs['raise_raise_def_opp'] = False
                self.attrs['enum_raise_raise_def'] = None
                return self.attrs['raise_raise_def_opp']

        for k, v in action2.items():
            plr, act = tuple(v.items())[0]
            if plr == self.player:
                self.attrs['raise_raise_def_opp'] = True
                self.attrs['enum_raise_raise_def'] = act
                return self.attrs['raise_raise_def_opp']

            if 'fold' not in act:
                self.attrs['raise_raise_def_opp'] = False
                self.attrs['enum_raise_raise_def'] = None
                return self.attrs['raise_raise_def_opp']

    def enum_raise_raise_def(self):
        # w jaki sposob reagowal na raise vs raise
        try:
            return self.attrs['enum_raise_raise_def']
        except KeyError:
            self.raise_raise_def_opp()
            return self.attrs['enum_raise_raise_def']


class Db(Bet):
    def __init__(self, hand, street, player, cache=None):
        Bet.__init__(self, hand, street, player)
        self.attrs = {}
        self._initiator()
        self.cache = cache
        self.dbetter = -1
        self.db_opp_flg = False
        self.db_def_opp_flg = False
        self.db_raise_def_opp_flg = False

    @staticmethod
    def hud_types():
        dct = {}
        dct['db_opp'] = 'BOOL'
        dct['db'] = 'BOOL'
        dct['db_def_opp'] = 'BOOL'
        dct['enum_db_def'] = 'VARCHAR(13)'
        dct['db_raise_def_opp'] = 'BOOL'
        dct['enum_db_raise_def'] = 'VARCHAR(13)'
        return dct

    def db_opp(self):
        # if could donk
        if self.db_opp_flg:
            return self.attrs['db_opp']
        self.db_opp_flg = True

        b_opp = self.b_opp() if self.cache is None else self.cache['b_opp']
        if not b_opp or self.initiator is None:
            self.attrs['db_opp'] = False
            self.attrs['db'] = False
            return self.attrs['db_opp']

        if self.has_relative_position(self.initiator, self.player):
            b = self.b() if self.cache is None else self.cache['b']
            self.attrs['db_opp'] = True
            self.attrs['db'] = b
            return self.attrs['db_opp']
        self.attrs['db_opp'] = False
        self.attrs['db'] = False
        return self.attrs['db_opp']

    def db(self):
        # if donked
        try:
            return self.attrs['db']
        except KeyError:
            self.db_opp()
            return self.attrs['db']

    def db_def_opp(self):
        # if could defend his initiative vs donkbet
        if self.db_def_opp_flg:
            return self.attrs['db_def_opp']
        self.db_def_opp_flg = True

        b_def_opp = self.b_def_opp() if self.cache is None else\
            self.cache['b_def_opp']
        if not b_def_opp:
            self.attrs['db_def_opp'] = False
            self.attrs['enum_db_def'] = None
            return self.attrs['db_def_opp']
        self._dbetter()
        if self.player == self.initiator and self.dbetter is not None:
            enum_b_def = self.enum_b_def() if self.cache is None else \
                self.cache['enum_b_def']
            self.attrs['db_def_opp'] = True
            self.attrs['enum_db_def'] = enum_b_def
            return self.attrs['db_def_opp']
        self.attrs['db_def_opp'] = False
        self.attrs['enum_db_def'] = None
        return self.attrs['db_def_opp']

    def enum_db_def(self):
        # w jaki sposob bronil sie przed donkiem
        try:
            return self.attrs['enum_db_def']
        except KeyError:
            self.db_def_opp()
            return self.attrs['enum_db_def']

    def db_raise_def_opp(self):
        # czy mial okazje bronic swojego donka przeciwko raisowi
        if self.db_raise_def_opp_flg:
            return self.attrs['db_raise_def_opp']
        self.db_raise_def_opp_flg = True

        b_raise_def_opp = self.b_raise_def_opp() if self.cache is None else\
            self.cache['b_raise_def_opp']
        if self.db() and b_raise_def_opp:
            enum_b_raise_def = self.enum_b_raise_def() if \
                self.cache is None else self.cache['enum_b_raise_def']
            self.attrs['db_raise_def_opp'] = True
            self.attrs['enum_db_raise_def'] = enum_b_raise_def
            return self.attrs['db_raise_def_opp']
        self.attrs['db_raise_def_opp'] = False
        self.attrs['enum_db_raise_def'] = None
        return self.attrs['db_raise_def_opp']

    def enum_db_raise_def(self):
        # w jakis sposob reagowal na raise vs donk
        try:
            return self.attrs['enum_db_raise_def']
        except KeyError:
            self.db_raise_def_opp()
            return self.attrs['enum_db_raise_def']


class Cb(Db):
    def __init__(self, hand, street, player, cache=None):
        Db.__init__(self, hand, street, player)
        self.attrs = {}
        self.cache = cache
        self._preflop_initiator()
        self.cbetter = -1
        self.cb_opp_flg = False
        self.cb_def_opp_flg = False
        self.cb_raise_def_opp_flg = False


    @staticmethod
    def hud_types():
        dct = {}
        dct['cb_opp'] = 'BOOL'
        dct['cb'] = 'BOOL'
        dct['cb_def_opp'] = 'BOOL'
        dct['enum_cb_def'] = 'VARCHAR(13)'
        dct['cb_raise_def_opp'] = 'BOOL'
        dct['enum_cb_raise_def'] = 'VARCHAR(13)'
        return dct

    def cb_opp(self):
        # mogl cbetowac
        if self.cb_opp_flg:
            return self.attrs['cb_opp']
        self.cb_opp_flg = True

        b_opp = self.b_opp() if self.cache is None else self.cache['b_opp']
        if self.initiator is None or self.initiator != self.player or not b_opp or self.pre_initiator != self.player:
            self.attrs['cb_opp'] = False
            self.attrs['cb'] = False
            return self.attrs['cb_opp']
        b = self.b() if self.cache is None else self.cache['b']
        self.attrs['cb_opp'] = True
        self.attrs['cb'] = b
        return self.attrs['cb_opp']

    def cb(self):
        # czy cbetowal
        try:
            return self.attrs['cb']
        except KeyError:
            self.cb_opp()
            return self.attrs['cb']

    def cb_def_opp(self):
        # czy mial okazje bronic sie przed cbetem
        if self.cb_def_opp_flg:
            return self.attrs['cb_def_opp']
        self.cb_def_opp_flg = True

        b_def_opp = self.b_def_opp() if self.cache is None else self.cache['b_def_opp']
        if not b_def_opp:
            self.attrs['cb_def_opp'] = False
            self.attrs['enum_cb_def'] = None
            return self.attrs['cb_def_opp']
        self._cbetter(self.street_name)
        if self.cbetter is not None:
            enum_b_def = self.enum_b_def() if self.cache is None else self.cache[
                'enum_b_def']
            self.attrs['cb_def_opp'] = True
            self.attrs['enum_cb_def'] = enum_b_def
            return self.attrs['cb_def_opp']
        self.attrs['cb_def_opp'] = False
        self.attrs['enum_cb_def'] = None
        return self.attrs['cb_def_opp']

    def enum_cb_def(self):
        # w jaki sposob bronil sie przed cbetem
        try:
            return self.attrs['enum_cb_def']
        except KeyError:
            self.cb_def_opp()
            return self.attrs['enum_cb_def']

    def cb_raise_def_opp(self):
        # czy mial okazje bronic swojego cbeta przeciwko raisowi
        if self.cb_raise_def_opp_flg:
            return self.attrs['cb_raise_def_opp']
        self.cb_raise_def_opp_flg = True


        b_raise_def_opp = self.b_raise_def_opp() if self.cache is None else self.cache['b_raise_def_opp']
        if self.cb() and b_raise_def_opp:
            enum_b_raise_def = self.enum_b_raise_def() if self.cache is None else self.cache[
                'enum_b_raise_def']
            self.attrs['cb_raise_def_opp'] = True
            self.attrs['enum_cb_raise_def'] = enum_b_raise_def
            return self.attrs['cb_raise_def_opp']
        self.attrs['cb_raise_def_opp'] = False
        self.attrs['enum_cb_raise_def'] = None
        return self.attrs['cb_raise_def_opp']

    def enum_cb_raise_def(self):
        # w jaki sposob reagowal na raise vs donk
        try:
            return self.attrs['enum_cb_raise_def']
        except KeyError:
            self.cb_raise_def_opp()
            return self.attrs['enum_cb_raise_def']


class BVsMcb(Cb):
    def __init__(self, hand, street, player, cache=None):
        Cb.__init__(self, hand, street, player)
        self.attrs = {}
        self.cache = cache
        self.b_vs_mcb_opp_flg = False
        self.b_vs_mcb_def_opp_flg = False
        self.b_vs_mcb_raise_def_opp_flg = False


    @staticmethod
    def hud_types():
        dct = {}
        dct['b_vs_mcb_opp'] = 'BOOL'
        dct['b_vs_mcb'] = 'BOOL'
        dct['b_vs_mcb_def_opp'] = 'BOOL'
        dct['enum_b_vs_mcb_def'] = 'VARCHAR(13)'
        dct['b_vs_mcb_raise_def_opp'] = 'BOOL'
        dct['enum_b_vs_mcb_raise_def'] = 'VARCHAR(13)'
        return dct

    def b_vs_mcb_opp(self):
        # mustn't be preflop agresor
        if self.b_vs_mcb_opp_flg:
            return self.attrs['b_vs_mcb_opp']
        self.b_vs_mcb_opp_flg = True

        b_opp = self.b_opp() if self.cache is None else self.cache['b_opp']
        if self.player == self.pre_initiator or not b_opp:
            self.attrs['b_vs_mcb_opp'] = False
            self.attrs['b_vs_mcb'] = False
            return self.attrs['b_vs_mcb_opp']
        player = self._plr_missed_cbet(self.street - 1)
        # if on last street someone missed cbet, i have to be out of position
        # and no one could bet on last street (= initiative == None)
        if player is not None:
            if self.has_relative_position(self.player, player):
                self.attrs['b_vs_mcb_opp'] = False
                self.attrs['b_vs_mcb'] = False
                return self.attrs['b_vs_mcb_opp']
            init = self.hand.get_init_street(self.street_name)

            if init is None:
                b = self.b() if self.cache is None else self.cache['b']
                self.attrs['b_vs_mcb_opp'] = True
                self.attrs['b_vs_mcb'] = b
                return self.attrs['b_vs_mcb_opp']
            self.attrs['b_vs_mcb_opp'] = False
            self.attrs['b_vs_mcb'] = False
            return self.attrs['b_vs_mcb_opp']
        else:
            player = self._plr_missed_cbet(self.street_name)
            if player is None:
                self.attrs['b_vs_mcb_opp'] = False
                self.attrs['b_vs_mcb'] = False
                return self.attrs['b_vs_mcb_opp']
            if self.has_relative_position(self.player, player):
                b = self.b() if self.cache is None else self.cache['b']
                self.attrs['b_vs_mcb_opp'] = True
                self.attrs['b_vs_mcb'] = b
                return self.attrs['b_vs_mcb_opp']
            self.attrs['b_vs_mcb_opp'] = False
            self.attrs['b_vs_mcb'] = False
            return self.attrs['b_vs_mcb_opp']

    def b_vs_mcb(self):
        # czy gral b_vs_mcb
        try:
            return self.attrs['b_vs_mcb']
        except KeyError:
            self.b_vs_mcb_opp()
            return self.attrs['b_vs_mcb']

    def b_vs_mcb_def_opp(self):
        if self.b_vs_mcb_def_opp_flg:
            return self.attrs['b_vs_mcb_def_opp']
        self.b_vs_mcb_def_opp_flg = True

        b_def_opp = self.b_def_opp() if self.cache is None else self.cache['b_def_opp']
        if not b_def_opp:
            self.attrs['b_vs_mcb_def_opp'] = False
            self.attrs['enum_b_vs_mcb_def'] = None
            return self.attrs['b_vs_mcb_def_opp']
        self._vs_mcb_better()
        if self.vs_mcb_better is None:
            self.attrs['b_vs_mcb_def_opp'] = False
            self.attrs['enum_b_vs_mcb_def'] = None
            return self.attrs['b_vs_mcb_def_opp']

        if self.has_relative_position(self.vs_mcb_better, self.player):
            cbet = Cb(self.hand, self.street_name, self.player)
            if cbet.cb_opp():
                enum_b_def = self.enum_b_def() if self.cache is None else \
                self.cache['enum_b_def']
                self.attrs['b_vs_mcb_def_opp'] = True
                self.attrs['enum_b_vs_mcb_def'] = enum_b_def
                return self.attrs['b_vs_mcb_def_opp']
            self.attrs['b_vs_mcb_def_opp'] = False
            self.attrs['enum_b_vs_mcb_def'] = None
            return self.attrs['b_vs_mcb_def_opp']
        else:
            last_street = self.hand.get_street(self.street - 1)
            cbet = Cb(self.hand, last_street.name, self.player)
            if cbet.cb_opp() and not cbet.cb():
                enum_b_def = self.enum_b_def() if self.cache is None else \
                self.cache['enum_b_def']
                self.attrs['b_vs_mcb_def_opp'] = True
                self.attrs['enum_b_vs_mcb_def'] = enum_b_def
                return self.attrs['b_vs_mcb_def_opp']
            self.attrs['b_vs_mcb_def_opp'] = False
            self.attrs['enum_b_vs_mcb_def'] = None
            return self.attrs['b_vs_mcb_def_opp']

    def enum_b_vs_mcb_def(self):
        # w jaki sposob bronil sie przed b_vs_mcb
        try:
            return self.attrs['enum_b_vs_mcb_def']
        except KeyError:
            self.b_vs_mcb_def_opp()
            return self.attrs['enum_b_vs_mcb_def']

    def b_vs_mcb_raise_def_opp(self):
        # czy mial okazje bronic swojego b_vs_mcb przeciwko raisowi
        if self.b_vs_mcb_raise_def_opp_flg:
            return self.attrs['b_vs_mcb_raise_def_opp']
        self.b_vs_mcb_raise_def_opp_flg = True

        b_raise_def_opp = self.b_raise_def_opp() if self.cache is None else self.cache['b_raise_def_opp']
        if self.b_vs_mcb() and b_raise_def_opp:
            enum_b_raise_def = self.enum_b_raise_def() if self.cache is None else self.cache[
                'enum_b_raise_def']
            self.attrs['b_vs_mcb_raise_def_opp'] = True
            self.attrs['enum_b_vs_mcb_raise_def'] = enum_b_raise_def
            return self.attrs['b_vs_mcb_raise_def_opp']
        self.attrs['b_vs_mcb_raise_def_opp'] = False
        self.attrs['enum_b_vs_mcb_raise_def'] = None
        return self.attrs['b_vs_mcb_raise_def_opp']

    def enum_b_vs_mcb_raise_def(self):
        # w jakis sposob reagowal na raise vs b_vs_mcb
        try:
            return self.attrs['enum_b_vs_mcb_raise_def']
        except KeyError:
            self.b_vs_mcb_raise_def_opp()
            return self.attrs['enum_b_vs_mcb_raise_def']


class Float(BVsMcb):
    # make double float???
    def __init__(self, hand, street, player, cache=None):
        BVsMcb.__init__(self, hand, street, player)
        self.attrs = {}
        self.cache = cache
        self.floater = -1
        self.float_opp_flg = False
        self.float_def_opp_flg = False
        self.float_raise_def_opp_flg = False


    @staticmethod
    def hud_types():
        dct = {}
        dct['float_opp'] = 'BOOL'
        dct['float'] = 'BOOL'
        dct['float_def_opp'] = 'BOOL'
        dct['enum_float_def'] = 'VARCHAR(13)'
        dct['float_raise_def_opp'] = 'BOOL'
        dct['enum_float_raise_def'] = 'VARCHAR(13)'
        return dct

    def float_opp(self):
        if self.float_opp_flg:
            return self.attrs['float_opp']
        self.float_opp_flg = True

        b_opp = self.b_opp() if self.cache is None else self.cache['b_opp']
        if not b_opp:
            self.attrs['float_opp'] = False
            self.attrs['float'] = False
            return self.attrs['float_opp']

        self._cbetter('FLOP')
        if self.cbetter is None:
            self.attrs['float_opp'] = False
            self.attrs['float'] = False
            return self.attrs['float_opp']

        if self.has_relative_position(self.player, self.cbetter):
            last_street = self.hand.get_street(self.street - 1)
            cbet = Cb(self.hand, last_street.name, self.player)
            if cbet.cb_def_opp() and self.b_vs_mcb_opp() and len(
                    self.street.get_players_start()) == 2:
                self.attrs['float_opp'] = True
                self.attrs['float'] = self.b_vs_mcb()
                return self.attrs['float_opp']
            self.attrs['float_opp'] = False
            self.attrs['float'] = False
            return self.attrs['float_opp']
        else:
            init = self.hand.get_init_street(self.street_name)
            if init is None:
                num = len(self.street.get_players_start())
                if self.b_vs_mcb_opp() and num == 2:
                    self.attrs['float_opp'] = True
                    self.attrs['float'] = self.b_vs_mcb()
                    return self.attrs['float_opp']
                self.attrs['float_opp'] = False
                self.attrs['float'] = False
                return self.attrs['float_opp']
            self.attrs['float_opp'] = False
            self.attrs['float'] = False
            return self.attrs['float_opp']

    def float(self):
        # czy gral float
        try:
            return self.attrs['float']
        except KeyError:
            self.float_opp()
            return self.attrs['float']

    def float_def_opp(self):
        if self.float_def_opp_flg:
            return self.attrs['float_def_opp']
        self.float_def_opp_flg = True

        b_def_opp = self.b_def_opp() if self.cache is None else\
            self.cache['b_def_opp']
        if not b_def_opp:
            self.attrs['float_def_opp'] = False
            self.attrs['enum_float_def'] = None
            return self.attrs['float_def_opp']
        if self.floater == -1:
            self._floater(self.street_name)
        if self.floater is None:
            self.attrs['float_def_opp'] = False
            self.attrs['enum_float_def'] = None
            return self.attrs['float_def_opp']

        self.attrs['float_def_opp'] = True
        self.attrs['enum_float_def'] = self.enum_b_def()
        return self.attrs['float_def_opp']

    def enum_float_def(self):
        # w jaki sposob bronil sie przed float
        try:
            return self.attrs['enum_float_def']
        except KeyError:
            self.float_def_opp()
            return self.attrs['enum_float_def']

    def float_raise_def_opp(self):
        # czy mial okazje bronic swojego float przeciwko raisowi
        if self.float_raise_def_opp_flg:
            return self.attrs['float_raise_def_opp']
        self.float_raise_def_opp_flg = True

        b_raise_def_opp = self.b_raise_def_opp() if self.cache is None else\
            self.cache['b_raise_def_opp']
        if not b_raise_def_opp:
            self.attrs['float_raise_def_opp'] = False
            self.attrs['enum_float_raise_def'] = None
            return self.attrs['float_raise_def_opp']
        if self.floater == -1:
            self._floater(self.street_name)
        if self.floater is None or self.floater != self.player:
            self.attrs['float_raise_def_opp'] = False
            self.attrs['enum_float_raise_def'] = None
            return self.attrs['float_raise_def_opp']

        self.attrs['float_raise_def_opp'] = True
        self.attrs['enum_float_raise_def'] = self.enum_b_raise_def()
        return self.attrs['float_raise_def_opp']

    def enum_float_raise_def(self):
        # w jakis sposob reagowal na raise vs float
        try:
            return self.attrs['enum_float_raise_def']
        except KeyError:
            self.float_raise_def_opp()
            return self.attrs['enum_float_raise_def']


class Aggression(FacingOpp):
    @staticmethod
    def hud_types():
        dct = {}
        dct['call'] = 'SMALLINT'
        dct['aggr'] = 'SMALLINT'
        return dct

    def call(self):
        # how many calls
        if self.players[self.player].get_street_ai_bool(self.street_name,
                                                        before=True):
            return -1
        pat = re.compile(r'^call')
        action = self.players[self.player].get_street_action(self.street_name)
        if action is None:
            # very rare occasion when everybody open folded before self.player
            return -1

        how_many = 0
        for act in action:
            if pat.match(act):
                how_many += 1
        return how_many

    def aggr(self):
        # how many aggro plays
        if self.players[self.player].get_street_ai_bool(self.street_name,
                                                        before=True):
            return -1
        action = self.players[self.player].get_street_action(self.street_name)
        if action is None:
            # very rare occasion when everybody open folded before self.player
            return -1
        how_many = 0
        for act in action:
            tmp = Act(act)
            if tmp.type == 'aggr':
                how_many += 1
        return how_many


class Preflop(object):
    def __init__(self, hand, player):
        self.hand = hand
        self.street_name = 'PREFLOP'
        self.street = hand.get_street('PREFLOP')
        self.player = player
        self.players = hand.get_street_players('PREFLOP')
        self.plr = self.players[player]
        self.action = hand.actions['PREFLOP']
        self.betters_flg = False
        self.attrs = {}

    def _betters(self):
        # sets _3better, squeezer, opener
        if not self.betters_flg:
            self.betters_flg = True
        self.callers = []
        self.thief = None
        self.limper = None
        self._3better = None
        self.squeezer = None
        self.opener = None
        flat_flg = False
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if '3bet' in act:
                if not flat_flg:
                    self._3better = plr
                else:
                    self.squeezer = plr
                break
            if 'flat' in act:
                flat_flg = True
                self.callers.append(plr)
            elif 'open' in act:
                self.opener = plr
                tmp = self.players[plr]
                if tmp.get_position() == 'SB' or tmp.get_position() == 'BU':
                    self.thief = plr
            elif 'limp' in act:
                self.limper = plr

    def _go_to_action(self, action_name):
        # leaves only actions after the action_name
        pat = re.compile(r'^{}'.format(action_name))
        action = copy.copy(self.action)
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if pat.match(act):
                action.pop(k)
                break
            action.pop(k)
        if not action:
            return None
        return action

    @staticmethod
    def hud_types():
        dct = {}
        dct['open_opp'] = 'BOOL'
        dct['open_'] = 'BOOL'
        dct['three_bet_opp'] = 'BOOL'
        dct['three_bet'] = 'BOOL'
        dct['three_bet_def_opp'] = 'BOOL'
        dct['enum_three_bet_def'] = 'VARCHAR(13)'
        dct['four_bet_def_opp'] = 'BOOL'
        dct['enum_four_bet_def'] = 'VARCHAR(13)'
        dct['five_bet_def_opp'] = 'BOOL'
        dct['enum_five_bet_def'] = 'VARCHAR(13)'
        dct['cold_four_bet_opp'] = 'BOOL'
        dct['cold_four_bet'] = 'BOOL'
        dct['cold_four_bet_def_opp'] = 'BOOL'
        dct['enum_cold_four_bet_def'] = 'VARCHAR(13)'
        dct['flat_opp'] = 'BOOL'
        dct['flat'] = 'BOOL'
        dct['izo_opp'] = 'BOOL'
        dct['izo'] = 'BOOL'
        dct['sqz_opp'] = 'BOOL'
        dct['sqz'] = 'BOOL'
        dct['sqz_def_opp'] = 'BOOL'
        dct['enum_sqz_def'] = 'VARCHAR(13)'
        dct['steal_opp'] = 'BOOL'
        dct['steal'] = 'BOOL'
        dct['steal_def_opp'] = 'BOOL'
        dct['enum_steal_def'] = 'VARCHAR(13)'
        return dct

    def open_opp(self):
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if plr == self.player:
                self.attrs['open_opp'] = True
                self.attrs['open_'] = 'open' in act
                return self.attrs['open_opp']
            if 'fold' not in act:
                self.attrs['open_opp'] = False
                self.attrs['open_'] = False
                return self.attrs['open_opp']

    def open_(self):
        try:
            return self.attrs['open_']
        except KeyError:
            self.open_opp()
            return self.attrs['open_']

    def three_bet_opp(self):
        open_flg, flat_flg = False, False
        for k, v in self.action.items():
            plr, act = tuple(v.items())[0]
            if plr == self.player:
                if open_flg and not flat_flg:
                    self.attrs['three_bet_opp'] = True
                    self.attrs['three_bet'] = '3bet' in act
                    return self.attrs['three_bet_opp']
                self.attrs['three_bet_opp'] = False
                self.attrs['three_bet'] = False
                return self.attrs['three_bet_opp']
            if 'open' in act:
                open_flg = True
            if 'flat' in act:
                flat_flg = True

    def three_bet(self):
        try:
            return self.attrs['three_bet']
        except KeyError:
            self.three_bet_opp()
            return self.attrs['three_bet']

    def three_bet_def_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.opener is None or self.opener != self.player or \
                        self._3better is None:
            self.attrs['three_bet_def_opp'] = False
            self.attrs['enum_three_bet_def'] = None
            return self.attrs['three_bet_def_opp']
        action = self._go_to_action('3bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['three_bet_def_opp'] = True
                    self.attrs['enum_three_bet_def'] = act
                    return self.attrs['three_bet_def_opp']
                if 'fold' not in act:
                    self.attrs['three_bet_def_opp'] = False
                    self.attrs['enum_three_bet_def'] = None
                    return self.attrs['three_bet_def_opp']
        self.attrs['three_bet_def_opp'] = False
        self.attrs['enum_three_bet_def'] = None
        return self.attrs['three_bet_def_opp']

    def enum_three_bet_def(self):
        try:
            return self.attrs['enum_three_bet_def']
        except KeyError:
            self.three_bet_def_opp()
            return self.attrs['enum_three_bet_def']

    def four_bet_def_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.player != self._3better and self.player != self.squeezer:
            self.attrs['four_bet_def_opp'] = False
            self.attrs['enum_four_bet_def'] = None
            return self.attrs['four_bet_def_opp']
        action = self._go_to_action('3bet')
        if action is not None:
            pat = re.compile(r'^4bet')
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['four_bet_def_opp'] = True
                    self.attrs['enum_four_bet_def'] = act
                    return self.attrs['four_bet_def_opp']
                if 'fold' not in act and not pat.match(act):
                    self.attrs['four_bet_def_opp'] = False
                    self.attrs['enum_four_bet_def'] = None
                    return self.attrs['four_bet_def_opp']
        self.attrs['four_bet_def_opp'] = False
        self.attrs['enum_four_bet_def'] = None
        return self.attrs['four_bet_def_opp']

    def enum_four_bet_def(self):
        try:
            return self.attrs['enum_four_bet_def']
        except KeyError:
            self.four_bet_def_opp()
            return self.attrs['enum_four_bet_def']

    def five_bet_def_opp(self):
        action = self.plr.get_street_action('PREFLOP')
        if '4bet' not in action and '4bet AI' not in action:
            self.attrs['five_bet_def_opp'] = False
            self.attrs['enum_five_bet_def'] = None
            return self.attrs['five_bet_def_opp']
        action = self._go_to_action('5bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['five_bet_def_opp'] = True
                    self.attrs['enum_five_bet_def'] = act
                    return self.attrs['five_bet_def_opp']
                if '6bet' in act:
                    self.attrs['five_bet_def_opp'] = False
                    self.attrs['enum_five_bet_def'] = None
                    return self.attrs['five_bet_def_opp']
        self.attrs['five_bet_def_opp'] = False
        self.attrs['enum_five_bet_def'] = None
        return self.attrs['five_bet_def_opp']

    def enum_five_bet_def(self):
        try:
            return self.attrs['enum_five_bet_def']
        except KeyError:
            self.five_bet_def_opp()
            return self.attrs['enum_five_bet_def']

    def cold_four_bet_opp(self):
        action = self._go_to_action('3bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['cold_four_bet_opp'] = True
                    self.attrs['cold_four_bet'] = '4bet' in act
                    return self.attrs['cold_four_bet_opp']
                if 'fold' not in act:
                    self.attrs['cold_four_bet_opp'] = False
                    self.attrs['cold_four_bet'] = False
                    return self.attrs['cold_four_bet_opp']
            self.attrs['cold_four_bet_opp'] = False
            self.attrs['cold_four_bet'] = False
            return self.attrs['cold_four_bet_opp']
        self.attrs['cold_four_bet_opp'] = False
        self.attrs['cold_four_bet'] = False
        return self.attrs['cold_four_bet_opp']

    def cold_four_bet(self):
        try:
            return self.attrs['cold_four_bet']
        except KeyError:
            self.cold_four_bet_opp()
            return self.attrs['cold_four_bet']

    def cold_four_bet_def_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.player != self._3better and self.player != self.squeezer:
            self.attrs['cold_four_bet_def_opp'] = False
            self.attrs['enum_cold_four_bet_def'] = None
            return self.attrs['cold_four_bet_def_opp']
        cold4better = None
        for pl in self.players:
            tmp = Preflop(self.hand, pl)
            if tmp.cold_four_bet():
                cold4better = pl
        if cold4better is None:
            self.attrs['cold_four_bet_def_opp'] = False
            self.attrs['enum_cold_four_bet_def'] = None
            return self.attrs['cold_four_bet_def_opp']
        action = self._go_to_action('4bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['cold_four_bet_def_opp'] = True
                    self.attrs['enum_cold_four_bet_def'] = act
                    return self.attrs['cold_four_bet_def_opp']
                if 'fold' not in act:
                    self.attrs['cold_four_bet_def_opp'] = False
                    self.attrs['enum_cold_four_bet_def'] = None
                    return self.attrs['cold_four_bet_def_opp']
        self.attrs['cold_four_bet_def_opp'] = False
        self.attrs['enum_cold_four_bet_def'] = None
        return self.attrs['cold_four_bet_def_opp']

    def enum_cold_four_bet_def(self):
        try:
            return self.attrs['enum_cold_four_bet_def']
        except KeyError:
            self.cold_four_bet_def_opp()
            return self.attrs['enum_cold_four_bet_def']

    def flat_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.opener is None:
            self.attrs['flat_opp'] = False
            self.attrs['flat'] = False
            return self.attrs['flat_opp']
        action = self._go_to_action('open')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['flat_opp'] = True
                    self.attrs['flat'] = 'flat' in act
                    return self.attrs['flat_opp']
                if '3bet' in act:
                    self.attrs['flat_opp'] = False
                    self.attrs['flat'] = False
                    return self.attrs['flat_opp']
        self.attrs['flat_opp'] = False
        self.attrs['flat'] = False
        return self.attrs['flat_opp']

    def flat(self):
        try:
            return self.attrs['flat']
        except KeyError:
            self.flat_opp()
            return self.attrs['flat']

    def izo_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.limper is None:
            self.attrs['izo_opp'] = False
            self.attrs['izo'] = False
            return self.attrs['izo_opp']
        action = self._go_to_action('limp')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['izo_opp'] = True
                    self.attrs['izo'] = 'open' in act
                    return self.attrs['izo_opp']
                if 'open' in act:
                    self.attrs['izo_opp'] = False
                    self.attrs['izo'] = False
                    return self.attrs['izo_opp']
        self.attrs['izo_opp'] = False
        self.attrs['izo'] = False
        return self.attrs['izo_opp']

    def izo(self):
        try:
            return self.attrs['izo']
        except KeyError:
            self.izo_opp()
            return self.attrs['izo']

    def sqz_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.opener is None:
            self.attrs['sqz_opp'] = False
            self.attrs['sqz'] = False
            return self.attrs['sqz_opp']
        action = self._go_to_action('flat')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['sqz_opp'] = True
                    self.attrs['sqz'] = '3bet' in act
                    return self.attrs['sqz_opp']
                if '3bet' in act:
                    self.attrs['sqz_opp'] = False
                    self.attrs['sqz'] = False
                    return self.attrs['sqz_opp']
        self.attrs['sqz_opp'] = False
        self.attrs['sqz'] = False
        return self.attrs['sqz_opp']

    def sqz(self):
        try:
            return self.attrs['sqz']
        except KeyError:
            self.sqz_opp()
            return self.attrs['sqz']

    def sqz_def_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.squeezer is None or self.squeezer == self.player:
            self.attrs['sqz_def_opp'] = False
            self.attrs['enum_sqz_def'] = None
            return self.attrs['sqz_def_opp']
        if self.opener != self.player and self.player not in self.callers:
            self.attrs['sqz_def_opp'] = False
            self.attrs['enum_sqz_def'] = None
            return self.attrs['sqz_def_opp']
        action = self._go_to_action('3bet')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['sqz_def_opp'] = True
                    self.attrs['enum_sqz_def'] = act
                    return self.attrs['sqz_def_opp']
                if 'fold' not in act:
                    self.attrs['sqz_def_opp'] = False
                    self.attrs['enum_sqz_def'] = None
                    return self.attrs['sqz_def_opp']
        self.attrs['sqz_def_opp'] = False
        self.attrs['enum_sqz_def'] = None
        return self.attrs['sqz_def_opp']

    def enum_sqz_def(self):
        try:
            return self.attrs['enum_sqz_def']
        except KeyError:
            self.sqz_def_opp()
            return self.attrs['enum_sqz_def']

    def steal_opp(self):
        try:
            if self.attrs['open_opp'] and (self.plr.get_position() == 'SB'
                                           or self.plr.get_position() == 'BU'):
                self.attrs['steal_opp'] = True
                self.attrs['steal'] = self.attrs['open']
                return self.attrs['steal_opp']
            self.attrs['steal_opp'] = False
            self.attrs['steal'] = False
            return self.attrs['steal_opp']
        except KeyError:
            self.open_opp()
        if self.attrs['open_opp'] and (self.plr.get_position() == 'SB'
                                       or self.plr.get_position() == 'BU'):
            self.attrs['steal_opp'] = True
            self.attrs['steal'] = self.attrs['open_']
            return self.attrs['steal_opp']
        self.attrs['steal_opp'] = False
        self.attrs['steal'] = False
        return self.attrs['steal_opp']

    def steal(self):
        try:
            return self.attrs['steal']
        except KeyError:
            self.steal_opp()
            return self.attrs['steal']

    def steal_def_opp(self):
        if not self.betters_flg:
            self._betters()
        if self.thief is None:
            self.attrs['steal_def_opp'] = False
            self.attrs['enum_steal_def'] = None
            return self.attrs['steal_def_opp']
        action = self._go_to_action('open')
        if action is not None:
            for k, v in action.items():
                plr, act = tuple(v.items())[0]
                if plr == self.player:
                    self.attrs['steal_def_opp'] = True
                    self.attrs['enum_steal_def'] = act
                    return self.attrs['steal_def_opp']
                if 'fold' not in act:
                    self.attrs['steal_def_opp'] = False
                    self.attrs['enum_steal_def'] = None
                    return self.attrs['steal_def_opp']
            self.attrs['steal_def_opp'] = False
            self.attrs['enum_steal_def'] = None
            return self.attrs['steal_def_opp']
        self.attrs['steal_def_opp'] = False
        self.attrs['enum_steal_def'] = None
        return self.attrs['steal_def_opp']

    def enum_steal_def(self):
        try:
            return self.attrs['enum_steal_def']
        except KeyError:
            self.steal_def_opp()
            return self.attrs['enum_steal_def']


class PreflopEvaluate(Preflop):
    def __init__(self, hand):
        self.hand = hand
        self.players = hand.get_street_players('PREFLOP')
        self.players_names = [str(pl) for pl in self.players]

    def evaluate(self):
        dct = dict()
        methods = self.hud_types().keys()
        for player in self.players_names:
            instance = Preflop(self.hand, player)
            try:
                dct_tmp = dict()
                for method in methods:
                    tmp = eval('instance.%s()' % method)
                    tmp = 'None' if tmp is None else tmp
                    dct_tmp[method] = tmp
                dct[player] = dct_tmp
            except:
                # one in ~100k hands fails (AI before preflop, limp AI)
                pass
        return dct


class PlayerGeneral(object):
    def __init__(self, hand, player):
        self.hand = hand
        self.player = player
        self.players = hand.get_players()
        self.zwyciezca = -1

    @staticmethod
    def hud_types():
        dct = {}
        dct['sd'] = 'BOOL'
        dct['wsd'] = 'BOOL'
        dct['sf'] = 'BOOL'
        dct['st'] = 'BOOL'
        dct['sr'] = 'BOOL'
        dct['ai'] = 'CHAR(7)'
        dct['pos_nr'] = 'SMALLINT'
        return dct

    def sd(self):
        # czy gracz zobaczyl sd
        help = HandGeneral(self.hand)
        self.zwyciezca = None
        if not help.sd():
            return False
        graczeNaSd = []
        sd = re.compile(r'(.*): shows .*')
        wsd = re.compile(r'(.*) collected .*')
        for line in self.hand:
            cos = sd.search(line)
            if cos is not None:
                graczeNaSd.append(cos.group(1))
            else:
                cos = wsd.search(line)
                if cos is not None:
                    self.zwyciezca = cos.group(1)

        return str(self.player) in graczeNaSd

    def wsd(self):
        # czy gracz wygral sd
        if self.zwyciezca == -1:
            self.sd()
        return self.player == self.zwyciezca

    def sf(self):
        # czy gracz zobaczyl flopa
        if self.hand.get_street_bool('FLOP'):
            lst = [str(p) for p in self.hand.get_street_players('FLOP')]
            return self.player in lst
        return False

    def st(self):
        # czy gracz zobaczyl turn
        if self.hand.get_street_bool('TURN'):
            lst = [str(p) for p in self.hand.get_street_players('TURN')]
            return self.player in lst
        return False

    def sr(self):
        # czy gracz zobaczyl river
        if self.hand.get_street_bool('RIVER'):
            lst = [str(p) for p in self.hand.get_street_players('RIVER')]
            return self.player in lst
        return False

    def ai(self):
        # strit na ktorym gracz poszedl AI, lub None jak nie poszedl na zadnym
        return self.players[self.player].get_street_ai()

    def pos_nr(self):
        return self.players[self.player].hud_position_nr()


class HandGeneral(object):
    def __init__(self, hand):
        self.hand = hand
        self.players = hand.get_players()
        self.opener = -1
        self.three_better = -1
        self.four_better = -1

    def _betters(self):
        self.opener = None
        self.three_better = None
        self.four_better = None
        pat1 = re.compile(r'^open')
        pat2 = re.compile(r'^3bet')
        pat3 = re.compile(r'^4bet')

        for k, v in self.hand.get_street_action('PREFLOP').items():
            plr, act = tuple(v.items())[0]
            if pat1.match(act):
                self.opener = self.players[plr]
            elif pat2.match(act):
                self.three_better = self.players[plr]
            elif pat3.match(act):
                self.four_better = self.players[plr]

    @staticmethod
    def hud_types():
        dct = {}
        dct['sd'] = 'BOOL'
        dct['sf'] = 'BOOL'
        dct['st'] = 'BOOL'
        dct['sr'] = 'BOOL'
        dct['ai'] = 'CHAR(7)'
        dct['pot_2bet'] = 'BOOL'
        dct['pot_3bet'] = 'BOOL'
        dct['pot_4bet'] = 'BOOL'
        dct['pot_5bet_plus'] = 'BOOL'
        dct['open_pos_nr'] = 'SMALLINT'
        dct['three_bet_pos_nr'] = 'SMALLINT'
        dct['four_bet_pos_nr'] = 'SMALLINT'
        dct['nr_of_players'] = 'SMALLINT'
        return dct

    def sd(self):
        # czy byl sd
        return self.hand.get_sd_bool()

    def sf(self):
        # czy byl flop
        return self.hand.get_street_bool('FLOP')

    def st(self):
        # czy byl turn
        return self.hand.get_street_bool('TURN')

    def sr(self):
        # czy byl river
        return self.hand.get_street_bool('RIVER')

    def pot_2bet(self):
        # czy to byl srp
        pre = self.hand.get_street('PREFLOP')
        return self.sf() and self.ai() != 'PREFLOP' and pre.how_many_aggr == 1

    def pot_3bet(self):
        # czy to byl 3bp
        pre = self.hand.get_street('PREFLOP')
        return self.sf() and self.ai() != 'PREFLOP' and pre.how_many_aggr == 2

    def pot_4bet(self):
        # czy to byl 4bp
        pre = self.hand.get_street('PREFLOP')
        return self.sf() and self.ai() != 'PREFLOP' and pre.how_many_aggr == 3

    def pot_5bet_plus(self):
        # czy to byl 5bp lub wiecej
        pre = self.hand.get_street('PREFLOP')
        return self.sf() and self.ai() != 'PREFLOP' and pre.how_many_aggr >= 4

    def ai(self):
        # nazwa strita albo None
        return self.hand.get_ai_street()

    def open_pos_nr(self):
        if self.opener == -1:
            self._betters()
        if self.opener is not None:
            return self.opener.hud_position_nr()
        return -1

    def three_bet_pos_nr(self):
        if self.three_better == -1:
            self._betters()
        if self.three_better is not None:
            return self.three_better.hud_position_nr()
        return -1

    def four_bet_pos_nr(self):
        if self.four_better == -1:
            self._betters()
        if self.four_better is not None:
            return self.four_better.hud_position_nr()
        return -1

    def nr_of_players(self):
        return self.hand.get_nr_of_players()


class Postflop(object):
    def __init__(self, hand):
        self.hand = hand
        self.results = {}
        self.streets = hand.streets

    @staticmethod
    def classes():
        return [Bet, Db, Cb, BVsMcb, Float, Aggression]

    def evaluate(self):
        plrs = [str(pl) for pl in self.hand.get_players()]
        for pl in plrs:
            tmp_dct1 = dict()
            for name, street in self.streets.items():
                if name == 'PREFLOP':
                    continue
                if pl not in [str(p) for p in street.get_players_start()]:
                    break

                if name == 'FLOP':
                    sufix = '_f'
                else:
                    sufix = '_t' if name == 'TURN' else '_r'

                cache_dct = dict()
                for cls in self.classes():
                    tmp_dct2 = dict()
                    methods = cls.hud_types().keys()
                    if cls != Aggression and cls != Bet:
                        instance = cls(self.hand, name, pl,
                                       cache=cache_dct)
                    else:
                        instance = cls(self.hand, name, pl)

                    for method in methods:
                        tmp = eval('instance.%s()' % method)
                        tmp = 'None' if tmp is None else tmp
                        tmp_dct2[method] = tmp

                    tmp_dct1[cls.__name__ + sufix] = tmp_dct2
                    if cls != Aggression:
                        cache_dct.update(instance.attrs)
            self.results[pl] = tmp_dct1
        return self.results



