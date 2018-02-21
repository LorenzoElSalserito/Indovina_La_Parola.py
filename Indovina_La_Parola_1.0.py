import random


def randomizza_lettere_parole_lista(lista):
    """
        ricordati di utilizzare le copie degli oggetti
        altrimenti il puntatore crea bug
        quando modifichi gli elementi di un oggetto mentre lo iteri
    """
    a = []
    for i in lista:
        parola = [e for e in i]
        random.shuffle(parola)
        print(parola)
        a.append(''.join(parola))
    return a
    
""" 
    def randomizza_lista(lista):
    
        dopo aver randomizzato le lettere della lista devo
        randomizzare la lista stessa per avere sempre risultati
        diversi ad ogni giocata
    
    a = []
    for i in lista:
		random.shuffle (i)
		print i
		a.append(''.join(i))
"""


def verifica (lista):
	i=0
	j=5
	lista = [i:j]
	while i!=j:
        verifica = input('Scrivi qui la parola: ')
        if verifica == lista [i]:
            print ('Bravo! Risposta Esatta!')
            i=i+1
        else:
			print ('Risposta sbagliata! La parola esatta era: ', lista[i])
			i=i+1
			
	if i == j:
		i=j
		j+=5


__main__ ():
	print ('Ciao! Benvenuto ad "Indovina la Parola"')
	print (' ')
	print ('Io sono ENER-OS, e sono qui per farti giocare!')
	print ('Adesso caricherò un set di parole da farti analizzare')
	print (' ')
	print ('Lo scopo del gioco è quello di mostrarti delle parole')
	print ('con le lettere disordinate, e tu dovrai indovinare')
	print ('la parola originale. Divertente no? Cominciamo!')
	lista = ['aereo','automobile','motocicletta','bicicletta',
	         'triciclo','trattore','elicottero','sottomarino',
	         'yatch','teletrasporto','navicella','shuttle',
	         'monociclo','carrozza','camion']
    print (lista[i:j])
    print ('Adesso inizia il Gioco!')
    print ('Le parole da analizzare sono: ', randomizza_lettere_parole_lista(lista[i:j]))

    verifica(lista[i:j])
    
    print ('Hai superato la prima manche, ne restano 2')
    print (lista[i:j]
    print ('Adesso inizia il Gioco!')
    print ('Le parole da analizzare sono: ', randomizza_lettere_parole_lista(lista[i:j]))

    verifica(lista[i:j])
    
    print ('Hai superato la seconda manche, resta la manche FINALE')
    print (lista[i:j]
    print ('Adesso inizia il Gioco!')
    print ('Le parole da analizzare sono: ', randomizza_lettere_parole_lista(lista[i:j]))

    verifica(lista[i:j])

    print ('Hai completato con successo la versione 1.0 del gioco!')
    print ('Spero che ti sia divertito! Ti aspetto per una nuova partita')
    print ('CIAO!')
