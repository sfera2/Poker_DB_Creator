from createDB import *


conn, cur = connection()


def float_pos(player, position, ip=True, _2b=True, _3b=False, _4b=False, _5b=False):
    query = "SELECT id FROM players WHERE name = '%s'" % player
    cur.execute(query)
    pl_id = cur.fetchone()[0]
    query = "SELECT id FROM positions WHERE name = '%s'" % position.upper()
    cur.execute(query)
    pos_id = cur.fetchone()[0]
    query = "SELECT hands.number, hud.b_opp_f  \
            FROM hands JOIN hud ON hands.id = hud.hands_id  \
            JOIN player_hand ON hands.id = player_hand.hands_id  \
            AND player_hand.players_id = hud.players_id  \
            JOIN hands_info ON hands.id = hands_info.hands_id  \
            WHERE (hud.players_id = %s  \
            AND hands_info.pot_2bet = true  \
            AND player_hand.sf = true  \
            AND player_hand.pos_nr = %s)" % (pl_id, pos_id)
    print(query)
    cur.execute(query)
    return cur.fetchall()


def read_hand(nr):
    statement = 'SELECT txt FROM hands WHERE number = %s' % nr
    cur.execute(statement)
    return cur.fetchone()[0]

for nr, result in float_pos('Rodik002', 'co'):
    # print(nr, result)
    print(read_hand(nr))
    print(result)
    input('dalej ?')
    print()
