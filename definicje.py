def zapisujWynikiDo1Pliku(plik):

    with open(plik) as files:
        x = files.read()
    x = x.split()

    with open(wszystko.txt,a) as files:
        for nazwa in x:
            files.write(nazwa + '\n')


def wypiszLiterowki(alfabet): # wypisuje wszystkie literowki z podanej listy znakow
    # alfabet = ['z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','p','o','i','u','y','t','r','e','w','q']
    # alfabet1 = ['1','2','3','4','5','6','7','8','9','0']

    
    ile_liter = input('podaj liczbe liter: ')
    ile_liter = int(ile_liter)
    ciag = ''
    if ile_liter == 1:
        for letter in alfabet:
            ciag = ciag + letter + ' '
        alfabet1 = ciag.split()
    else:
        for letter in alfabet: 
            index = 0
            while index < len(alfabet):
                ciag = ciag + letter + alfabet[index] + ' '
                index += 1

        alfabet1 = ciag.split()
        
        index = 0
        while index < ile_liter - 2:
            ciag1 = ''
            for letter in alfabet:
                index1 = 0
                while index1 < len(alfabet1):
                    ciag1 = ciag1 + letter + alfabet1[index1] + ' '
                    index1 += 1
                
            alfabet1 = ciag1.split()
            index += 1
    return alfabet1

def wczytajPlikDoListy(y):
    files = open (y)
    x = files.read()
    files.close()
    x = x.split()
    return x

def wyczyscListeZPowtarzajacychElementow(b): # b to lista
    i = 0
    y = []
    for letter in b:
        if letter not in b[:i]:
            y.append(letter)
        else:
            pass
        i += 1
    return y

def plikDoListy(plik): # linie
    files = open (plik)
    a = files.readlines()
    files.close()
    return a
    
def zapiszWszystkiePliki(sciezka, rozszerzenie):
    import os
    x = os.listdir(sciezka)
    for b in x:
        if not b.endswith(rozszerzenie):
            x.remove(b)

    with open('wszystko.txt', 'w') as files:
        for line in x:
            with open(sciezka + line) as files1:
                a = files1.read()
                files.write(a + '\n')

    # files = open (wszystko.txt, w)
    # for line in x:
    #     files1 = open (sciezka + line)
    #     a = files1.read()
    #     files1.close()
    #     print (a, file = files)
    # files.close()