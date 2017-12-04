import psycopg2
import sys
from handHud import *
import time
from psycopg2.extensions import AsIs
import copy
from multiprocessing import Pool
import os


def connection():
    try:
        conn = psycopg2.connect(database="new", user="postgres",
                                password="postgrespass", host='localhost',
                                port='5432')
        # print('super')
        curs = conn.cursor()
    except psycopg2.OperationalError:
        print(sys.exc_info())
        print('connection failed')
        sys.exit()
    return conn, curs


def drop_tables(cur, con):
    # for testing when needed to empty database
    cur.execute(''' DROP TABLE IF EXISTS public.hands_info CASCADE''')
    cur.execute(''' DROP TABLE IF EXISTS public.hands CASCADE''')
    cur.execute(''' DROP TABLE IF EXISTS public.players CASCADE''')
    cur.execute(''' DROP TABLE IF EXISTS public.positions CASCADE''')
    cur.execute(''' DROP TABLE IF EXISTS public.player_hand CASCADE''')
    cur.execute(''' DROP TABLE IF EXISTS public.hud CASCADE''')
    con.commit()


def create_schema(cur, con):
    def hands(c):
        c.execute('''
            CREATE TABLE public.hands (
                id SERIAL PRIMARY KEY UNIQUE,
                number BIGINT UNIQUE,
                txt TEXT
                    )''')

    def players(c):
        c.execute('''
            CREATE TABLE public.players (
                id SERIAL PRIMARY KEY UNIQUE,
                name VARCHAR(30) UNIQUE
                    )''')

    def positions(c):
        c.execute('''
            CREATE TABLE public.positions (
                id SMALLINT PRIMARY KEY UNIQUE,
                name CHAR(3)
                    )''')

        c.execute('''
            INSERT INTO public.positions (id, name) VALUES (1, 'BU');
            INSERT INTO public.positions (id, name) VALUES (2, 'BB');
            INSERT INTO public.positions (id, name) VALUES (3, 'SB');
            INSERT INTO public.positions (id, name) VALUES (4, 'CO');
            INSERT INTO public.positions (id, name) VALUES (5, 'MP');
            INSERT INTO public.positions (id, name) VALUES (6, 'UTG');
        ''')

    def player_hand(c):
        types = PlayerGeneral.hud_types()
        columns = ''
        for k, v in types.items():
            columns += k + ' ' + v + ', '
        c.execute('''
            CREATE TABLE public.player_hand (
                players_id INTEGER,
                hands_id INTEGER,
                %s
                PRIMARY KEY (players_id, hands_id),
                FOREIGN KEY (players_id) REFERENCES players (id),
                FOREIGN KEY (hands_id) REFERENCES hands (id),
                FOREIGN KEY (pos_nr) REFERENCES positions (id)
                    )''' % columns)

    def hands_info(c):
        types = HandGeneral.hud_types()
        columns = ''
        for k, v in types.items():
            columns += k + ' ' + v + ', '
        columns = columns[:-2]
        c.execute('''
            CREATE TABLE public.hands_info (
                hands_id INTEGER PRIMARY KEY UNIQUE REFERENCES hands (id),
                %s
                    )''' % columns)

    def hud(c):
        classes_post = [Bet, Db, Cb, BVsMcb, Float, Aggression]
        classes2 = [Preflop]
        post = ['_f', '_t', '_r']
        columns = ''
        for cls in classes2:
            types = cls.hud_types()
            for k, v in types.items():
                columns += k + ' ' + v + ', '
        for cls in classes_post:
            types = cls.hud_types()
            for k, v in types.items():
                for el in post:
                    columns += k + el + ' ' + v + ', '
        c.execute('''
            CREATE TABLE public.hud (
                players_id INTEGER,
                hands_id INTEGER,
                %s
                PRIMARY KEY (players_id, hands_id),
                FOREIGN KEY (players_id) REFERENCES players (id),
                FOREIGN KEY (hands_id) REFERENCES hands (id)
                    )''' % columns)

    hands(cur)
    players(cur)
    positions(cur)
    player_hand(cur)
    hands_info(cur)
    hud(cur)
    con.commit()


def fill_tables(cur, con, hand_huds):
    def hands(c, hand_hud):
        dct = hand_hud.hands
        try:
            columns = dct.keys()
            values = [dct[col] for col in columns]
            ins_stment = 'INSERT INTO hands (%s) VALUES %s' \
                         ' ON CONFLICT DO NOTHING'
            cur.execute(ins_stment, (AsIs(','.join(columns)), tuple(values)))
        except:
            print('KONIEC')
            sys.exit()

    def players(c, hand_hud):
        dct = hand_hud.players
        for k, v in dct.items():
            column, player = tuple(v.items())[0]
            cur.execute('''
                INSERT INTO players (name) VALUES (%s)
                ON CONFLICT DO NOTHING
            ''' % player)

    def hands_info(c, hand_hud):
        nr = hand_hud.get_number()
        c.execute('''
            SELECT id FROM public.hands WHERE number = %s
        ''' % nr)
        hand_id = c.fetchone()[0]

        dct = hand_hud.hands_info
        dct['hands_id'] = hand_id
        try:
            columns = dct.keys()
            values = [dct[col] for col in columns]
            ins_stment = 'INSERT INTO hands_info (%s) VALUES %s'
            cur.execute(ins_stment, (AsIs(','.join(columns)), tuple(values)))
        except:
            print('KONIEC')
            sys.exit()

    def player_hand(c, hand_hud):
        nr = hand_hud.get_number()
        c.execute('''
            SELECT id FROM public.hands WHERE number = %s
        ''' % nr)
        hand_id = c.fetchone()[0]

        dct = hand_hud.player_hand
        tmp = copy.copy(dct)

        for player in tmp:
            # plr = player.replace(', '')
            dct[player]['hands_id'] = hand_id
            c.execute('''
                SELECT id FROM public.players WHERE name = '%s'
            ''' % player)
            player_id = c.fetchone()[0]

            dct[player]['players_id'] = player_id
            try:
                columns = dct[player].keys()
                values = [dct[player][col] for col in columns]
                ins_stment = 'INSERT INTO player_hand (%s) VALUES %s'
                cur.execute(ins_stment, (AsIs(','.join(columns)),
                                         tuple(values)))
            except:
                print('KONIEC')
                sys.exit()

    def hud(c, hand_hud):
        nr = hand_hud.get_number()
        c.execute('''
            SELECT id FROM public.hands WHERE number = %s
        ''' % nr)
        hand_id = c.fetchone()[0]

        dct = hand_hud.hud
        tmp = copy.copy(dct)

        for player in tmp:
            dct[player]['hands_id'] = hand_id
            c.execute('''
                SELECT id FROM public.players WHERE name = '%s'
            ''' % player)
            player_id = c.fetchone()[0]

            dct[player]['players_id'] = player_id
            try:
                columns = dct[player].keys()
                values = [dct[player][col] for col in columns]
                ins_stment = 'INSERT INTO hud (%s) VALUES %s'
                cur.execute(ins_stment, (AsIs(','.join(columns)),
                                         tuple(values)))
            except:
                print('KONIEC')
                sys.exit()

    for hnd_hud in hand_huds:
        if hnd_hud is not None:
            hands(cur, hnd_hud)
            players(cur, hnd_hud)
            hands_info(cur, hnd_hud)
            player_hand(cur, hnd_hud)
            hud(cur, hnd_hud)
    con.commit()


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
    try:
        return HandHud(hand)
    except:
        pass


def make_hand(txt):
    return Reka(txt)


def folder_to_db(folder):
    return [fle for fle in os.listdir(folder) if fle.endswith('txt')]


if __name__ == '__main__':
    conn, curs = connection()
    # drop_tables(curs, conn)
    create_schema(curs, conn)

    folder_base = os.getcwd() + '/hands/'
    if not os.path.exists(os.getcwd() + '/hands_backup/'):
        os.makedirs(os.getcwd() + '/hands_backup/')
    folder_back = os.getcwd() + '/hands_backup/'

    i, cnt = 0, 0
    t = time.time()

    for file in folder_to_db(folder_base):
        dirc = folder_base + file
        try:
            hands_t = read_hands(dirc)
        except:
            continue
        i += 1
        print('File number: ', i)
        print('Making hands...')
        with Pool(processes=4) as p:
            hands = p.map(make_hand, hands_t, chunksize=1)
            huds = p.map(make_hud, hands, chunksize=1)
        os.rename(dirc, folder_back + file)
        cnt += len(huds)

        print('Filling...')
        fill_tables(curs, conn, huds)
        print('Filled. Average time: ', round(cnt / (time.time() - t), 2),
              'hands/s')
        print()
