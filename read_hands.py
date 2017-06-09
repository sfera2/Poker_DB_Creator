import time
from czytanieAkcji import Reka
from multiprocessing import Pool
from handHud import *


def read_hands(data, limit=-1):
    import re
    pat = re.compile(r'^PokerStars Hand #\d+:.*')
    with open(data) as plk:
        hands = plk.readlines()

    start = []
    hand_cnt, limit_flg = 0, False
    for i, line in enumerate(hands):
        if pat.match(line):
            start.append(i)
            hand_cnt += 1
            if hand_cnt == limit:
                limit_flg = True
                break

    hands_lst = []
    for i in range(len(start)):
        if i == len(start) - 1:
            if limit_flg:
                break
            hand = (hands[start[i]:len(hands)])
        else:
            hand = (hands[start[i]:start[i + 1]])
        hands_lst.append(hand)
    return hands_lst


def make_hud(hand):
    return HandHud(hand)


def make_hand(txt):
    return Reka(txt)

if __name__ == '__main__':
    t = time.time()
    hands_t = read_hands('ps.txt')
    with Pool(processes=4) as p:
        hands = p.map(make_hand, hands_t, chunksize=1)
        huds = p.map(make_hud, hands, chunksize=1)
    print(len(huds))
    print(time.time() - t)
