import rozne, definicje
from Hand import *
import numpy


class Stan(object):
    def setBoard(self, board):
        # jaki jest board
        self.board = board
        
    def setPrzeciwnik(self, przeciwnik):
        # statystyki przeciwnika - docelowo klasa Przeciwnik
        self.przeciwnik = przeciwnik
        
    def setCzyOtwarta(self, czyOtwarta):
        # czy pula byla otwarta
        self.czyOtwarta = czyOtwarta
        
    def setJa(self, ja):
        # ja to obiekt reprezentujacy mnie (class Ja)
        self.ja = ja
        
    def getJa(self):
        return self.ja
        
    def getBoard(self):
        # jaki jest board
        return self.board
        
    def getPrzeciwnik(self):
        # statystyki przeciwnika - docelowo klasa Przeciwnik
        return self.przeciwnik
        
    def getCzyOtwarta(self):
        # czy pula byla otwarta
        return self.czyOtwarta
        
class Gracz(object):
    def setPozycja(self, pozycja):
        # jaka jest pozycja gracza
        self.pozycja = pozycja.upper()

    def pozycja(self):
        # jaka mam pozycje
        return self.pozycja
        
    def setZakres(self, zakres):
        # zakres gracza
        self.zakres = zakres
        
    def getZakres(self):
        # zakres gracza
        return self.zakres

class Ja(Gracz):
    def setReka(self, reka):
        # moja reka
        self.reka = reka
    
    def reka(self):
        return self.reka
        
    def setInicjatywa(self, inicjatywa):
        # inicjatywa to boolean mowiacy czy mam inicjatywe
        self.inicjatywa = inicjatywa
        
    def inicjatywa(self):
        return self.inicjatywa
        
    def setWzglednaPozycja(self, pozycja):
        # pozycja to bool mowiacy czy mam pozycje nad przeciwnikiem w HU
        self.wzglednaPozycja = pozycja
        
    def wzglednaPozycja(self):
        return self.wzglednaPozycja
        
class Przeciwnik(Gracz):
    # wszystko co moge wiedziec o przeciwniku, jego nick, jego staty, jego pozycja
    def __init__(self): # nie wiem czy dobry jest ten init, czy nie psuje czegos przy dziedziczeniu
        self.staty = {}
        
    def __str__(self):
        try:
            return self.nazwa
        except:
            return 'BRAK NICKU'
            
    def setNick(self, nazwa):
        self.nazwa = nazwa
        
    def addStatystyka(self, nazwa_staty, stata):
        self.staty[nazwa_staty] = stata
        
    def setStatystyki(self, staty):
        # staty to slownik ze statami
        self.staty = staty
        
    # def agroRange(self):
        # # range z ktorym jest agresywny, raisuje, albo cbetuje
        
        
    # def pasivRange(self):
        # # range z ktorym jest pasywny, czyli C lub X/C
        
    def statystyki(self):
        return self.staty
    
class Board(object):
    # wszystko co moge wiedziec o boardzie, jaki jest, czy jest mokry, sparowany, suchy itd,
    def __init__(self, board):
        self.board = board
        self.karty = []
        i = 0
        for el in self.board:
            if i % 2 == 1:
                self.karty.append(Karta(self.board[i - 1] + self.board[i]))
            i += 1
            
        self.talia = Talia()
        for karta in self:
            self.talia.usun(karta)
            
    def __add__(self, karta):
        self.karty.append(karta)
        self.board += str(karta)
        return self
        
    def __str__(self):
        napis = ''
        for el in self.karty:
            napis += str(el)
        return napis
    
    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i == len(self.karty):
            raise StopIteration
        self.i += 1
        return self.karty[self.i - 1]
    
    def losujNastepny(self, reka = False):
        # losuje nastepny strit
        if not reka:
            karta = self.talia.losuj()
            self.talia.usun(karta)
            self += karta
        else:
            for karta in reka:
                self.talia.usun(karta)
            karta = self.talia.losuj()
            self.talia.usun(karta)
            self += karta
        
    def liczby(self):
        liczbyx = []
        for karta in self:
            liczbyx.append(karta.liczba())
        lista = sorted(liczbyx, reverse = True)
        return lista
        
    def suits(self):
        suitsx = []
        for karta in self:
            suitsx.append(karta.suit())
        return suitsx
        
    def boardMax(self):
        return self.boardLiczby()[0]
        
    def ulica(self):
        if len(self.board) == 0:
            self.strit = 'preflop'
            return 'preflop'
        elif len(self.board) == 6:
            self.strit = 'flop'
            return 'flop'
        elif len(self.board) == 8:
            self.strit = 'turn'
            return 'turn'
        else:
            self.strit = 'river'
            return 'river'
    
    def czySparowany(self):
        # niesamodzielna
        # boardV = rozne.toNumbers(rozne.values(self.board))
        boardV = self.liczby()
        help = list(numpy.unique(boardV))
        checker = False
        for el in boardV:
            if boardV.count(el) == 3:
                self.nazwa += ' trips'
                checker = True
                break
        
        if not checker:
            if len(boardV) - 2 == len(help):
                self.nazwa += ' 2 pary'
            elif len(boardV) - 1 == len(help):
                self.nazwa += ' sparowany'
            else:
                self.nazwa += ' bez pary'
    
    def sparowanaKarta(self):
        # jezeli board jest sparowany to zwraca wartosc karty sparowanej np. 12 na boardzie KKx; jezeli board jest niesparowany to zwraca None
        help = self.liczby()
        for el in help:
            if help.count(el) == 2:
                return el
                
    def kolor(self):
        self.ulica()
        kolory = self.suits()
        if self.strit == 'river':
            kolory1 = kolory[:-1]
            for el in kolory:
                if kolory.count(el) == 5:
                    self.nazwa = 'mono five2flush'
                    break
                elif kolory.count(el) == 4:
                    self.nazwa = 'four2flush'
                    break
                elif kolory.count(el) == 3:
                    self.nazwa = 'three2flush'
                    break
                else:
                    # wiem, ze nie ma koloru, sprawdzam czy byly jakies drawy na wczesniejszych stritach
                    checker = True
                    for el1 in kolory1:
                        if kolory1.count(el1) == 2:
                            self.nazwa = 'mFd'
                            checker = False
                            break
                    
                    if checker:
                        self.nazwa = 'rainbow'
        
        else:
            liczbaFD = 0
            for el in kolory:
                checker = False
                if kolory.count(el) == len(kolory):
                    if kolory.count(el) == 4:
                        self.nazwa = 'mono four2flush'
                        checker = True
                        break
                    else:
                        self.nazwa = 'mono three2flush'
                        checker = True
                        break
                    
                elif kolory.count(el) == 3:
                    self.nazwa = 'three2flush'
                    checker = True
                    break
                
                if not checker:
                    if kolory.count(el) == 2:
                        # bo jak kolory sa: ssch to dwa razy doda 0.5 za kazde s
                        liczbaFD += 0.5
            
            if not checker:
                if liczbaFD == 0:
                    self.nazwa = 'rainbow'
                elif liczbaFD == 1:
                    self.nazwa = 'FD'
                elif liczbaFD == 2:
                    self.nazwa = '2xFD'
                    
    def czyGS(self, board2):
        '''funkcja pomocnicza wykorzystywana tylko do funkcji str8
        powinna dzialac na wszystkich dlugosciach boardu
        
        rozpatruje serie 4 kolejnych kart i patrzy czy jest tam GS'''
        checker = True
        if len(board2) < 4:
            pass
        else:
            board3 = list(board2)
            if 13 in board3:
                board3.append(0)
            ileGS = 0
            for i in range(len(board3) - 3):
                if board3[i] - board3[i + 3] == 4:
                    checker = False
                    ileGS += 1
                
            if ileGS == 2:
                self.nazwa += ' + doubleGS'
            elif ileGS == 1:
                self.nazwa += ' + GS'
            else:
                pass
                
        if checker:
            self.czy3(board2)
                
    def czy3(self, board2):
        '''funkcja pomocnicza wykorzystywana tylko do funkcji str8
        
        rozpatruje serie 3 kolejnych kart'''
        board3 = list(board2)
        if 13 in board3:
            board3.append(0)
        for i in range(len(board3) - 2):
            if 'mozliw' in self.nazwa:
                continue
            if board3[i] - board3[i + 2] == 2 and board3[i] < 12 and board3[i + 2] > 1 :
                self.nazwa += ' + (3 mozliwe strity)'
            elif board3[i] - board3[i + 2] <= 3 and (board3[i] == 12 or board3[i + 2] == 1):
                self.nazwa += ' + (2 mozliwe strity)'
            elif board3[i] - board3[i + 2] <= 4 and (board3[i] == 13 or board3[i + 2] == 0):
                self.nazwa += ' + (1 mozliwy strit)'
            elif board3[i] - board3[i + 2] == 3:
                self.nazwa += ' + (2 mozliwe strity)'
            elif board3[i] - board3[i + 2] == 4:
                self.nazwa += ' + (1 mozliwy strit)'
                
    def czy4(self, board2):
        '''funkcja pomocnicza wykorzystywana tylko do funkcji str8
        
        rozpatruje serie 4 kolejnych kart'''
        checker = False
        if len(board2) < 4:
            pass
        else:
            board3 = list(board2)
            if 13 in board3:
                board3.append(0)
            for i in range(len(board3) - 3):
                # nie moze byc 2 serii 4 kolejnych kart na jednym boardzie tak, zeby nie bylo str8 (wiec spoko)
                if board3[i] - board3[i + 3] == 3:
                    checker = True
                    # jak A jest w serii 4 kart to to jest tylko GS
                    if board3[i] == 13: 
                        self.nazwa += ' + GS'
                    elif board3[i + 3] == 0:
                        self.nazwa += ' + GS'
                    else:
                        self.nazwa += ' + four2str8'
        
        # nie bylo 4 kolejnych kart, wiec rozpatruje serie 3 kolejnych kart
        if not checker:
            self.czyGS(board2)
            
    def str8(self): # duzo rzeczy moze nie dzialac - jeszcze nie sprawdzona
        self.kolor()
        # if self.nazwa == 'mono' and self.strit == 'river':
            # pass
        # else:
        # board = rozne.toNumbers(rozne.values(self.board))
        board = self.liczby()
        board2 = list(numpy.unique(board))
        board2.sort(reverse = True)
        if len(board2) == 5:
            board3 = list(board2)
            if 13 in board3:
                board3.append(0)
                # czyli wiem, ze jest A, wiec jak mam K na stole to str8 moze byc tylko broadwayem, jak
                # nie mam K to str8 moze byc tylko wheelem
                if 12 in board3:
                    board3.remove(0)
                else:
                    board3.remove(13)
                
            if board3[0] - board3[4] == 4:
                self.nazwa += ' + str8'
            # nie mam strita
            else:
                # funkcja czy4 najpierw sprawdza czy sa 4 kolejne karty na stole, jak nie ma to sprawdza czy
                # jest GS albo podwojny GS na stole, jak nie ma to sprawdza czy sa 3 kolejne karty na stole
                self.czy4(board2)
                
        else:
            self.czy4(board2)
    
    def getNazwa(self):
        self.str8()
        self.czySparowany()
        return self.nazwa
    
class Zakres(object):
    # ma byc wszystko o zakresie
    def __init__(self, zakres):
        self.talia = Talia()
        self.zakres = []
        try: # jak sie uda to znaczy ze zakres nie jest pusty
            for el in rozne.makerange(zakres):
                self.zakres.append(el)
        except IndexError: # zakres byl pusty (czyli po prostu chcialem go stworzyc i potem cos do niego dodawac)
            pass
            # print ('zakres byl pusty')
        
    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i == len(self.zakres):
            raise StopIteration
        self.i += 1
        return self.zakres[self.i - 1]
    
    def __sub__(self, other):
        nowy = []
        for hand in self:
            if hand in other:
                pass
            else:
                nowy.append(hand)
        
        self = Zakres(nowy)
        return self
        
    def __add__(self, other):
        nowy = list(self.zakres)
        if type(other) is Hand:
            nowy.append(other)
        
        else:
            for hand in other:
                if hand in self:
                    pass
                else:
                    nowy.append(hand)
                
        self = Zakres(nowy)
        return self
        
    def __len__(self):
        try:
            return len(list(self.rece()))
        except:
            return len(self.zakres)
            
    def setBoard(self, board):
        self.board = board
        pomoc = []
        for hand in self.zakres:
            checker = True
            for karta in self.board:
                if karta in hand:
                    checker = False
                    
            if checker:
                pomoc.append(hand)
        self.zakres = pomoc
        
    def helpDoSetBoard(self):
        # stworzone tylko po to, zeby na biezaco aktualizowalo board przy porzadkowaniu range (def porzadkuj)
        help = list(self.zakres)
        self.zakres = []
        for reka in help:
            i, u = 0,0
            for karta in reka:
                i += 1
                if karta not in self.board:
                    u += 1
            if i == u:
                reka.setBoard(self.board)
                self.zakres.append(reka)
                
    def porzadkuj(self, reverse = False, AI = False):
        '''reverse = True - zakres daje najpierw najslabsze rece, AI = True - to tylko preflop - rece sortowane wg equity przy all inach a nie wg grywalnosci'''
        try: # jak jest board(czyli postflop) to to sie uda, jak nie ma boardu to sie nie uda, czyli jest preflop
            if self.board: # tylko po to, ze jak nie ma self.board to zeby juz tu wysypywalo
                pass
            self.helpDoSetBoard()
            self.posegregowanyZakres = []
            for el in self.zakres:
                # posegregowanyZakres.append((el.liczba(), el.reka()))
                self.posegregowanyZakres.append((el.liczba(), el))
            self.posegregowanyZakres.sort(reverse = True)
            zakres = []
            for el in self.posegregowanyZakres:
                zakres.append(el[1])
            self.zakres = zakres
            if reverse:
                self.zakres = self.zakres[::-1]
            return self.zakres
            
        except AttributeError:
            if AI: # to jest w miare dobra segregacja do AI kiedy to ja wrzucam. jak ktos mi wrzucil a ja mam callowac pewnie da sie to zrobic lepiej (bo inny range jest wrzucony i z czym innym calle)
                help = '''AA,KK,AKs,QQ,AKo,JJ,TT,AQs,99,AQo,88,AJs,77,66,ATs,87s,76s,65s
                        ,A5s,A4s,A3s,A2s,AJo,KQs,55,ATo,A9s,KJs,A8s,KQo,98s,A7s,A9o,A8o,KTs,A6s
                        ,44,A7o,QJs,KJo,K9s,KTo,33,QTs,A5o,A6o,QJo,K8s,JTs,A4o,K9o,A3o,Q9s,A2o,K7s,QTo,22,K6s
                        ,K8o,Q8s,K5s,J9s,K7o,JTo,Q9o,K4s,K3s,T9s,K6o,Q7s,J8s,K2s,Q8o,Q6s,K5o,J9o,T8s,Q5s,K4o,J7s,K3o,Q4s,T9o
                        ,Q7o,Q3s,K2o,J3s,J8o,Q6o,T7s,Q2s,J6s,Q5o,J5s,97s,T8o,J7o,Q4o,T6s,J4s,Q3o,98o,96s,86s,T7o,J6o
                        ,Q2o,J2s,T5s,J5o,T4s,97o,J4o,95s,T3s,87o,85s,75s,54s,T6o,J3o,T2s,94s,96o,64s,84s,74s,86o,76o
                        ,53s,J2o,T5o,T4o,93s,95o,92s,43s,63s,83s,65o,73s,85o,75o,82s,52s,T3o,T2o,94o,54o,42s,62s,72s,64o,32s
                        ,84o,74o,53o,43o,93o,92o,63o,83o,82o,73o,52o,42o,72o,62o,32o'''
            else:
                help = '''AA,KK,AKs,QQ,AKo,AQs,JJ,TT,AJs,KQs,AQo,ATs,KJs,QJs,KTs,99,QTs,88,AJo,JTs,66,77,55,A4s
                        ,A5s,A9s,KQo,KJo,K9s,A3s,A2s,98s,87s,76s,65s,44,T9s,A8s,J9s,Q9s,33,ATo,A7s,K8s
                        ,T8s,22,A6s,Q8s,QJo,J8s,K7s,A9o,A8o,A7o,QTo,JTo,KTo,A5o,K6s,T7s,97s
                        ,A4o,A6o,K5s,J7s,86s,A3o,A2o,Q6s,K9o,T9o,96s,Q7s,K4s,J9o,75s,54s,Q9o,T6s
                        ,K3s,Q5s,98o,K2s,J6s,85s,K8o,K7o,T8o,64s,K6o,Q4s,J5s,K5o,Q3s,J4s,95s,87o
                        ,Q8o,K4o,J8o,K3o,K2o,Q2s,74s,J3s,T5s,T4s,97o,Q7o,Q6o,76o,Q5o,T7o,J7o,J2s,Q4o,84s,Q3o,T3s
                        ,86o,J6o,J5o,T2s,94s,J4o,T6o,J3o,96o,J2o,93s,T5o,T4o,Q2o,95o,T3o,92s,T2o
                        ,85o,83s,75o,82s,94o,93o,65o,73s,53s,63s,84o,43s,74o,54o,72s,64o,52s,92o,62s,83o,42s,82o,73o
                        ,53o,63o,32s,43o,72o,52o,62o,42o,32o'''
                        
            help = rozne.makerange(help)
            zakres1 = list(self.zakres)
            self.zakres = []
            for hand in help:
                if hand in zakres1:
                    self.zakres.append(hand)
            
            if reverse:
                self.zakres = self.zakres[::-1]
            return self.zakres
    
    def topProcent(self, procent):
        # procent to ma byc 0 < int < 100
        # poki co tylko jak jest ustalony board, ale dorobic preflop
        self.porzadkuj()
        procent = procent / 100
        self.zakres = self.zakres[:round(len(self) * procent)]
    
    def equity(self, other):
        # liczy equity tego zakresu, na inny zakres (tylko postflop, wiec musi byc board podany)
        other.setBoard(self.board)
        eq = 0
        for el in self.czysc():
            reka,waga = el
            eq += reka.equityRange(other,self.board)*waga
                
        return round(eq / len(self),2)
        
    def czysc(self):
        # zeby szybciej liczyc equity, to nie chce zeby mi liczyl za kazdym razem equity rak, ktore na danym boardzie graja
        # identycznie, wiec wystarczy, ze w zakresie zostana mi rece o innych value, i wagi tych rak (zeby zachowac proporcje)
        self.porzadkuj()
        pomoc = {}
        for hand in self.posegregowanyZakres:
            klucz,reka = hand
            if pomoc.get(klucz) is None:
                pomoc[klucz] = (reka,1)
            else:
                reka,waga = pomoc[klucz]
                waga += 1
                pomoc[klucz] = (reka,waga)
        
        # to bedzie lista skladajaca sie z tupli (x,y) gdzie x to reka, a y to jej waga
        return list(pomoc.values())
                    
    def jakiboard(self):
        return self.board
            
class Premium(Zakres):
    def __init__(self):
        self.zakres = []
        for hand in rozne.makerange('QQ+,AKs,AKo'):
            self.zakres.append(hand)
            
class Karta(object):
    def __init__(self,karta):
        self.karta = karta[0].upper() + karta[1]
        
    def __str__(self):
        return self.karta
        
    def __eq__(self, other):
        return self.karta[0] == other.karta[0] and self.karta[1] == other.karta[1]
        
    def __gt__(self, other):
        return self.karta[0] > other.karta[0]

    def __add__(self, other):
        return self.karta + other.karta
    
    def liczba(self):
        karty = '023456789TJQKA'
        liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        liczba = liczby[karty.find(self.karta[0])]
        return liczba
        
    def suit(self):
        return self.karta[1]
        
    def nazwa(self):
        if self.liczba() > 8:
            return 'wysoka'
        elif self.liczba() > 5:
            return 'srednia'
        else:
            return 'niska'
        
class Talia(object):
    def __init__(self):
        self.talia = []
        for el in '23456789tjqka':
            for el1 in 'csdh':
                self.talia.append(Karta(el + el1))
    
    def __iter__(self):
        self.i = 0
        return self
        
    def __next__(self):
        if self.i >= len(self.talia):
            raise StopIteration
        self.i += 1
        return self.talia[self.i - 1]
    
    def losuj(self):
        import random
        return random.choice(self.talia)
        
    def getTalia(self):
        return self.talia
        
    def usun(self, karta):
        for el in self.talia:
            if el == karta:
                self.talia.remove(el)

'''                
class Zagranie(object):
    def __init__(self, przeciwnik):
        self.przeciwnik = przeciwnik # Przeciwnik
        
    def setPula(self, pula):
        self.pula = pula
        
    def setSizing(self, sizing):
        self.sizing = sizing
        
    def foldIP(self):
        pass
        
    def callIP(self):
        pass
        
    def raiseIP(self):
        pass
        
    def foldVsDB(self):
        pass
        
    def callVsDB(self):
        pass
        
    def raiseVsDB(self):
        pass
        
    def xbIP(self):
        pass
        
    def xFold(self):
        pass
        
    def xCall(self):
        pass
        
    def xRaise(self):
        pass
        
    def betFoldIP(self):
        pass
        
    def betFoldOOP(self):
        pass
        
    def betCallIP(self):
        pass
        
    def betCallOOP(self):
        pass
        
    def betRaiseIP(self):
        pass
        
    def betRaiseOOP(self):
        pass
        
    def procentValue(self, sizing, pula):
        # okresla stopien polaryzacji zakresu przeciwnika w zaleznosci od sizingu
        pass
'''
