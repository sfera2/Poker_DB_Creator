import rozne, definicje
from collections import Counter
import numpy


class Hand(object):
    # praktycznie nigdzie nie powinienem uzywac self.hand bo to jest do kitu. powinienem albo wszedzie uzywac self.karty
    # ,albo zmienic odpowiednio self.hand tak zeby sie skladalo z Kart
    def __init__(self, hand):
        from klasy import Karta
        if type(hand) is Hand:
            self.karty = hand.karty

        else:
            self.hand = hand
            self.karty = []
            for i, el in enumerate(self.hand):
                if i % 2 == 1:
                    self.karty.append(Karta(self.hand[i - 1] + self.hand[i]))

        if self.karty[0].liczba() > self.karty[1].liczba():
            pass
        else:
            self.karty = [self.karty[1], self.karty[0]]

    def __str__(self):
        string = ''
        for karta in self.karty:
            string += str(karta)
        return string
    
    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i == len(self.karty):
            raise StopIteration
        self.i += 1
        return self.karty[self.i - 1]
    
    def __eq__(self, other):
        i = 0
        for el in self.karty:
            if el in other.karty:
                i += 1
        return i == len(self.karty)
        
    def __lt__(self, other):
        return self.liczba() < other.liczba()
    
    def __getitem__(self, num):
        return self.karty[num]

    def rowna(self, other):
        try: # jak przejdzie to znaczy ze jest ustalony board, czyli postflop
            other.setBoard(self.board)
            if self.liczba() == other.liczba():
                return True
            else:
                return False
                
        except AttributeError: # nie przeszlo czyli preflop
            if self.suited() != other.suited():
                return False
            else:
                if self.liczby()[0] == other.liczby()[0] and self.liczby()[1] == other.liczby()[1]:
                    return True
                return False
            
    def equity(self, other, liczbaBoardow):
        from klasy import Talia
        from klasy import Board
        import random, copy
        
        talia = Talia()
        for karta in self.board:
            talia.usun(karta)
        for karta in self:
            talia.usun(karta)
        for karta in other:
            talia.usun(karta)
            
        a,b = 0,0
        for i in range(liczbaBoardow):
            # losowanie 4 boardow jest wystarczajace do liczenia equity mojej reki na jego range jezeli w range jest 130 rak. wiec
            # iloczyn wynosi 520. i tego sie mozna trzymac. jak np. w range bedzie 260 rak to wystarczy losowac 2 boardy
            if self.board.ulica() == 'flop':
                help = random.sample(list(talia), 2)
            elif self.board.ulica() == 'turn':
                help = random.sample(list(talia), 1)
            else:
                help = []

            board = str(self.board)
            for el in help:
                board += str(el)
            
            board = Board(board)
            help1, help2 = copy.deepcopy(self), copy.deepcopy(other)
            help1.setBoard(board)
            help2.setBoard(board)
            if help1 > help2:
                a += 1
            elif help2 > help1:
                pass
            else: # sa rowne
                a += 0.5
            b += 1
        
        return a / b
    
    def equityRange(self, zakres, board):
        zakres.setBoard(board)
        dlugosc = len(zakres)
        liczbaBoardow = round(550 / dlugosc)
        liczbaBoardow = 1 if liczbaBoardow == 0 else liczbaBoardow
        eq = 0
        for el in zakres.czysc():
            reka,waga = el
            eq += self.equity(reka, liczbaBoardow) * waga
            
        return eq / dlugosc
        
    def ile_outow(self):
        '''funkcja, ktora stara sie obliczyc ile mam czystych outow jak nie mam wystarczajaco mocnego made
        to czy reka jest wystarczajaco mocna rozstrzygane jest juz w programie. tutaj tylko zawarte sa outy
        jezeli uznam ze ich potrzebuje. jezeli jakiejs reki nie ma w slowniku tzn. ze ma 0 outow
        
        DOROBIC 3B POTY:
        w normalnym pocie jak mam JT na 873 to moge liczyc, ze J lub T sa moimi outami, a w 3b pocie jak
        zakresy sa waskie nie moge na to liczyc
        '''

        self.outy = 0
        if self.board.ulica() == 'river':
            return
        nazwaBoardu = self.board.getNazwa()
        
        # strita na boardzie nie ma co rozwazac bo to musialby byc river
        if 'niesparowany' in nazwaBoardu:
            if 'rainbow' in nazwaBoardu:
                if 'GS' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'OESD' in self.nazwa:
                        self.outy = 8
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 8
                    elif 'GS' in self.nazwa:
                        self.outy = 4
                    else:
                        pass
                    
                elif 'four2str8' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'GS' in self.nazwa:
                        self.outy = 4
                    else:
                        pass
                # to znaczy ze sa mozliwe boardy na ktorych jest mozliwe 0-3 stritow, pod wzgledem
                # outow nie ma znaczenia czy sa mozliwe jakies strity czy nie, bo na boardzie na ktorym
                # nie ma stritow nie moge miec idiotEndow, bo zawsze beda uzywane 2 karty
                else:
                    if 'OESD' in self.nazwa:
                        if '2OC' in self.nazwa:
                            self.outy = 11
                        elif '1P' in self.nazwa:
                            self.outy = 10 # licze tylko do tripsa, a nie do 2P
                        else:
                            self.outy = 8
                            
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 8
                    
                    elif 'GS' in self.nazwa:
                        if '2OC' in self.nazwa:
                            self.outy = 7
                        else:
                            self.outy = 4
                            
                    elif '2OC' in self.nazwa:
                        self.outy = 5 # 1 mniej bo nie zawsze to beda moje outy
                        
                    elif '1P' in self.nazwa:
                        self.outy = 5
                    
            elif '2xFD' in nazwaBoardu:
                if 'GS' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'OESD' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 4
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 2
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                
                elif 'four2str8' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 2
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                # to znaczy ze sa mozliwe 0,1,2,3 strity
                else:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'OESD' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 4
                    elif 'doubleBelly' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 4
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 2
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        
                    if '2OC' in self.nazwa:
                        self.outy += 2
                    if '1P' in self.nazwa:
                        self.outy += 3
            
            elif 'FD' in nazwaBoardu:
                if 'GS' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'OESD' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 6
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 3
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        
                elif 'four2str8' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 3
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                # to znaczy ze sa mozliwe 0,1,2,3 strity
                else:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'OESD' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 6
                    elif 'doubleBelly' in self.nazwa:    
                        if 'FD' in self.nazwa:
                            self.outy = 15
                        else:
                            self.outy = 6
                    elif 'GS' in self.nazwa:
                        if 'FD' in self.nazwa:
                            self.outy = 12
                        else:
                            self.outy = 3
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        
                    if '2OC' in self.nazwa:
                        self.outy += 2
                    if '1P' in self.nazwa:
                        self.outy += 3
                        
            # three2flush na T, albo mono F + T
            else:
                if 'GS' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        if 'OESD' in self.nazwa: # tak symbolicznie dolicze
                            self.outy += 2
                        elif 'GS' in self.nazwa:
                            self.outy += 1
                    
                elif 'four2str8' in nazwaBoardu:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        if 'GS' in self.nazwa:
                            self.outy += 1
                # to znaczy ze sa mozliwe 0,1,2,3 strity
                else:
                    if 'set' in self.nazwa:
                        self.outy = 10
                    elif '2P' in self.nazwa:
                        self.outy = 4
                    elif 'FD' in self.nazwa:
                        self.outy = 9
                        if 'OESD' in self.nazwa: # tak symbolicznie dolicze
                            self.outy += 2
                        elif 'doubleBelly' in self.nazwa:
                            self.outy += 2
                        elif 'GS' in self.nazwa:
                            self.outy += 1
                    elif 'OESD' in self.nazwa and '2OC' in self.nazwa:
                        if self.board.ulica() == 'turn':
                            if 'mono' in nazwaBoardu:
                                pass
                            else:
                                self.outy = 4 # tak symbolicznie
                        # czyli flop
                        else:
                            self.outy = 4
                            
                    elif 'doubleBelly' in self.nazwa:
                        if self.board.ulica() == 'turn':
                            if 'mono' in nazwaBoardu:
                                pass
                            else:
                                self.outy = 4 # tak symbolicznie
                        # czyli flop
                        else:
                            self.outy = 4
                        
                    if '1P' in self.nazwa:
                        self.outy += 1 # tez symbolicznie
                    
        # sparowany
        else:
            # sparowany stol nigdy nie bedzie mono, a four2flush tylko na R
            if 'rainbow' in nazwaBoardu:
                # najbardziej connected board moze wygladac 8876, GS i 42str8 nie mozliwe, wiec nie rozrozniam boardow
                if 'OESD' in self.nazwa:
                    self.outy = 7
                elif 'doubleBelly' in self.nazwa:
                    self.outy = 7
                elif 'GS' in self.nazwa:
                    self.outy = 3
                elif '2P' in self.nazwa:
                    self.outy = 2
                    
                if '2OC' in self.nazwa:
                    self.outy += 3
                    
            elif '2xFD' in nazwaBoardu:
                # najbardziej connected board moze wygladac 8876, GS i 42str8 nie mozliwe, wiec nie rozrozniam boardow
                if 'FD' in self.nazwa:
                    if 'OESD' in self.nazwa:
                        self.outy = 11
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 11
                    elif 'GS' in self.nazwa:
                        self.outy = 8
                    else:    
                        self.outy = 7
                else:
                    if 'OESD' in self.nazwa:
                        self.outy = 3
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 3
                    elif 'GS' in self.nazwa:
                        self.outy = 1
                    elif '2P' in self.nazwa:
                        self.outy = 1
                    
                if '2OC' in self.nazwa:
                    self.outy += 1
                    
            elif 'FD' in nazwaBoardu:
                # najbardziej connected board moze wygladac 8876, GS i 42str8 nie mozliwe, wiec nie rozrozniam boardow
                if 'FD' in self.nazwa:
                    if 'OESD' in self.nazwa:
                        self.outy = 13
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 13
                    elif 'GS' in self.nazwa:
                        self.outy = 10
                    else:    
                        self.outy = 7
                else:
                    if 'OESD' in self.nazwa:
                        self.outy = 5
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 5
                    elif 'GS' in self.nazwa:
                        self.outy = 2
                    elif '2P' in self.nazwa:
                        self.outy = 2
                    
                if '2OC' in self.nazwa:
                    self.outy += 1
                    
            elif 'three2flush' in nazwaBoardu:
                # najbardziej connected board moze wygladac 8876, GS i 42str8 nie mozliwe, wiec nie rozrozniam boardow
                if 'FD' in self.nazwa:
                    # symbolicznie zwiekszam
                    if 'OESD' in self.nazwa:
                        self.outy = 9
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 9
                    elif 'GS' in self.nazwa:
                        self.outy = 8
                    else:    
                        self.outy = 7
                else:
                    if 'OESD' in self.nazwa:
                        self.outy = 2
                    elif 'doubleBelly' in self.nazwa:
                        self.outy = 2
                    
                if '2OC' in self.nazwa:
                    self.outy += 1
                    
                if '2P' in self.nazwa:
                    self.outy = 2
                    
        return self.outy
        
    def setBoard(self, board):
        from klasy import Karta
        self.board = board
        lst = [card for card in self.karty] + [card for card in self.board]
        lst.sort(key=lambda x: x.liczba(), reverse=True)
        # self.lst1 used for flushes and FDs
        self.lst1 = list(lst)
        for crd in lst:
            if crd.liczba() == 13:
                card = Karta('0' + crd.suit())
                lst.append(card)
        self.lst = lst
        # w ten sposob wiem, ze za kazdym razem gdy tylko board jest wprowadzony do reki od razu ustalane
        # sa wszystkie jej parametry
        self.uklad()
        self.blefingValue()
        
    def getKicker(self):
        # jak jest board
        try:
            return self.kicker
        except:
            return None

    def getKickerFD(self):
        # jak jest board
        try:
            return self.kickerFD
        except:
            return None

    def reka(self):
        return self.hand
        
    def liczby(self):
        liczbyx = []
        for karta in self:
            liczbyx.append(karta.liczba())
        liczbyx.sort()
        return liczbyx
        
    def suits(self):
        suitsx = []
        for karta in self:
            suitsx.append(karta.suit())
        return suitsx
        
    def suited(self):
        if self.hand[1] == self.hand[3]:
            return True
        else:
            return False
            
    def pocket(self):
        if self.hand[0] == self.hand[2]:
            return True
        else:
            return False
            
    def co(self):
        return self.nazwa

    def liczba(self):
        return self.value
        
    def Made(self):
        return self.made
        
    def SDv(self):
        return self.sdv
    
    def Bv(self):
        return self.bv
        
    def poker(self):
        suits = [card.suit() for card in self.lst1]
        suits = Counter(suits)
        checker = True
        for key in suits:
            if suits[key] >= 5:
                color = key
                checker = False
                break
        if checker:
            return False

        cards = [card for card in self.lst if card.suit() == color]
        num = 1
        for i, card in enumerate(cards):
            if i == 0:
                continue
            else:
                pr_card = cards[i - 1]
                if pr_card.liczba() - card.liczba() == 1:
                    num += 1
                    if num == 5:
                        kicker = cards[i - 4].liczba()
                        return True, 13 ** 4 * kicker
                    pass
                else:
                    num = 1

            if num + (len(cards) - i) <= 5:
                return False

    def kareta(self):
        lst = [card.liczba() for card in self.lst]
        lst = Counter(lst)
        for key, value in lst.items():
            if value == 4:
                kicker = max([c for c in lst if c != key])
                return True, 13**4 * key + 13**3 * kicker, key, kicker
        return False

    def full(self):
        lst = [card.liczba() for card in self.lst]
        lst = Counter(lst)
        trips, pairs = [], []
        twos, threes = 0, 0
        for key, value in lst.items():
            if value == 3:
                threes += 1
                trips.append(key)
            elif value == 2:
                twos += 1
                pairs.append(key)
        if threes == 2:
            return True, 13**4 * max(trips) + 13**3 * min(trips), max(trips), min(trips)
        elif threes == 0:
            return False
        elif twos != 0:
            return True, 13**4 * trips[0] + 13**3 * max(pairs), trips[0], max(pairs)
        else:
            return False

    def kolor(self):
        kolory = Counter([card.suit() for card in self.lst1])
        checker = False
        for key, value in kolory.items():
            if value >= 5:
                jakiKolor = key
                checker = True
                break

        if checker:
            cards = [card for card in self.lst1 if card.suit() == jakiKolor][:5]
            cards_hand = [card for card in self.karty if card in cards]
            if len(cards_hand) > 0:
                # most important kicker is the one from hand not the board
                kicker = cards_hand[0].liczba()
                cards.remove(cards_hand[0])
                kicker1, kicker2 = cards[0].liczba(), cards[1].liczba()
                kicker3, kicker4 = cards[2].liczba(), cards[3].liczba()
            else:
                kicker, kicker1, kicker2 = cards[0].liczba(), cards[0].liczba(), cards[2].liczba()
                kicker3, kicker4 = cards[3].liczba(), cards[4].liczba()

            return True, (13**4 * kicker) + (13**3 * kicker1) + (13**2 * kicker2) + (13 * kicker3) + kicker4,\
                   kicker, kicker1, kicker2, kicker3, kicker4
        else:
            return False

    def str8(self):
        num = 1
        lst = sorted(list(numpy.unique([c.liczba() for c in self.lst])),
                     reverse=True)
        # print ('629', [str(c) for c in lst])
        for i, card in enumerate(lst):
            if i == 0:
                continue
            else:
                pr_card = lst[i - 1]
                if pr_card - card == 1:
                    num += 1
                    if num == 5:
                        kicker = lst[i - 4]
                        cards_str8 = lst[i - 4: i + 1]
                        cards_hands = []
                        for cardh in self.karty:
                            if cardh.liczba() in cards_str8 and\
                                    cardh.liczba() not in self.board.liczby():
                                cards_hands.append(cardh)
                        end = 'smartEnd'
                        if len(cards_hands) == 1 and\
                                    cards_hands[0].liczba() == cards_str8[-1]:
                            # I have one card to make the bottom of the str8:
                            # it's easy to have better str8
                            end = 'idiotEnd'

                        return True, 13**4 * kicker, kicker,\
                               len(cards_hands), end
                else:
                    num = 1

            if num + (len(lst) - i) < 5:
                return False

    def trips(self, listaV):
        figury = Counter(listaV)
        x = 0
        
        for key in figury.keys():
            if figury[key] == 3:
                x += 1
                trips = key
                for el in listaV:
                    if el == trips:
                        ktory = listaV.index(el) + 1
                
                listaV = list(numpy.unique(listaV))
                listaV.remove(trips)
                kicker1 = max(listaV)
                listaV.remove(kicker1)
                kicker2 = max(listaV)
        
        if x == 1:
            return True, 13**4 * trips + 13**3 * kicker1 + 13**2 * kicker2, ktory, trips, kicker1, kicker2
        else:
            return False

    def dwiePary(self):
        if 'sparowany' in self.board.getNazwa():
            if self.pocket():
                if self.liczby()[0] < max(self.board.liczby()):
                    # board sparowany, pocket nizszy niz TP, uznaje ze to 1 para
                    return False
                else:
                    # board sparowany, pocket wyzszy niz TP, uznaje ze to 2 pary
                    para1, para2 = self.liczby()[0], self.board.sparowanaKarta()
                    for el in self.board.liczby():
                        if el != self.board.sparowanaKarta():
                            kicker = el
                            break
                    pierwsza_para = 1
                    druga_para = 2
                    for el in self.board.liczby():
                        if el > self.board.sparowanaKarta():
                            druga_para += 1
                        else:
                            break
                    
                    return True, (13 ** 4 * para1) + (13 ** 3 * para2)  + 13 ** 2 * kicker, pierwsza_para, druga_para, para1, para2, kicker
                    
            else:
                trafioneKarty = []
                for el in self.liczby():
                    if el in self.board.liczby():
                        trafioneKarty.append(el)
                if len(trafioneKarty) < 2:
                    # board sparowany, niepocket trafiajacy tylko 1 karte, uznaje ze to 1 para (np. KT na K322)
                    return False
                else:
                    if self.board.sparowanaKarta() < min(trafioneKarty) and max(trafioneKarty) == max(self.board.liczby()):
                        # board sparowany, niepocket trafiajacy 2 karty, z czego 1 jest TP a druga jest wyzsza niz para na stole. uznaje ze to 2P
                        para1, para2 = max(trafioneKarty), min(trafioneKarty)
                        pierwsza_para = 1
                        druga_para = 2
                        for el in self.board.liczby():
                            if el > self.board.sparowanaKarta():
                                druga_para += 1
                            else:
                                break
                                
                        for el in self.board.liczby():
                            if el != para1 and el != para2:
                                kicker = el
                                
                        return True, (13 ** 4 * para1) + (13 ** 3 * para2)  + 13 ** 2 * kicker, pierwsza_para, druga_para, para1, para2, kicker
                    else:
                        return False
        else:
            if self.pocket():
                return False
            else:
                trafioneKarty = []
                for el in self.liczby():
                    if el in self.board.liczby():
                        trafioneKarty.append(el)
                        
                if len(trafioneKarty) < 2:
                    return False
                else:
                    para1, para2 = max(trafioneKarty), min(trafioneKarty)
                    pierwsza_para = 1
                    druga_para = 2
                    for el in self.board.liczby():
                        if el > para1:
                            pierwsza_para += 1
                            druga_para += 1
                        elif el > para2:
                            druga_para += 1
                        else:
                            break
                            
                    for el in self.board.liczby():
                        if el != para1 and el != para2:
                            kicker = el
                            
                    return True, (13 ** 4 * para1) + (13 ** 3 * para2)  + 13 ** 2 * kicker, pierwsza_para, druga_para, para1, para2, kicker
        
    def jednaPara(self):
        if 'sparowany' in self.board.getNazwa():
            if self.pocket():
                # bo wszystkie inne przypadki przerobione w 2P
                para = self.liczby()[0]
                for el in self.board.liczby():
                    if el != para and el != self.board.sparowanaKarta():
                        kicker = el
                        break
                        
                ktora_para = 1
                for el in self.board.liczby():
                    if el > para:
                        ktora_para += 1
                    else:
                        break
                
                kicker1 = self.board.sparowanaKarta()
                # mpocket ponizej TP
                if para > kicker:
                    bonus = 10 ** 5
                    self.bonus = True
                else:
                    bonus = 0
                    self.bonus = False
                    
                return True, bonus + (13 ** 4 * para) + (13 ** 3 * kicker) + (13 ** 2 * kicker1) + 13 * kicker1, ktora_para, para, kicker, kicker1, kicker1
                
            else:
                self.bonus = False
                trafioneKarty = []
                for el in self.liczby():
                    if el in self.board.liczby():
                        trafioneKarty.append(el)
                if len(trafioneKarty) >= 1:
                    # nie uwzgledniam ze board moze byc podwojnie sparowany
                    para = max(trafioneKarty)
                    
                    ktora_para = 1
                    for el in self.board.liczby():
                        if el > para:
                            ktora_para += 1
                        else:
                            break
                            
                    for el in sorted(self.board.liczby() + self.liczby(), reverse = True):
                        if el != para and el != self.board.sparowanaKarta():
                            kicker = el
                            break
                    kicker1 = self.board.sparowanaKarta()
                    
                    return True,(13 ** 4 * para) + (13 ** 3 * kicker) + (13 ** 2 * kicker1) + 13 * kicker1, ktora_para, para, kicker, kicker1, kicker1
                    
                else:
                    return False    
        else:
            self.bonus = False
            if self.pocket():
                para = self.liczby()[0]
                kickery = {}
                for i in range(3):
                    kickery[str(i)] = self.board.liczby()[i]
                    
                ktora_para = 1
                for el in self.board.liczby():
                    if el > para:
                        ktora_para += 1
                    else:
                        break
                        
                return True,(13 ** 4 * para) + (13 ** 3 * kickery['0']) + (13 ** 2 * kickery['1']) + 13 * kickery['2'], ktora_para, para, kickery['0'], kickery['1'], kickery['2']
            else:
                trafioneKarty = []
                for el in self.liczby():
                    if el in self.board.liczby():
                        trafioneKarty.append(el)
                        
                if len(trafioneKarty) == 1:
                    # bo wszystkie inne przypadki sa przerobione w 2P
                    para = trafioneKarty[0]
                    lista = sorted(self.board.liczby() + self.liczby(), reverse = True)
                    lista.remove(para)
                    lista.remove(para) # bo beda dwie takie karty
                    kickery = {}
                    for i in range(3):
                        kickery[str(i)] = lista[i]
                        
                    ktora_para = 1
                    for el in self.board.liczby():
                        if el > para:
                            ktora_para += 1
                        else:
                            break
                            
                    return True,(13 ** 4 * para) + (13 ** 3 * kickery['0']) + (13 ** 2 * kickery['1']) + 13 * kickery['2'], ktora_para, para, kickery['0'], kickery['1'], kickery['2']
                else:
                    return False
                    
    def twoOC(self, boardV, handV, listaV):
        if min(handV) > max(boardV):
            return self.XHigh(listaV)
            
        else:
            return False
            
    def XHigh(self, listaV):
        karta1, karta2, karta3, karta4, karta5 = listaV[0], listaV[1], listaV[2], listaV[3], listaV[4]
        return True, ((13 ** 4 * karta1) + (13 ** 3 * karta2) + (13 ** 2 * karta3) + (13 * karta4) + karta5) / 2, karta1, karta2, karta3, karta4, karta5

    def FD(self, listaS, boardV, handS):
        # na river juz nie mam FD
        if self.board.ulica() == 'river':
            return False
            
        else:
            help = Counter(listaS)
            checker = False
            for key in help:
                if help[key] == 4:
                    jakiKolor = key
                    checker = True
                    break
                    
            if checker:
                if jakiKolor not in handS:
                    return False
                    
                else:
                    help = -1
                    for karta in self.karty:
                        if karta.suit() == jakiKolor:
                            if karta.liczba() > help:
                                help = karta.liczba()

                    return True, help # help - najwyzsza karta z REKI z kolorem
                    
            else:
                return False
        
    def bFd(self, listaS, boardV, handS):
        # bFd moge miec tylko na flopie
        if self.board.ulica() != 'flop':
            return False
            
        else:
            help = Counter(listaS)
            checker = False
            
            for key in help:
                if help[key] == 3:
                    jakiKolor = key
                    checker = True
                    break
                    
            if checker:
                if jakiKolor in handS:
                    
                    reka = []
                    for el in self:
                        reka.append(el.liczba())
                        reka.append(el.suit())
                        
                    help = -1
                    for i in range(len(reka)):
                        if reka[i] == jakiKolor:
                            if reka[i - 1] > help:
                                help = reka[i - 1]
                            
                    return True, help
                    
                else:
                    return False
            
            else:
                return False

    def OESD(self, listaV, boardV, handV):
        # nie moge miec drawa na river
        if self.board.ulica() == 'river':
            return False
        
        # potrzebuje min. 4 kart do OESD
        elif len(list(numpy.unique(listaV))) < 4:
            return False
            
        else:
            listaV = list(numpy.unique(listaV))
            if max(listaV) == 13:
                listaV.append(0)
                
            for i in range(len(listaV)):
                # print (i, listaV[i], listaV[i + 3], len(listaV))
                if listaV[i] - listaV[i + 3] == 3:
                    if listaV[i] != 13 and listaV[i + 3] != 0:
                        # okreslam ilu kartowy oesd
                        oesd = list(range(listaV[i], listaV[i] - 4, -1))
                        kartyZReki = 0
                        for el in oesd:
                            if el in boardV:
                                continue
                            else:
                                kartyZReki += 1
                        
                        end = 'smartEnd'
                        # okreslam czy mam 'idiotEnd' czy 'smartEnd'
                        if kartyZReki == 0:
                            for el in handV:
                                if el - max(oesd) == 2:
                                    end = 'idiotEnd' # dlatego ze to bedzie w funkcjach uznane po prostu jako GS
                                    break
                                    
                            if end == 'smartEnd': # czyli nie mam GS
                                end = 'MEGAidiotEnd'
                                
                        elif kartyZReki == 1:
                            # okreslam, ktora moja karta z reki ma strita
                            for el in handV:
                                if el in oesd:    
                                    karta = el
                                    break
                            
                            if karta == min(oesd) and 'GS' in self.board.getNazwa():
                                end = 'MEGAidiotEnd' # np. A4 na 9765
                            elif karta == min(oesd):
                                end = 'idiotEnd'
                                
                        # mam 2 kartowy ale np. 34 na 9865 powinno miec 0 outow
                        else:
                            if min(boardV) > max(handV) and 'GS' in self.board.getNazwa():
                                end = 'MEGAidiotEnd'
                                
                        return True, listaV[i], kartyZReki, end
                        
                    else:
                        if i + 3 == len(listaV) - 1:
                            break
                
                else:
                    if i + 3 == len(listaV) - 1:
                        break
                        
            return False

    def doubleBelly(self, listaV, boardV):
        # nie moge miec drawa na river
        if self.board.ulica() == 'river':
            return False
        
        # potrzebuje min. 5 kart do doubleBelly
        elif len(list(numpy.unique(listaV))) < 5:
            return False
            
        else:
            listaV = list(numpy.unique(listaV))
            if max(listaV) == 13:
                listaV.append(0)
                
            for i in range(len(listaV)):
                if listaV[i] - listaV[i + 1] == 2 and listaV[i + 1] - listaV[i + 3] == 2 and listaV[i + 3] - listaV[i + 4] == 2:
                    if 'GS' in self.board.getNazwa():
                        end = 'idiotEnd'
                    else:
                        end = 'smartEnd'
                        
                    return True, listaV[i], end
                
                else: # to znaczy ze dobieglem do konca listy
                    if i + 4 == len(listaV) - 1:
                        break
            
            return False

    def GS(self, listaV, boardV, handV):
        # nie moge miec drawa na river
        if self.board.ulica() == 'river':
            return False
        
        # potrzebuje min. 4 kart do GS
        elif len(list(numpy.unique(listaV))) < 4:
            return False
            
        else:
            listaV = list(numpy.unique(listaV))
            if max(listaV) == 13:
                listaV.append(0)
                
            for i in range(len(listaV)):
                # to jest definicja OESD, ale GS moze byc tylko uzyty jesli OESD zwrocil False, wiec to bedzie lapalo sytuacje OESD gdy najwyzszy jest A lub wheel
                if listaV[i] - listaV[i + 3] == 3:
                    # tutaj nie ma idiotEnd, bo to jes GS gdzie najwyzsza karta jest A, wiec to nie ma
                    # znaczenia
                    end = 'smartEnd'
                    return True, listaV[i], end
                
                elif listaV[i] - listaV[i + 3] == 4:
                    # okreslam czy mam GS od dolu np. mam 54 na 987, bo taki GS jest nic niewarty
                    gs = []
                    for a in range(4):
                        gs.append(listaV[i + a])
                    
                    kartyZReki = 0
                    end = 'smartEnd'
                    for el in handV:
                        if el not in gs:
                            continue
                        else:
                            kartyZReki += 1
                            if el == min(gs) and kartyZReki == 1:
                                if 13 in gs:
                                    end = 'smartEnd'
                                else:
                                    end = 'idiotEnd'
                                
                    return True, listaV[i], end
                    
                else:
                    if i + 3 == len(listaV) - 1:
                        break
                    
            return False
            
    def boesd(self, boardV, handV):
        # moge miec tylko jak nie mam OESD ani GS
        # nie moge miec drawa na R
        if self.board.ulica() == 'river':
            return False
            
        # uznaje ze mam boesd kiedy moje 2 karty z reki z 3. z boardu tworza ciag 3 kolejnych kart (bo wtedy mam 8 outow do OESD)
        for el in boardV:
            help = list(handV)
            help.append(el)
            help.sort(reverse = True)
            if help[0] - help[1] == 1 and help[1] - help[2] == 1: # w ten sposob mam gwarancje, ze sa 3 kolejne, a np. 997
                return True
                
        return False

    def coMamMade(self):
        # okresla jakie mam madehandy
        handV = self.liczby()
        handS = self.suits()
        boardV = self.board.liczby()
        boardS = self.board.suits()
        
        string = self.hand + str(self.board)
        listaV = handV + boardV
        listaV.sort(reverse = True)
        listaS = handS + boardS
        
        nazwaStolu = self.board.getNazwa()
        help = self.poker()
        if help:
            self.value = 90 * (10 ** 6) + help[1]
            self.reszta = help[2:]
            self.nazwa = 'poker'
            self.made = True
            self.sdv = 'mocne'


        else:
            help = self.kareta()
            if help:
                self.value = 80 * (10 ** 6) + help[1]
                self.reszta = help[2:]
                self.nazwa = 'kareta'
                self.made = True
                self.sdv = 'mocne'

            else:
                help = self.full()
                if help:
                    self.value = 70 * (10 ** 6) + help[1]
                    self.reszta = help[2:]
                    self.nazwa = 'full'
                    
                    self.made = True
                    if 'trips' not in nazwaStolu:
                        self.sdv = 'mocne'
                    else:
                        self.sdv = 'srednie' # za duzo zmieniania teraz, zeby to uzaleznic od kart. przykladowo JJ na KKK22 jest dobre, ale na KKKAQ juz nie.
                    
                else:
                    help = self.kolor()
                    if help:
                        self.value = 60 * (10 ** 6) + help[1]
                        self.reszta = help[2:]
                        if self.reszta[0] == 13:
                            self.nazwa = 'nFlush'
                            self.kicker = 13
                        else:
                            self.nazwa = 'Flush(%s)' % self.reszta[0]
                            self.kicker = self.reszta[0]
                        
                        # okreslam sdv
                        self.made = True
                        if 'trips' in nazwaStolu or '2 pary' in nazwaStolu:
                            self.sdv = 'slabe'
                        elif ('four2flush' in nazwaStolu or 'five2flush' in nazwaStolu) and self.kicker < 7:
                            self.sdv = 'slabe'
                        elif ('four2flush' in nazwaStolu or 'five2flush' in nazwaStolu) and self.kicker < 11:
                            self.sdv = 'srednie'
                        else:
                            self.sdv = 'mocne'

                    else:
                        help = self.str8()
                        if help:
                            self.value = 50 * (10 ** 6) + help[1]
                            self.reszta = help[2:]
                            self.nazwa = 'str8(%(y)s) %(x)skartowy %(z)s' %\
                                         {'x': self.reszta[1],
                                          'y': self.reszta[0],
                                          'z': self.reszta[2]}
                            # x ile kartowy, y najwyzsza karta, z czy idiotEnd
                            
                            self.made = True
                            # okreslam sdv
                            pomoc = ['trips', '2 pary', 'four2flush', 'five2flush']
                            checker = True
                            for el in pomoc:
                                if el in nazwaStolu:
                                    self.sdv = 'slabe'
                                    checker = False
                                    break
                            if checker:
                                if 'three2flush' in nazwaStolu and 'sparowany' in nazwaStolu:
                                    self.sdv = 'slabe'
                                elif 'three2flush' in nazwaStolu:
                                    self.sdv = 'srednie'
                                else:
                                    self.sdv = 'mocne'
                            
                        else:
                            help = self.trips(listaV)
                            if help:
                                self.value = 42 * (10 ** 6) + help[1]
                                self.reszta = help[2:]
                                if self.pocket():
                                    self.nazwa = 'set(%s)' % self.reszta[0]
                                else:
                                    self.nazwa = 'trips'
                                    self.kicker = self.reszta[2]
                            
                                self.made = True
                                # okreslam sdv
                                if 'str8' in nazwaStolu and 'four2str8' not in nazwaStolu:
                                    self.sdv = 'brak'
                                else:
                                    pomoc = ['trips', '2 pary', 'four2flush', 'five2flush', 'GS', 'four2str8']
                                    checker = True
                                    for el in pomoc:
                                        if el in nazwaStolu:
                                            self.sdv = 'slabe'
                                            checker = False
                                            break
                                    if checker:
                                        self.sdv = 'mocne'
                                
                            else:
                                help = self.dwiePary()
                                if help:
                                    self.value = 30 * (10 ** 6) + help[1]
                                    self.reszta = help[2:]
                                    self.nazwa = '2P(%(x)s i %(y)s)' % {'x': self.reszta[0], 'y': self.reszta[1]} # ktore pary
                                    self.kicker = self.reszta[4]
                            
                                    self.made = True
                                    # okreslam sdv
                                    if 'str8' in nazwaStolu and 'four2str8' not in nazwaStolu:
                                        self.sdv = 'brak'
                                    else:
                                        pomoc = ['trips', '2 pary', 'three2flush', 'four2flush', 'five2flush', 'GS', 'four2str8']
                                        checker = True
                                        for el in pomoc:
                                            if el in nazwaStolu:
                                                self.sdv = 'slabe'
                                                checker = False
                                                break
                                        if checker:
                                            self.sdv = 'mocne'
                                            
                                else:
                                    help = self.jednaPara()
                                    if help:
                                        wartosc = help[1]
                                        # self.bonus jest przydzielany tylko w funkcji jednaPara dla szczegolnych mpocketow. Latanie kodu
                                        bonus = - 10 ** 5 if self.bonus else 0
                                        wartosc += bonus
                                        
                                        boardV.sort(reverse = True)
                                        lista = [13,12,11,10,9,8,7,6,5,4,3,2,1]
                                        lista.remove(boardV[0])
                                        # sprawdzam czy OvP
                                        mini = 13 ** 4 * (boardV[0] + 1) + 13 ** 3 * boardV[0] + 13 ** 2 * lista[-1] + 13 ** 1 * lista[-2] # troche mniej niz min, ktore musi miec OvP
                                        tpgk = 13 ** 4 * boardV[0] + 13 ** 3 * lista[2] # minimum jakie ma TPGK
                                        tptk = 13 ** 4 * boardV[0] + 13 ** 3 * lista[0] # minimum jakie ma TPTK
                                        tp = 13 ** 4 * boardV[0] + 13 ** 3 * 4 # okolice minimum jakie musi miec TP
                                        self.reszta = help[2:]

                                        if wartosc > mini:
                                            # mam OvP i chce to miec wyroznione - zawsze jest wieksza niz 1P,
                                            self.value = 12 * (10 ** 6) + wartosc
                                            self.nazwa = '1P OvP(%s)' % self.reszta[1]
                            
                                        elif wartosc >= tpgk:
                                            # tu wiem, ze mam TPGK
                                            self.value = 11 * (10 ** 6) + wartosc
                                            if wartosc >= tptk:
                                                self.nazwa = '1P TPTK'
                                            else:
                                                self.nazwa = '1P TPGK'
                                                
                                            self.kicker = self.reszta[2]
                                            
                                        elif wartosc >= tp:
                                            # tu wiem, ze mam TP
                                            self.value = 8.3 * (10 ** 6) + wartosc
                                            self.nazwa = '1P TPWK'
                                            self.kicker = self.reszta[2]
                                            
                                        else:
                                            self.value = 8 * (10 ** 6) + wartosc
                                            if self.pocket():
                                                self.nazwa = '1P MPocket(%s)' % self.reszta[0] # ktora para
                                            else:
                                                self.nazwa = '1P(%s)' % self.reszta[0] # ktora para
                                                self.kicker = self.reszta[2]
                                                
                                        self.made = True
                                        # okreslam sdv
                                        if 'str8' in nazwaStolu and 'four2str8' not in nazwaStolu:
                                            self.sdv = 'brak'
                                        else:
                                            pomoc = ['trips', '2 pary', 'three2flush', 'four2flush', 'five2flush', 'GS', 'four2str8']
                                            checker = True
                                            for el in pomoc:
                                                if el in nazwaStolu:
                                                    if el == 'three2flush' and ('TP' in self.nazwa or 'OvP' in self.nazwa):
                                                        self.sdv = 'srednie'
                                                    else:
                                                        self.sdv = 'slabe'
                                                    checker = False
                                                    break
                                                    
                                            if checker:
                                                if 'TP' in self.nazwa or 'OvP' in self.nazwa:
                                                    self.sdv = 'mocne'
                                                else:
                                                    self.sdv = 'srednie' # bo to jedna para nie TP
                                                
                                                
                                    else:
                                        help = self.twoOC(boardV, handV, listaV)
                                        if help:
                                            self.value = help[1]
                                            self.reszta = help[2:]
                                            self.nazwa = '2OC'

                                        else:
                                            help = self.XHigh(listaV)
                                            self.value = help[1]
                                            self.nazwa = '%shigh' % rozne.lickar(str(max(self.liczby())))
                                            self.reszta = help[2:]
                                            
                                        self.made = False
                                        self.sdv = 'brak'

    def uklad(self):
        # okresla co mam i jakie drawy
        handV = self.liczby()
        handS = self.suits()
        boardV = self.board.liczby()
        boardS = self.board.suits()
        
        string = self.hand + str(self.board)
        listaV = handV + boardV
        listaV.sort(reverse = True)
        listaS = handS + boardS
        
        self.coMamMade()
        liczbaDoPomocyNaKoncu = int(self.value)
        # jak mam str8 lub lepiej, to moge uznac ze nie mam drawow
        if self.value >= 30 * (10 ** 6) or self.board.ulica() == 'river':
            return
            
        else:
            help = self.FD(listaS, boardV, handS)
            # nie mam FD
            if not help:
                help = self.bFd(listaS, boardV, handS)
                # nie mam bFd
                if not help:
                    pass
                # mam bFd
                else:
                    if help[1] == 13:
                        self.nazwa += ' + nbFd'
                    else:
                        self.nazwa += ' + bFd(%s)' % help[1]
            # mam FD
            else:
                if help[1] == 13:
                    self.nazwa += ' + nFD'
                else:
                    self.nazwa += ' + FD(%s)' % help[1]
                    self.kickerFD = help[1]
                    
            help = self.OESD(listaV, boardV, handV)
            # nie mam OESD
            if not help:
                help = self.doubleBelly(listaV, boardV)
                # nie mam doubleBelly
                if not help:
                    help = self.GS(listaV, boardV, handV)
                    # nie mam GS
                    if not help:
                        help = self.boesd(boardV, handV)
                        # nie mam boesd
                        if not help:
                            pass
                        # mam boesd
                        else:
                            self.nazwa += ' + boesd'
                    # mam GS
                    else:
                        if help[2] == 'idiotEnd':
                            pass
                        else:
                            self.nazwa += ' + GS'
                # mam doubleBelly
                else:
                    if help[2] == 'idiotEnd':
                        pass
                    else:
                        self.nazwa += ' + doubleBelly'
                        
            # mam OESD
            else:
                if help[3] == 'MEGAidiotEnd':
                    pass
                elif help[3] == 'idiotEnd':
                    self.nazwa += ' + GS'
                else:
                    self.nazwa += ' + OESD(%(x)s) %(y)skartowy' % {'x':help[1], 'y': help[2]}
                
            # okreslam value
            # mam 1P
            if '1P' in self.nazwa:
                # mam nFD
                if 'nFD' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 29 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 29.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 24 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 18 * 10 ** 6
                # mam nienutsowego FD
                elif 'FD' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 28 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 28.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 24 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 17 * 10 ** 6
                # mam bFd
                elif 'bFd' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 12 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 12.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 1 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        if 'TP' not in self.nazwa and 'OvP' not in self.nazwa:
                            self.value += 0.01 * 10 ** 6
                # nie mam zadnego FD bFd
                else:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 7 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 7.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 0.6 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 0
            # nie mam 1p
            else:
                # mam nFD
                if 'nFD' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 37 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 37.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 21 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 10 * 10 ** 6
                        
                    if '2OC' in self.nazwa:
                        self.value += 30 * 10 ** 3
                        
                # mam nienutsowego FD
                elif 'FD' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 36 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 36.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 20 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 9 * 10 ** 6
                        
                    if '2OC' in self.nazwa:
                        self.value += 30 * 10 ** 3
                        
                # mam bFd
                elif 'bFd' in self.nazwa:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 9 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 9.1 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        self.value += 8.05 * 10 ** 6
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        self.value += 5 * 10 ** 6
                        
                    if '2OC' in self.nazwa:
                        self.value += 30 * 10 ** 3
                        
                # nie mam zadnego FD bFd
                else:
                    # mam OESD
                    if 'OESD' in self.nazwa:
                        self.value += 8.6 * 10 ** 6
                    # mam doubleBelly
                    elif 'doubleBelly' in self.nazwa:
                        self.value += 8.7 * 10 ** 6
                    # mam GS
                    elif 'GS' in self.nazwa:
                        if '2OC' in self.nazwa:
                            self.value += 8.01 * 10 ** 6
                        else:
                            self.value += 7 * 10 ** 6
                        
                    # nie mam zadnego OESD, doubleBelly, GS
                    else:
                        if '2OC' in self.nazwa:
                            self.value += 6 * 10 ** 6
        
    def blefingValue(self, raising = False):
        if raising:
            # blefy do raisowania
            pass
        else:
            if 'FD' in self.nazwa or 'OESD' in self.nazwa or 'doubleBelly' in self.nazwa or 'GS' in self.nazwa or 'bFd' in self.nazwa:
                self.bv = True
            else:
                self.bv = False
'''
1. poker                            90m
2. kareta                            80m
3. full                                70m
4. flush                            60m
5. str8                                50m
6. trips                            42m
7. 1P + FD + OESD                    36-40m
8. FD + OESD                         36m
8. 1P + FD + GS                        31-35m
9. 2P                                30m
10. 1P + FD                            25-29m
11. 1P+ OESD + bFd                    20-24m
12. FD + GS                            20m
13. 1P + OESD                        15-19m
14. OvP                                12m
15. TPGK                             11m
16. nFD                                10m
17. 1P + GS + bFd                    9+m
18. OESD + bFd                        9m
19. FD                                9m
18. 1P + GS                            8.6 - 9m bez 9
19. OESD                            8.6m
20. TP                                8.3 - 8.7m
19. 1P + bFd                        8.3 - 8.7m
20. 1P                                8-8.4m            
20. GS + bFd                        8.2 - 8.4m
21. GS + TwoOC                        7.8m
21. GS                                7m
22. TwoOC                            6m
23. bFd                                5m
'''
'''
FD + OESD =     {28m gdy 1P
                {36m gdy ~1P

FD + GS =         {23m gdy 1P
                {20m gdy ~1P
                
FD  =             {17m gdy 1P
                {9m gdy ~1P
                
OESD + bFd =     {12m gdy 1P
                {9m gdy ~1P
                
OESD =             {7m gdy 1P
                {8.6m gdy ~1P
                
GS + bFd =         {0.86m gdy 1P
                {8.1m gdy ~1P
                
GS =             {0.6m gdy 1P
                {7m gdy ~1P
                
bFd =             {0.019m gdy 1P
                {5m gdy ~1P
gdy sparowany board obnizam wszystko o 2mln (lub do 0)
'''