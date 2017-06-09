from klasy import *
from Hand import *

def suited(hand):
	hand = hand[0]+'s'+ hand[1]+'s'+',' + hand[0]+'c'+ hand[1]+'c'+',' + hand[0]+'d'+ hand[1]+'d'+',' + hand[0]+'h'+ hand[1]+'h' + ','
	return hand

def offsuit(hand):
	hand = hand[0]+'s'+ hand[1]+'d'+',' + hand[0]+'s'+ hand[1]+'h'+',' + hand[0]+'s'+ hand[1]+'c'+',' + hand[0]+'c'+ hand[1]+'h' + ',' + hand[0]+'c'+ hand[1]+'s'+',' + hand[0]+'c'+ hand[1]+'d'+',' + hand[0]+'d'+ hand[1]+'h'+',' + hand[0]+'d'+ hand[1]+'s' + ',' + hand[0]+'d'+ hand[1]+'c'+',' + hand[0]+'h'+ hand[1]+'c'+',' + hand[0]+'h'+ hand[1]+'d'+',' + hand[0]+'h'+ hand[1]+'s' + ','
	return hand

def pair(hand):
	hand = hand[0]+'d'+ hand[1]+'s'+',' + hand[0]+'h'+ hand[1]+'s'+',' + hand[0]+'s'+ hand[1]+'c'+',' + hand[0]+'h'+ hand[1]+'c' + ',' + hand[0]+'d'+ hand[1]+'c'+',' + hand[0]+'d'+ hand[1]+'h' + ','
	return hand

def karlic(x):     # przypisuje liczby odpowiednie dla wysokosci kart
	lista = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	if x in lista:
		x = lista.index(x) + 1
		
	else:
		raise ValueError('Podalem zly element')
	return x

def przedzial(x,y):		# wypisuje wszystkie liczby z przedzialu od x do y wlacznie
	a = ''
	if x < y :
		while x <= y:
			a = a + str(x) + ' '
			x = x + 1
		return a
	if x > y :
		while y <= x:
			a = a + str(y) + ' '
			y = y + 1
	if x == y:
		a = x
	return a
	
def lickar(x): 		# przypisuje z powrotem karty od liczby
	lista = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	lista1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
	if x in lista1:
		x = lista[lista1.index(x)]
		return x
	elif x in lista2:
		x = lista[lista2.index(x)]
		return x
		
def oddo(cards):				# to ma rozbijac rece typu BB-CC na BB i CC; za pomoca tego mozna tez bedzie zalatwic od razu +, bo + to tylko specyficzny oddo
	if cards[0] == cards [1]: 
		hand = cards[0]
		hand = karlic(hand)
		hand1 = cards[4]
		hand1 = karlic(hand1)
		hands = przedzial(hand,hand1)
		hands = hands.split()
		zakres = ''
		for number in hands:
			zakres = zakres + lickar(number)*2 + ','
		zakres = zakres[0:len(zakres)-1]
	else:
		hand = cards[1]
		hand = karlic(hand)
		hand1 = cards[5]
		hand1 = karlic(hand1)
		hands = przedzial(hand,hand1)
		hands = hands.split()
		zakres = ''
		for number in hands:
			zakres = zakres + cards[0] + lickar(number) + cards[2] + ','
		zakres = zakres[0:len(zakres)-1]
	return zakres

def plus(cards):
	if cards[0] != cards[1]:
		card = cards[0]
		card = karlic(card)
		card1 = cards[1]
		card1 = karlic(card1)
		hand = cards[0]+lickar(str((int(card)-1)))+cards[2]
		hand1 = cards[0:2]
		hands = hand + '-' + hand1
		zakres = oddo(hands)
	else:
		hand = 'AA'
		hand1 = cards[0:2]
		hands = hand + '-' + hand1
		zakres = oddo(hands)
	return zakres

def makerange(hands):
	if type(hands) is list:
		for hand in hands:
			yield hand
	else:
		zakres1 = ''
		if hands.endswith(','):
			hands = hands[:-1]
		hands = hands.split(',')
		for hand in hands:
			# to znaczy ze to jest konkretna reka, wiec nic nie trzeba z nia juz robic
			if hand[1] in 'csdh':
				yield Hand(hand)
				
			checker = False
			checker1 = False
			if '-' in hand:
				checker = True
			elif '+' in hand:
				checker1 = True
				
			if checker == True:
				zakres1 = zakres1 + oddo(hand) + ','
			elif checker1 == True:
				zakres1 = zakres1 + plus(hand) + ','
			else:
				zakres1 = zakres1 + hand + ','
		
		zakres1 = zakres1[:len(zakres1) - 1]
		zakres1 = zakres1.split(',')
		zakres = ''
		for hand in zakres1:
			if hand[1] in 'cdsh':
				zakres = zakres + hand + ','
			elif hand[0] == hand[1]:
				hand = pair(hand)
				
				if hand.endswith(','):
					hand = hand[:len(hand) - 1]
				hand = hand.split(',')
				for el in hand:
					yield Hand(el)
					
			else:
				if hand[2] == 's':
					hand = suited(hand)
					
					if hand.endswith(','):
						hand = hand[:len(hand) - 1]
					hand = hand.split(',')
					for el in hand:
						yield Hand(el)

				elif hand[2] == 'o':
					hand = offsuit(hand)
					
					if hand.endswith(','):
						hand = hand[:len(hand) - 1]
					hand = hand.split(',')
					for el in hand:
						yield Hand(el)
					
def statsToInts(stats):
	stats = stats.split()
	stats = stats[0]
	staty = stats.split('/')
	i = 0
	for i in range (0, len(staty)):
		staty[i] = int(staty[i])
		i += 1
	return staty

def values(str): # zwraca wysokosci kart ze stringu
	board1 = []
	for i in range (len(str)):
		if i % 2 == 0:
			board1.append(str[i])
	return board1

def suits(str): # zwraca kolory kart ze stringu
	board1 = []
	for i in range (len(str)):
		if i % 2 == 1:
			board1.append(str[i])
	return board1

def toNumbers(list): # zwraca liczby od kart z listy
	lista = []
	for el in list:
		lista.append(karlic(el))
	return lista
	
def czyRekaSuited(str):
	str = suits(str)
	if str[0] == str[1]:
		return True
	else:
		return False

def cardRemoval(range,board): # zwraca range, bez kombinacji, ktorych byc nie moze bo karty sa na boardzie
	if type(range) == list:
		pass
	else:
		range = makerange(range)
	board1 = []
	i = 0
	for el in board:
		if i % 2 == 1:
			board1.append(board[i - 1:i + 1])
		i += 1
	range1 = []
	for el in range:
		checker = True
		for el1 in board1:
			if el1 in el:
				checker = False
		if checker:
			range1.append(el)
			
	return range1
			
def cardRemovalGen(range,board): # zwraca range, bez kombinacji, ktorych byc nie moze bo karty sa na boardzie
	import klasy
	if type(range) == list:
		pass
	else:
		range = makerange(range)
	if type(board) is klasy.Board:
		board = board.getBoard()
	board1 = []
	i = 0
	for el in board:
		if i % 2 == 1:
			board1.append(board[i - 1:i + 1])
		i += 1
	range1 = []
	for el in range:
		checker = True
		for el1 in board1:
			if el1 in el:
				checker = False
		if checker:
			yield el
			
def zrobReke(reka):
	# kiedy reka jest wpisywana konkretnie (np. AdKs)
	reka = reka.strip()
	if len(reka) == 4:
		if reka[0] != reka[2]:
			# czyli pierwsza podana karta jest wyzsza
			if karlic(reka[0].upper()) > karlic(reka[2].upper()):
				reka = reka[0].upper() + reka[1] + reka[2].upper() + reka[3]
				
			# pierwsza podana karta jest nizsza => musze odwrocic ich kolejnosc
			else:
				reka = reka[2].upper() + reka[3] + reka[0].upper() + reka[1]

		else:
			kolejnoscKolorow = ['ds','dh','dc','hs','hc','sc']
			for el in kolejnoscKolorow:
				if reka[1] in el and reka[3] in el:
					reka = reka[0].upper() + el[0] + reka[2].upper() + el[1]
	
	# kiedy reka jest wpisywana ogolnie (np. AKo)
	else:
		niepara = re.compile(r'\w\w\w')
		if niepara.match(reka):
			if reka[2] == 'o':
				reka = reka[0:2].upper() + reka[2]
				reka = rozne.offsuit(reka)
				reka = reka [0:4]
				
			else:
				reka = reka[0:2].upper() + reka[2]
				reka = rozne.suited(reka)
				reka = reka[0:4]
				
		else:
			reka = reka.upper()
			reka = rozne.pair(reka)
			reka = reka[0:4]
			
	return reka
	
def zrobSizing(sizing):
	try:
		sizing = int(sizing) / 100
	except:
		if '/' in sizing:
			sizing = sizing.split('/')
			sizing = int(sizing[0]) / int(sizing[1])
		elif ',' in sizing:
			sizing = sizing.split(',')
			sizing = sizing[0] + '.' + sizing[1]
			sizing = float(sizing)
			
	return sizing

def zdobadzIP():
	'''
	znajduje moje IP sieciowe. (korzystam z kilku sieci, nie chce mi sie za kazdym razem tego zmieniac. musze miec polaczenie z internetem
	'''
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 80))
	a = s.getsockname()[0]
	s.close()
	return a

def tworzBoard(jaki, suit, para = True):
	'''jaki to str 'wysoki' = Ah, 'sredni' = Jh-Kh, 'niski' = reszta
	suit to 'mono', 'fd', 'suchy'
	para to czy board ma byc sparowany'''
	
	values = ['2','3','4','5','6','7','8','9','t','j','q','k','a']
	suits = ['c','h','d','s']
	
	if suit == 'mono':
		para = False
		
	board = ''
	if jaki == 'wysoki':
		board += 'a'
		values = ['2','3','4','5','6','7','8','9','t','j','q','k','a']
	elif jaki == 'sredni':
		board += random.choice(['j','q','k'])
		values = ['2','3','4','5','6','7','8','9','t','j','q','k']
	elif jaki == 'niski':
		values = ['2','3','4','5','6','7','8','9','t']
		
	while len(board) < 3:
		board += str(random.choice(values))
		if len(board) == 2:
			if para:
				if board[0] != board[1]:
					board += str(random.choice(board))
				else:
					values.remove(board[1])
					board += str(random.choice(values))
			else:
				if board[0] != board[1]:
					values.remove(board[0])
					values.remove(board[1])
					board += str(random.choice(values))
				else:
					board = board[0]
					values.remove(board)
					board += str(random.choice(values))
					values.remove(board[1])
					board += str(random.choice(values))
					
	if suit == 'mono':
		kol = random.choice(suits)
		lista = [kol] * 3
	elif suit == 'fd':
		kol = random.choice(suits)
		lista = [kol] * 2
		suits.remove(kol)
		lista.append(random.choice(suits))
	elif suit == 'suchy':
		lista = []
		kol = random.choice(suits)
		lista.append(kol)
		suits.remove(kol)
		kol = random.choice(suits)
		lista.append(kol)
		suits.remove(kol)
		kol = random.choice(suits)
		lista.append(kol)
		
	boardx = ''
	for i in range(3):
		boardx += board[i] + lista[i]
		
	return boardx
	
def stworzBoardy(ile):
	'''Board to klasa z pliku klasy'''
	boardy = []
	jakie = ['wysoki', 'sredni', 'niski']
	kolory = ['suchy', 'mono', 'fd']
	para = [0, 1]
	for el in jakie:
		for el1 in kolory:
			for el2 in para:
				for i in range(ile):
					boardy.append(Board(tworzBoard(el, el1, el2)))
					
	return boardy

def szukamValueZakresow(stan, minValPct):
	'''Stan, Gracz, Zakres to klasy z pliku klasy'''
	import cbetowanie
	zakres = Zakres('22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+,32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,72o+,62o+,52o+,42o+,32o')
	stan = Stan()
	gracz = Gracz()
	stan.setJa(gracz)
	for i in range(1, 100):
		print (i)
		procent = i / 100
		rece = zakres.porzadkuj()[:round(len(zakres.porzadkuj()) * procent)]
		rece = Zakres(rece)
		gracz.setZakres(rece)
		stan.setJa(gracz)
		ile_value = []
		for board in stworzBoardy(2):
			stan.setBoard(board)
			nazwa = board.getNazwa()
			if 'rainbow' in nazwa and 'mozliw' in nazwa and 'niesparowany' in nazwa:
				funkcja = cbetowanie.str8dForV
			elif 'rainbow' in nazwa and 'niesparowany' not in nazwa:
				funkcja = cbetowanie.ParaForV
			elif 'rainbow' in nazwa:
				funkcja = cbetowanie.suchyForV
			elif 'mono' in nazwa:
				funkcja = cbetowanie.monoForV
			elif 'FD' in nazwa and 'niesparowany' in nazwa:
				funkcja = cbetowanie.mokryForV
			elif 'FD' in nazwa and 'niesparowany' not in nazwa:
				funkcja = cbetowanie.paraFDForV
				
			help = funkcja(stan)
			ile_value.append(round(len(help) / rece.dlugosc(), 2))
			
		if (sum(ile_value) / len(ile_value)) < minValPct:
			return i

def przykladowyStan():
	stan = Stan()
	board = Board('Kh9s3d')
	reka = Hand('AhAc')
	ja = Ja()
	mojZakres = Zakres('22+,ATs+,KJs+,QJs,T9s,98s,87s,76s,65s,AJo+,KQo')
	mojZakres.setBoard(board)
	ja.setZakres(mojZakres)
	ja.setReka(reka)
	stan.setJa(ja)
	
	return stan
	
def polaryzacja(zakres, polar, procent):
	from klasy import Zakres
	# zakres to caly zakres, z ktorym jest kontynuacja; polar to stopien polaryzacji [0,1] gdzie 1 to samo value; procent rak calego zakresu, ktory ma tworzyc spolaryzowany zakres
	value, spolaryzowanyZakres = round(procent * len(zakres) * polar), Zakres('')
	blefy = round(procent * len(zakres)) - value
	
	zakresValue = Zakres('')
	zakres.porzadkuj()
	i = 0
	for hand in zakres:
		spolaryzowanyZakres += hand
		zakresValue += hand
		i += 1
		if i == value:
			break
			
	zakres.porzadkuj(reverse = True)
	i = 0
	for hand in zakres:
		spolaryzowanyZakres += hand
		i += 1
		if i == blefy:
			break
	
	srodkowyZakres = zakres - spolaryzowanyZakres
	
	return spolaryzowanyZakres, srodkowyZakres, zakresValue
	
def read_hands(data, limit=-1):
    import re
    pat = re.compile(r'^PokerStars Hand #\d+:.*')
    with open(data) as plk:
        hands = plk.readlines()

    start = []
    i, hand_cnt, limit_flg = 0, 0, False
    for line in hands:
        if pat.match(line):
            start.append(i)
            hand_cnt += 1
            if hand_cnt == limit:
                limit_flg = True
                break
        i += 1

    hands_lst = []
    for i in range(len(start)):
        if i == len(start) - 1:
            if limit_flg:
                break
            hand = Reka(hands[start[i]:len(hands)])
        else:
            hand = Reka(hands[start[i]:start[i + 1]])
        hands_lst.append(hand)
    return hands_lst
