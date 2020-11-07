import random as rd
from itertools import chain

def vytvor_tabulku(vyska,sirka):
    #Funkce vytvoří tabulku podle zadané výšky a šířky
    #Vstupní tabulka
    tabulka = []
    #Naplnění tabulky
    for i in range(vyska):
        tabulka_vnorena = []
        for b in range(sirka):
            tabulka_vnorena.append(".")
        tabulka.append(tabulka_vnorena)
        
    return tabulka

def nakresli_mapu(souradnice,seznam_ovoce,kolo):
    #Funkce přepíše prvek podle zvolených souřadnic a vykreslí tabulku
    #Vytvoření tabulky
    tabulka = vytvor_tabulku(vyska,sirka)

    #Přepsání prvku "." za "x"
    for prvek in souradnice:
        x,y = prvek
        tabulka[x][y] = "x"
        
    #Přepsání prvku "." za "o"
    for prvek in seznam_ovoce:
        x,y = prvek
        tabulka[x][y] = "o" 
        
    #Vytvoreni ovoce
    if "o" not in chain(*tabulka): 
        seznam_ovoce = ovoce(tabulka)
     #Vytvoření ovoe ve 30 kole   
    if kolo == 30:
        seznam_ovoce = ovoce(tabulka)
    else:
        pass
    print(kolo)   
    #Vykreslení tabulky    
    for tabulka_vnorena in tabulka:
        for prvek in tabulka_vnorena:
            print(prvek, end=' ')
        print()


def pohyb(souradnice,smer,seznam_ovoce):
    #Přiřazení souřadnic
    x,y = souradnice [-1]
    #Tah na východ
    if smer == "v":
        y_nove = y+1
        souradnice.append((x,y_nove))
    #Tah na západ
    elif smer == "z":
        y_nove = y-1
        souradnice.append((x,y_nove))
    #Tah na jih   
    elif smer == "j":
        x_nove = x+1
        souradnice.append((x_nove,y))
    #Tah na sever   
    elif smer == "s":
        x_nove = x-1
        souradnice.append((x_nove,y))

    #Ochrana proti nabourani do těla
    if len(souradnice) != len(set(souradnice)):
        raise ValueError("Game over")
    
    #Ochrana proti narazu do zdi sever, zapad
    if souradnice [-1][0] < 0 or souradnice [-1][1] < 0 :
        raise ValueError("Game Over")
        
    #Ochrana proti narazu do zdi jih východ 
    elif souradnice [-1][0] >= vyska or souradnice [-1][1] >= sirka: 
         raise ValueError("Game Over") 
    #Kontrola požrání     
    pozrani = set(seznam_ovoce) & set(souradnice) 

   #Zachování delky při požrání
    if len(pozrani) == 0: 
        del(souradnice[0])
    else:
        del(seznam_ovoce[0])
        
def ovoce(tabulka):
    while True:
        souradnice_x =rd.randrange(0,sirka-1)
        souradnice_y= rd.randrange(0,vyska-1)
        
        if tabulka[souradnice_x][souradnice_y] == "x":
            continue
        else:
            seznam_ovoce.append((souradnice_x,souradnice_y))
            break
       
    return seznam_ovoce

def had():
    global sirka,vyska,seznam_ovoce,kolo
    #Výchozí souřadnice
    souradnice = [(0, 0), (1, 0), (2, 0)] 
    #Rozměry pole
    vyska = 10
    sirka = 10
    #Počítadlo kol
    kolo = 0
    #Souradnice ovoce
    seznam_ovoce = [(2,3)]

    while True:
        smer = input("Zadej smer (s,j,v,z):")
        kolo = kolo + 1
        if kolo > 30:
            kolo = 0
        pohyb(souradnice,smer,seznam_ovoce)
        nakresli_mapu(souradnice,seznam_ovoce,kolo)

had()
