import random

#print(u"\u2764") #srce
#print(u"\u2663") #tref
#print(u"\u2660") #pik
#print(u"\u25C6") #karo
#print(u"\U0001F929") #skocko (faca sa zvezdama u ocima)
#print(u"\u2605") #zvezda
#print(u"\U0001F534") #crveni krug
#print(u"\U0001F7E1") #zuti krug
#SIMBOLI = [u"\u2764", u"\u2663", u"\u2660", u"\u25C6", u"\U0001F929", u"\u2605"]

SIMBOLI = []

file = open("skockofile.txt", "r", encoding="utf-8")
content = file.readlines()
for line in content:
    SIMBOLI = line.split("|")
file.close()
#print(*SIMBOLI, sep="   ")

""" def generator():
    prvi = random.choices(SIMBOLI) 
    drugi = random.choices(SIMBOLI)
    treci = random.choices(SIMBOLI)
    cetvrti = random.choices(SIMBOLI)
    kombinacija = prvi + drugi + treci + cetvrti
    #print(kombinacija[0],kombinacija[1],kombinacija[2],kombinacija[3]) 
    return kombinacija"""

def generator():
    kombinacija =[random.choice(SIMBOLI) for n in range(4)]
    #print(kombinacija[0],kombinacija[1],kombinacija[2],kombinacija[3])
    return kombinacija

def tekstSkocko():
    print("Ovo je igra skočko")
    print("Potrebno je da pogodite tačnu kombinaciju simbola \U0001F929, \u2663, \u2660, \u25C6, \u2764, \u2605")
    print("Da biste sa tastature uneli odgovarajuci simbol potrebno je da unesete broj:")
    print("0 za simbol srce \u2764")
    print("1 za simbol tref \u2663")
    print("2 za simbol pik \u2660")
    print("3 za simbol karo \u25C6")
    print("4 za simbol skočko \U0001F929")
    print("5 za simbol zvezda \u2605")
    print("Morate pažljivo da pogađate kombinaciju jer imate samo 6 pokušaja")

def prevod(zad):
    br1 = SIMBOLI.index(zad[0])
    br2 = SIMBOLI.index(zad[1])
    br3 = SIMBOLI.index(zad[2])
    br4 = SIMBOLI.index(zad[3])
    broj = str(br1) + str(br2) + str(br3) + str(br4)
    #print(broj)
    return broj


""" def pogodiSkocka(unos, zadato):
    izlaz = [0, 1, 2, 3]
    for i in range(4):
        if unos[i] == zadato[i]:
            izlaz[i]="\U0001F534"
        else:
            izlaz[i]="\U0001F7E1"
    print(izlaz[0],izlaz[1],izlaz[2],izlaz[3]) """


def bodovi(korak):
    ukupno = korak*5
    print("Osvojeni broj bodova je:",ukupno)
    if korak >0:
        print("Čestitamo!!!")
        print("POBEDILI STE!!!")
    else:
        print("Bilo je zabavno igrati se, ali na žalost :< izgubili ste :<")

def pobednik(resenje):
    print("Kombinacija koju je trebalo pogoditi je:")
    print(*resenje, sep="  ")


def pogodiSkocka(zadato):
    izlaz = [1, 2, 3, 4]
    koraci = 6
    
    while koraci>0:
        pogodjen = 0
        postoji = 0
        nema = 0
        #unos = input("unesi: ")
        #u slucaju da unos nije dobro unet on se mora uneti ponovo

        while True:
            unos = input("unesi: ")  
            broj = unos.isdigit()
            duzina = len(unos)
            if duzina == 4 and broj:
                break
            else:
                print("eej, moraš lepo da uneseš ")

        ispis(unos)

        #izlaz = [0, 1, 2, 3]
        for i in range(4):
            if unos[i] == zadato[i]:
                #izlaz[i]="\U0001F534"
                pogodjen += 1
        
        for i in range(4):
            if zadato[i] in unos:
                postoji += 1
        postoji = postoji - pogodjen
         
        for i in range(4):
            if zadato[i] not in unos:
                nema += 1

        if pogodjen == 4:
            print("\U0001F534 \U0001F534 \U0001F534 \U0001F534")
            break
        
        #ispisati kruzice
        for i in range(4):
            if pogodjen>0:
                izlaz[i]="\U0001F534"
                pogodjen -= 1
        for i in range(4):
            if izlaz[i]!="\U0001F534":
                if postoji>0:
                    izlaz[i]="\U0001F7E1"
                    postoji -= 1
        for i in range(4):
            if (izlaz[i]!="\U0001F534" and izlaz[i]!="\U0001F7E1"):
                if nema>0:
                    izlaz[i]="\U000026AB"
                    nema -= 1
                
        print(izlaz[0],izlaz[1],izlaz[2],izlaz[3])
        izlaz = [1, 2, 3, 4]

        koraci = koraci - 1
    bodovi(koraci)

def ispis(uneto):
    simboli = [1, 2, 3, 4]
    for i in range(4):
        simboli[i] = uneto[i]
        a = int(simboli[i])
        simboli[i]=SIMBOLI[a]
    print(*simboli, sep = "  ")
       
    
 

if __name__ == "__main__":
    tekstSkocko()
    resenje = generator()
    pravores = prevod(resenje)
    pogodiSkocka(pravores)
    pobednik(resenje)
    

