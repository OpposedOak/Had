def vytvor_tabulku(vyska,sirka):
    #Funkce vytvoří tabulku podle zadané výšk a šířky
    #Vstupní tabulka
    tabulka = []
    #Naplěnní tabulky
    for i in range(vyska):
        tabulka_vnorena = []
        for b in range(sirka):
            tabulka_vnorena.append(".")
        tabulka.append(tabulka_vnorena)
        
    return tabulka

def nakresli_mapu(souradnice):
    #Funkce přepíše prvek podle zvolené souřadnice a vykreslí tabulku
    #Vytvoření tabulky
    tabulka = vytvor_tabulku(vyska,sirka)
    #Přepsání prvku . za x
    for prvek in souradnice:
        x,y = prvek
        tabulka[x][y] = "x"
    #Vykreslení tabulky    
    for tabulka_vnorena in tabulka:
        for prvek in tabulka_vnorena:
            print(prvek, end=' ')
        print()

        
def pohyb(souradnice,smer):
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
    
    print(souradnice) 
    
    #Ochrana proti narazu do zdi sever, zapad
    if souradnice [-1][0] < 0 or souradnice [-1][1] < 0 :
        raise ValueError("Game Over")
        
    #Ochrana proti narazu do zdi jih východ 
    elif souradnice [-1][0] >= vyska or souradnice [-1][1] >= sirka: 
         raise ValueError("Game Over")    
    #Vymazání prní souřadnice   
    del(souradnice[0])
    
    
def had():
    global sirka,vyska
    #Výchozí souřadnice
    souradnice = [(0, 0), (1, 0), (2, 0)] 
    #Rozměry pole
    vyska = 10
    sirka = 10

    
    while True:
        smer = input("Zadej smer (s,j,v,z):") 
        pohyb(souradnice,smer)
        nakresli_mapu(souradnice)
        
had()
